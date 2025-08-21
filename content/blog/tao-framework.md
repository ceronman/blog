+++
title = "Tao Framework"
date = 2005-05-30
+++

## Tao

Desde hace unas semanas he estado experimentando un poco con [Tao Framework](http://www.mono-project.com/Tao), un conjunto de recubrimientos a varias librerías para el desarrollo de software multimedia y videojuegos, algo que toda la vida me ha llamado mucho la atención. Aprovechando esto, hace unas semanas me comprometía a dar una charla sobre Tao en una de las reuniones del [GLUC](http://gluc.unicauca.edu.co/), la charla se tituló Programación Multimedia con Mono.

Me llama mucho la atención la idea de tener un framework para el desarrollo de videojuegos realmente multiplataforma, y en este sentido Tao es bastante impresionante, las Dll de Tao funcionan muy bien en distintas plataformas sin recompilar, digo que es sorprendente porque Tao es una librería totalemente escrita a base de llamadas a funcionalidad nativa (Platform Invoke).

El desarrollo de videojuegos es un tema que siempre me ha apasionado, y una de las cosas que he aprendio es que el rendimiento es uno de los requerimientos más importantes. Hasta el momomento, la mayoría de los desarrolladores de juegos trabajan con C y C++; opciones como Java o Mono/.NET no son muy bienvenidas debido al problema del rendimiento. Sin embargo, parece que últimamente algunas personas están considerando la idea de usar herramientas de programación de más algo nivel, tal vez es hora de sacrificar un poco el rendimiento para dar paso a un desarrollo un poco más fácil. Ya hemos escuchado hablar de Mono como una plataforma de desarrollo para el escritorio, qué tal una plataforma de desarrollo para videojuegos, tal vez no sea una idea tan descabellada…

## Grupo Mono

El [grupo de estudio en Mono](http://gluc.unicauca.edu.co/mono) retomó actividades. En este semestre semestre hemos decidio dedicarnos más a la parte práctica, para ello vamos a comenzar a desarrollar una pequeña aplicación con fines educativos. La idea que tenemos es hacer un sencillo editor de HTML. De esta forma pensamos probar algunos componentes interesantes como Gtksourceview#, Gecko#, Glade# entre otras cosas. Vamos a ver como nos vá con esta pequeña prueba.

## MonoUML

Despues de analizar varias alternativas: DiaCanvas, GnomeCanvas, Cairo, Rsvg; creo que la mejor opción para UMLCanvas# va a ser System.Drawing (GDI+). Las otras APIs tienen varios inconvenientes: Diacanvas# es muy inestable, GnomeCanvas pronto estará obsoleto (deprecated), Cairo es de muy bajo nivel, y Rsvg no parece ser el tipo de librería para hacer el trabajo. System.Drawing está basado en Cairo y su diseño es bastante interesante. Ahora, gracias a Gtk.DotNet, se puede acceder a toda la funcionalidad de System.Drawing desde una aplicación Gtk#.
