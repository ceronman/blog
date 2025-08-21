+++
title = "Revelando"
date = 2005-11-29
+++

## Curso de Fotografía

Hace unas semanas me inscribí en un curso de fotografía que estaba dando el Foto Club de la [Universidad](http://www.unicauca.edu.co/). Desde hacía varios semestres quería inscribirme en el curso, pero no había tenido tiempo, este semestre tampoco tenía, así que me tocó decidirme e inscribirme como sea, ya que de otra forma nunca lo iba a hacer. En fin, el curso es a la antigua, con cámaras analógicas manuales, yo he estado usando la magnifica [Canon A1](http://en.wikipedia.org/wiki/Canon_A-1) de mi papá. Al principio quería comprarme una cámara digital, pero la verdad es que me he dado cuenta que la fotografía analógica tiene su encanto, por eso tengo pensado conseguirme una [Canon AE1](http://en.wikipedia.org/wiki/Canon_AE-1) o similar, que sea manual.

En una de las prácticas del curso tomamos unas fotos en blanco y negro por varias zonas de [Popayán](http://es.wikipedia.org/wiki/Popay%C3%A1n). Hicimos todo el proceso manual, desde la escoger objetivo, filtros, velocidad y diafragma, hasta el mismo revelado y copiado. Este último, el revelado, es uno de los aspectos más interesantes de la fotografía analógica. Todo el proceso que va desde desenrollar el rollo completamente a oscuras en la etapa de revelado hasta ver cómo va apareciendo lentamente la foto en el papel bajo una tenue luz roja en la etapa de copiado, es simplemente fascinante.

Esta es mi hoja de contacto de aquella práctica:

![Image 1: Hoja de Contacto](/images/revelando/revelando1.png)

Esta es una de las fotos ya copiada en papel:

![Image 2: Foto de un Árbol](/images/revelando/revelando2.png)

## Mono Canvas

Después de varios meses de no tocar el código de [MonoCanvas](http://www.monouml.org/mediawiki/index.php/MonoCanvas) ni de [MonoUML](http://www.monouml.org/), ayer decidí volver al retomar el trabajo. [MonoCanvas](http://www.monouml.org/mediawiki/index.php/MonoCanvas) ha cambiado mucho desde la última vez que lo vi, [Mario](http://marioc.blogspot.com/) ha avanzado bastante. Durante el fin de semana desempolvé el repositorio del SVN y empecé a corregir algunos bugs y a refactorizar un poco el código. Por ahora el trabajo que falta es re-escribir la parte de los elementos anidados, la cual era la causante de varios bugs, tengo pensando crear una nueva clase aparte para ello. De ahí seguirá el trabajo con las conexiones, que es importantísimo.

Una cosa que todavía me preocupa es el rendimiento, pese a que se han corregido varios [bugs](http://lists.ximian.com/pipermail/mono-devel-list/2005-October/015164.html) en [Mono.Cairo](http://www.mono-project.com/Drawing#Mono.Cairo) por parte del equipo de [Mono](http://www.mono-project.com/), me parece que todavía hay mucho por mejorar, tanto desde la parte de [MonoCanvas](http://www.monouml.org/mediawiki/index.php/MonoCanvas) como del mismo [Mono](http://www.mono-project.com/), en fin, creo que luego hay que dedicarle un tiempo a eso más adelante.

Avance en MonoCanvas:

![Image 3: Screenshot de MonoCanvas](/images/revelando/monocanvas.png)

## DeStar

Continuando con el tema del rendimiento, últimamente me estoy dedicando a mejorar el de [DeStar](http://destar.berlios.de/). Después de analizar detenidamente, por fin he dado con el cuello de botella, que es una sincronización entre datos y metadatos que tienen los configlets. Esta sincronización se requiere cada vez que un configlet es accedido o modificado. El proceso de sincronización es lento porque tiene que recorrer todos los configlets, y por cada uno, recorrer todas sus variables y sincronizarlas, además de otras tareas de bricolaje. El proceso puede llegar a tardar hasta cuatro minutos con una configuración relativamente compleja, lo cual es exageradamente lento. La solución al problema es obvia, cambiar el sistema de sincronización y manejar los configlets con una estructura de datos más apropiada. Sin embargo, esta solución implica reescribir una enorme cantidad de código, es el problema de los errores a nivel de arquitectura. Lo que he estado analizando es cómo podría disminuir el problema sin reescribir mucho código, se me han ocurrido varias ideas, pero han tenido resultados desastrosos, en fin, hay que seguir probando…
