+++
title = "Software Libre, Software Legal"
date = 2005-02-04
+++

En el [GLUC](http://gluc.unicauca.edu.co/) nos ha ido bastante bien por estos días, la Vicerectoría de Bienestar y Cultura de la [Universidad del Cauca](http://www.unicauca.edu.co/) nos aprobó un proyecto bastante interesante, se trata de una Campaña antipiratería y pro-software libre llamada [“Software Libre, Software Legal”](http://gluc.unicauca.edu.co/wiki/index.php/Archivo:Campa%F1a-antipirateria.sxw). La ídea del proyecto es dar una serie de charlas que concientisen sobre por qué no se debe usar software pirata y por qué es mejor usar software libre en su lugar. Con la aprobación del proyecto, el grupo recibirá una cantidad de dinero con la cual se piensa hacer afiches de publicidad, regalar distribuciones de Linux, y programas libres para Windows entre otras cosas. Uno de los puntos claves del proyecto es la participación en la Ciudad de el [Primer Festival Latinoamericano de Instalación de Software Libre – FLISOL](http://ingenieria.ean.edu.co/%7Eazul/svnwiki.cgi/colibri/fisl/default), del cual ya había hablado previamente. Esperamos que con el dinero que nos de la universidad podamos realizar un gran evento aquí en Popayán.

## Grupo Mono.

El sábado pasado regresamos a las actividades en el [Grupo de Estudio en Mono](http://gluc.unicauca.edu.co/wiki/index.php/GrupoMono) del [GLUC](http://gluc.unicauca.edu.co/). Ese día sólo nos dedicamos a organizar lo que se hará en el grupo durante el resto del semestre. Se decidió continuar en base a la [lista ToDo](http://gluc.unicauca.edu.co/wiki/index.php/GrupoMono#Temas_y_Responsables) que quedó despues del curso de C#. La idea es que cada uno de los miembros del grupo se apropie de una parte del curso.

Algo bastante interesante es que he hablado con varios amigos que viven fuera de Popayán, y hay muchos que están interesados en el [Grupo de Estudio](http://gluc.unicauca.edu.co/wiki/index.php/GrupoMono), entonces han entrado a formar parte de este como integrante virtuales. Los integrantes virtuales darán charlas por IRC y estarán pendientes de lo que se haga en en grupo leyendo el material del [FTP](ftp://ciclope.unicauca.edu.co/gluc/grupo_mono/).

Con todo esto, nuevamente surge la idea de crear una comunidad de Mono en Colombia. Incluso ya tenemos un proyecto en [el-directorio.org](http://el-directorio.org/)

## Tutorial de GTK#

Con el [tutorial de GTK#](http://www.monohispano.org/tutoriales/man_gtksharp/) estoy un poco atrasado, aun no termino el capítulo 8. Sin embargo, en general el proyecto de creación del tutorial ha avanzado bastante. Mahomedalid Pacheco se une al equipo y ya ha enviado los capítulos [20](http://www.monohispano.org/tutoriales/man_gtksharp/ch-draganddrop.html) y [21](http://www.monohispano.org/tutoriales/man_gtksharp/ch-gtkrcfiles.html). Últimamente hemos tenido bastantes charlas en el equipo, discutiendo temas como el estilo de codificación, los screenshots etc. Parece que todo va muy bien por este lado.

## MonoUML

En lo que respecta a [MonoUML](http://monouml.sourceforge.net/), en estos días me estoy dedicando completamente al nuevo diseño de UMLCanvas#. He subido lo que tengo de los diagramas al CVS para que sea más fácil la participación de todos. Una de las características que más me gusta del nuevo diseñó es la utilización de una serie de interfaces IHandler para manejar los eventos y el comportamiento de los elementos del canvas. El hecho de desacoplar el manejo de enventos de los propios objetos es algo brinda bastante flexibilidad al diseño. También he comenzado a estudiar un poco las librerías GDI, ya que me gustaría que UMLCanvas# pudiera usarlas además de [GnomeCanvas](http://developer.gnome.org/doc/whitepapers/canvas/canvas.html); esto previendo un futuro port para Windows.

Me bajé [Poseidon for UML Community Versión](http://www.gentleware.com/). En realidad nunca antes lo había probado, no se porque siempre pensé que era muy parecido a [ArgoUML](http://argouml.tigris.org/), el cual no me gusta mucho que digamos. La verdad es que Poseidon es bastante diferente a [ArgoUML](http://argouml.tigris.org/); me ha gustado mucho, incluso lo prefiero a otros como [Rational Rose](http://www.rationalrose.com/). El único problema que le veo es que es tremendamente pesado, en mi máquina ha llegado a consumir casi 500 MB de memoria. El canvas es especialemente lento, no se si es que no está funcionando la aceleración por hardware o qué, sin embargo, este es bastante agradable de usar. Espero que el canvas de [MonoUML](http://monouml.sourceforge.net/) llegue a ser tan cómodo de usar como el de [Poseidon](http://www.gentleware.com/), incluso creo que lo podría superar.
