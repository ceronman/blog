+++
title = "Fin de los exámenes"
date = 2005-02-27
+++

El lunes pasado terminé exámenes parciales. La siguiente temporada vendrá muy pronto, así que tengo que aprovechar al máximo este tiempo para adelantar muchas cosas que tengo pendientes.

## MonoUML

Ya he comenzado a implementar las primeras partes de UMLCanvas# 2.0. He decidido comenzar por la parte de más bajo nivel. Aunque hasta ahora no he avanzado mucho, me parece que las cosas no van a ser tan complicadas debido a que muchos problemas ya han sido resueltos en la versión actual de UMLCanvas#, aunque en forma un poco desordenada. Estoy bastante optimista en cuanto a esta parte y creo que puede estar lista un poco antes de lo planeado.

El hecho de que UMLCanvas# tenga un diseño flexible que permita cambiar de API gráfica sin mayor traumatismo es más importante ahora que nunca. Según lo que he leído, [GTK+](http://www.gtk.org/) se pasa definitivamente a [Cairo](http://www.cairographics.org/) como librería gráfica. En este contexto quedarían 3 toolkits gráficas que podrían ser usadas por UMLCanvas#: [GnomeCanvas](http://developer.gnome.org/doc/API/2.0/libgnomecanvas/GnomeCanvas.html), [Cairo](http://www.cairographics.org/) y [GDI+](http://www.mono-project.com/contributing/drawing.html) (la cual está basada en [Cairo](http://www.cairographics.org/) en su implementación en Unix). Por ahora se seguirá con [GnomeCanvas](http://developer.gnome.org/doc/API/2.0/libgnomecanvas/GnomeCanvas.html), pero estoy casi seguro de que en un futuro vamos a tener que cambiar y debemos estar preparados para ello.

## GLUC

En el [GLUC](http://gluc.unicauca.edu.co/) seguimos con el proyecto antipiratería del cual ya había hablado antes. También estamos trabajando duro para el [Festival Latinoamericano de Instalación de Software Libre](http://ingenieria.ean.edu.co/%7Eazul/svnwiki.cgi/colibri/fisl/default) que se realizará el 2 de Abril. Por mi parte, me ha tocado hacer un CD-ROM que contenga una colección de programas libres para Windows. Para no empezar todo desde cero, he decidido hacer un hack de [TheOpenCD](http://www.theopencd.org/), el cual por cierto está muy llamativo. Básicamente me ha tocado traducir gran parte de [TheOpenCD](http://www.theopencd.org/), cambiar las imágenes y modificar un par de pequeñeces.

![Image 1: == TheOpenCD hack 1 ==](/images/fin-de-los-examenes/theopencd1.png)
![Image 2: == TheOpenCD hack 2 ==](/images/fin-de-los-examenes/theopencd2.png)

## Free Abuse.

En tiempos de exámenes y exceso de trabajo, nada mejor para quitar el estrés que un buen juego, y mejor aún, un juego libre. Por estos días instalé la [versión libre del clásico Abuse](http://www.labyrinth.net.au/%7Etrandor/abuse/). Abuse es un juego de acción futurista, con aliens, disparos y mucha emoción. Definitivamente entra a encabezar la lista de los mejores juegos libres.

El paquete de [Ubuntu](http://www.ubuntu.org/) de Abuse no funcionó (esto ya se está volviendo costumbre, Ubuntu me tiene aburrido) así que me tocó hacer una mezcla entre el paquete y los binarios disponibles en la página de abuse.

![Image 3: == Abuse Screenshot 1 ==](/images/fin-de-los-examenes/abuse1.jpg)
![Image 4: == Abuse Screenshot 2 ==](/images/fin-de-los-examenes/abuse2.jpg)

## Mono Bundle

Me ha gustado mucho el nuevo instalador genérico de [Mono](http://www.go-mono.org/) para Linux. Funciona en multiples distribuciones y es la forma más fácil de instalar y redistribuir Mono. Lástima que la versión 1.1.4 que era la que más me interesaba no funcionó en [Ubuntu](http://www.ubuntu.org/) (y otra más con Ubuntu).

![Image 5: == Screenshot 1 Mono Bundle ==](/images/fin-de-los-examenes/mono-installer.png)
![Image 6: == Screenshot 2 Mono Bundle ==](/images/fin-de-los-examenes/mono-installer2.png)
![Image 7: == Screenshot 3 Mono Bundle ==](/images/fin-de-los-examenes/mono-installer3.png)
