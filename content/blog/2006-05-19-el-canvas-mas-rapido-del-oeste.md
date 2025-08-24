+++
title = "El Canvas más rápido del oeste"
date = 2006-05-19
+++

Esta semana [Mario](http://mario.monouml.org/) y yo hemos estado trabajado para optimizar al máximo [MonoCanvas](www.monouml.org/wiki/MonoCanvas). La idea es lograr un rendimiento similar a [Dia](http://www.gnome.org/projects/dia/). Creo que hasta el momento se ha avanzado bastante. Yo he estado portando lo que ya estaba de GDI+ a [Cairo](http://www.cairographics.org/) directamente. Mario está haciendo una re-implementacion usando widgets de Gtk#. Lo interesante de este enfoque es que se aprovecha toda la lógica, ya bastante optimizada a través de los tiempos, que ya usa [GTK+](http://www.gtk.org/).

Para las pruebas con Cairo, he usado una pequeña aplicación Gtk# con 100, 200 o más widgets. He hecho pruebas con Dia y empieaza a flaquear más o menos al mover 200 formas simultaneamente. Con este número de formas, la taza de actualización del _canvas_ se reduce drásticamente, a menos de 4 repintadas por segundo. Los resultados con el nuevo _canvas_ basado en Cairo son similares a los de Dia, sin embargo, hay que tener en cuenta que la versión de Cairo usa _antialiasing_ y transparencias mientras que Dia no. La verdad es que estoy muy satisfecho y creo que incluso hay potencial para optimizar más.

Aquí hay unos pantallazos de MonoCanvas basado en Cairo y Dia:

![Image 1: Pantallazo de Mono Canvas Test](/images/el-canvas-mas-rapido-del-oeste/monocanvas1.png)
![Image 2: Pantallazo de Dia](/images/el-canvas-mas-rapido-del-oeste/dia.png)

Por supuesto la versión de Cairo no es simplemente un cambio de GDI+ por Cairo, también son varios cambios que hacen más óptimo el programa. Dibujar a través de Gtk.DotNet es bastante lento. Y no sólo se trata de que el API `System.Drawing` esté basada en `libgdiplus` que a su vez esta implementada encima de Cairo, sino que el procedimiento de obtener un `Drawing.Graphics` de un `Gdk.Drawable` no es el más eficiente. He aquí un pedazo del [código de Gtk.DotNet.Graphics](http://svn.myrealbox.com/viewcvs/trunk/gtk-sharp/gtkdotnet/Graphics.cs?rev=59518&view=markup):

```cs
public static System.Drawing.Graphics FromDrawable(
  Gdk.Drawable drawable,
  bool double_buffered)
{
    ...

    Type graphics = typeof (System.Drawing.Graphics);
    MethodInfo mi = graphics.GetMethod (
      "FromXDrawable",
      BindingFlags.Static | BindingFlags.NonPublic
    );
    if (mi == null)
        throw new NotImplementedException(
        "In this implementation I can not get a graphics from a drawable");
    object [] args = new object [2] {
      (IntPtr) gdk_x11_drawable_get_xid (drawable.Handle), (IntPtr) display
    };
    object r = mi.Invoke (null, args);
    System.Drawing.Graphics g = (System.Drawing.Graphics) r;

    ...

    return g;
}
```

Este método es el que se llama cada vez que se repinta parte del _canvas_ cuando se usa `Gtk.DotNet`. El cual se debe llamar, además de todas las operaciones de dibujo, unas 40 veces por segundo para lograr un movimiento fluido. Rápidamente se pueden observar dos problemas de rendimiento. Por un lado, el uso de System.Reflection para encontrar el método FromXDrawable y por el otro, la creación del objeto args.

Cuando se usa Cairo, en cambio, se usa el método `Gdk.CairoHelper.Create` que está basado en la implementación nativa que viene con el nuevo GTK+ 2.8, por lo tanto las cosas se hacen considerablemente más rápido.

La clave del rendimiento es dibujar lo menos posible. Definitivamente las operaciones de dibujo son las que más tardan, hay que hacer todo lo posible por no dibujar lo que no es necesario. Otras operaciones que puede pensarse son lentas, como las iteraciones a largas listas, en realidad no influyen mucho. Algo a tener en cuenta es que dibujar donde no se ve, es decir, fuera del QueueDrawArea también influye en el rendimiento, hay que evitarlo.

Otra cosa bastante curiosa es que el rendimiento depende bastante de la forma que se esté dibujando. Por ejemplo, una elipse es más lenta que un rectágunlo. Pero mucho más curioso es que una elipse con borde y sin relleno, es casi tres veces más lenta que una con relleno y sin borde. Algo similar pasa con los rectángulos.

El API de Cairo me ha gustado bastante. Es bastane parecido a [OpenGL](http://www.opengl.org/), por lo que es bastante familiar para mi. Aunque tiene [alguas cosas raras](http://www.cairographics.org/FAQ), me ha gustado mucho más que System.Drawing, creo que es mucho más flexible.

Pronto uniremos el trabajo de Mario con el mio en la versión definitiva de MonoCanvas.
