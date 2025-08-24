+++
title = "Error en Mono"
date = 2006-11-06
+++

Hoy, mientras trabajaba en MonoCanvas, estaba husmeando en el código de [Mono](http://www.mono-project.com/), cuando por casualidad me di cuenta de un error que, al parecer, nadie había notado. El operador de inequidad `!=` entre dos objetos del tipo `System.Drawing.RectangleF` estaba implementado de esta forma:

```cs
public static bool operator != (RectangleF r1, RectangleF r2)
{
	return (r1.X != r2.X) && (r1.Y != r2.Y) &&
        (r1.Width != r2.Width) && (r1.Height != r2.Height);
}
```

Obviamente, la implementación correcta debería ser:

```cs
public static bool operator != (RectangleF r1, RectangleF r2)
{
	return (r1.X != r2.X) || (r1.Y != r2.Y) ||
        (r1.Width != r2.Width) || (r1.Height != r2.Height);
}
```

Aproveché que estaba trabajando con la versión SVN e inmediatamente [hice un parche y lo mandé](http://lists.ximian.com/pipermail/mono-devel-list/2006-November/021199.html).

Es increible como, pese a la gran cantidad de [pruebas unitarias](http://en.wikipedia.org/wiki/Unit_test) que tiene Mono, se haya colado un bug de este tipo. Me he dado cuenta de que en el código trivial, como el de este ejemplo, es más fácil dejar pasar bugs. Esto caso me recuerda mucho al caso del [error en la búsqueda binaria en Programming Pearls](http://googleresearch.blogspot.com/2006/06/extra-extra-read-all-about-it-nearly.html).

Curiosamente el error lo encontré mientras miraba el código, pero ¿qué hubiera pasado si estuviera escribiendo una aplicación que usara ese operador? Creo que hubiera pasado un largo rato partiendome la cabeza antes de siquiera sospechar que es el operador el que tiene un bug. La moraleja de la historia es no subestimar las tareas triviales a la hora de programar.
