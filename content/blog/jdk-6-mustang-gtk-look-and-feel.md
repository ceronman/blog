+++
title = "JDK 6 (Mustang) GTK+ Look and Feel"
date = 2006-03-05
+++

Durante estos días decidí probar la [versión beta de Java 1.6](https://mustang.dev.java.net/), apodada “Mustang”. Según había leído por [aquí](http://www.osnews.com/story.php?news_id=10986) y por [allá](http://ensode.net/java_swing_mustang_screenshots_gtk.html), esta nueva versión traerá varias mejoras en cuestión de las interfaces gráficas Swing. La idea es que Swing tenga una apariencia más parecida a las interfaces nativas dependiendo del sistema operativo en el que se estén ejecutando. Me gusta mucho esta idea, y desde el principio soñé con ver [algunas](http://www.jedit.org/) [aplicaciones](http://freemind.sourceforge.net/) Swing que me gustan con la misma apariencia que el resto de mi entorno Gnome.

Se supone que Swing en JDK 6 hace uso de _widgets_ nativos de GTK+, pero, según lo que probé, me parece que lo que en realidad pasa es que Swing trata de imitar el estilo de GTK+. Esto se puede comprobar fácilmente al ver diferencias sutiles (otras no tanto) entre Swing con tema GTK+ y una verdadera aplicación GTK+.

He aquí unos pantallazos de la aplicación de demostración que viene con el JDK, SwingSet2, con diferentes temas de Swing:

![Image 1: Pantallazo-SwingSet2-Swing-Metal](/images/jdk-6-mustang-gtk-look-and-feel/swing1.png)

![Image 2: Pantallazo-SwingSet2-GTK-Clearlooks](/images/jdk-6-mustang-gtk-look-and-feel/swing2.png)

![Image 3: Pantallazo-SwingSet2-GTK-Human](/images/jdk-6-mustang-gtk-look-and-feel/swing3.png)

Desde aquí se ven varias cosas interesantes. Una es que el tema de GTK+ en Swing cambia en forma coherente con el tema actual de Gnome, prueba de ello es que dos de los pantallazos con tema GTK+ tienen tema de Gnome diferente, uno usa Clearlooks y el otro usa Human. Otra cosa bastante curiosa es ver cómo implementan una interfaz tipo [MDI](http://en.wikipedia.org/wiki/Multiple_document_interface), que no están soportadas por GTK+. También se puede ver que a este estilo MDI le falta mucho por pulir, los botones de las ventanas internas aún están bastante burdos.

Para comparar como son renderizados algunos _widgets_ específicos, aquí hay un diálogo típico de Gnome junto a algunos diálogos de preferencias de JEdit con tema GTK+ activado:

![Image 4: Pantallazo-Preferencias de ventana-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing4.png)

![Image 5: Pantallazo-Opciones JEdit-Swing-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing5.png)

![Image 6: Pantallazo-Opciones JEdit 2-Swing-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing6.png)

La primera diferencia que se nota es que los _widgets_ de Swing GTK+ usan una fuente de texto diferente de los _widgets_ GTK+ reales. Para mi esto es crucial para no sentirse como en casa usando Swing. Ojalá que lo corrijan para la versión definitiva.

Algunos _widgets_ en Swing GTK+ son casi idénticos a la versión real de GTK+, es el caso de los GtkCheckButton y los GtkRadioButton. Sin embargo, digo que son “casi idénticos” porque la versión de Swing no cuenta con pequeños detalles proporcionados por temas como Clearlooks, como los efectos de desvanecimiento suave en los GtkCheckButton. Otros _widgets_ definitivamente son muy diferentes, es el caso de los GtkHScale y los GtkComboBoxEntry, que se notan bastante diferentes en la versión Swing. Otra cosa diferente son las barras de desplazamiento cuadradas al estilo GtkScrollBar en lugar de las redondeadas estilo GtkTextView.

Parece que la gente de Sun no sólo se ha preocupado por la similitud a nivel de _widgets_ simples, sino que también han hecho algunos de los diálogos usuales bastante similares. He aquí algunos pantallazos:

![Image 7: Pantallazo-Abrir-GTK]((/images/jdk-6-mustang-gtk-look-and-feel/swing7.png))

![Image 8: Pantallazo-Abrir-JDK](/images/jdk-6-mustang-gtk-look-and-feel/swing8.png)

Bueno, en realidad los diálogos de selección de archivos son muy diferentes. No encuentro el por qué Sun decidió usar el antiguo dialogo de abrir de GTK+ en lugar del nuevo. Este sí que me parece que es un punto negativo.

![Image 9: Pantallazo-Escoger Fuente-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing9.png)

![Image 10: Pantallazo-Escoger Fuente-JDK](/images/jdk-6-mustang-gtk-look-and-feel/swing10.png)

Aquí se pueden ver las diferencias entre los diálogos de selección de fuente. Se parecen bastante, aunque algunas cosas están en diferente orden y para ciertas cosas (texto de muestra) se usan _widgets_ diferentes. De nuevo se nota aquí la diferencia entre las barras de desplazamiento diferentes, cuadradas en Swing GTK+ y redondeadas en Gnome.

![Image 11: Pantallazo-Escoger Color-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing11.png)

![Image 12: Pantallazo-Escoger Color-JDK](/images/jdk-6-mustang-gtk-look-and-feel/swing12.png)

![Image 13: Pantallazo-Escoger Color-Swing-Metal](/images/jdk-6-mustang-gtk-look-and-feel/swing13.png)

Aquí hay una comparación de tres diálogos de selección de color. Uno es el original de Gnome, otro es de Swing GTK+ y otro es de Swing Metal. El diálogo de Swing GTK+ es bastante parecido al de Gnome. De nuevo se notan diferencias en los _widgets_, como por ejemplo los GtkSpinButtons. También hay cosas que faltan y cosas que se agregan, como el botón del gotero (se quitó) o la vista preliminar de texto (se agregó). En el triángulo de selección de color se puede notar como la versión de Swing GTK+ es mucho más burda, a diferencia de la versión Gnome que usa un bonito _antialiasing_, el cual viene desde GTK+ 2.8, gracias a Cairo. Supongo que Swing no usa nada similar a Cairo por debajo. Otra parte donde se nota una extraña inconsistencia es en los botones “aceptar” y “cancelar”, los cuales no usan los iconos de botones estándar. Y digo que es extraña esta inconsistencia es porque en el diálogo de selección de archivo si lo usaban.

En el último pantallazo se ve el mismo diálogo de selección de color, sacado exactamente de la misma parte de la misma aplicación, pero usando el tema Metal de Swing. Aquí se nota cómo un mismo diálogo de Swing puede verse radicalmente diferente dependiendo del tema que se use. No sé que tan bueno sea esto.

Al final dejo dos pantallazos comparando JEdit con tema GTK y tema Metal:

![Image 14: Pantallazo-jEdit-Swing-GTK](/images/jdk-6-mustang-gtk-look-and-feel/swing14.png)

![Image 15: Pantallazo-jEdit-Swing-Metal](/images/jdk-6-mustang-gtk-look-and-feel/swing15.png)

Aparte de las diferencias de apariencia, existe otro problema grave, gravísimo con Swing GTK+: El rendimiento. Y es que cuando se activa el tema de GTK+ la aplicación se vuelve considerablemente más lenta en comparación con el tema Metal, y, por supuesto, mucho más lenta que una aplicación GTK+ nativa. Esto si que es un gran problema para la adopción de este _look and feel_ nativo.

Bueno, afortunadamente esta todavía es una versión beta. Estoy seguro que la gente de Sun va a corregir muchos de los errores que existen por el momento. El problema del rendimiento es realmente obligatorio de corregir, por lo menos hacer que sea igual de rápido que Swing Metal. De todos modos me parece que el enfoque que está tomando Sun de imitar GTK+ no es el más adecuado, creo que nunca va a ser posible tener un 100% de concordancia. Por ahora me parece que la mejor opción para tener un _look and feel_ nativo en Java es SWT, usado por aplicaciones como Eclipse o Azureus.
