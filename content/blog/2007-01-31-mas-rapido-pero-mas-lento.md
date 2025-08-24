+++
title = "Mas rápido, pero mas lento"
date = 2007-01-31
+++

En estas vacaciones de diciembre, fui a visitar a mi familia en Medellín. Mi tía Patricia tenía un viejo computador portátil Toshiba Satellite Pro 440 CDT que ya no usaba y decidió regalárselo a mi Papá. Es un portátil que ya tiene sus 11 años, pero, dado que mi papá escasamente usa el PC para leer y escribir correos electrónicos, navegar por Internet y de vez en cuando escribir una carta, le sirve perfectamente. Por supuesto, como buen entusiasta de software libre, pensé que si se le instalara Linux se podría explotar más su potencial. Sin embargo, rápidamente descubrí algo que me dejó atónito y me motivó a escribir esta entrada en mi blog.

El Toshiba Satellite Pro 440 CDT tiene las siguientes características:

* Procesador Intel Pentium MMX de 166 Mhz
* Memoria 32 MB Disco Duro 2 GB.
* Software Microsoft Windows 98 y Microsoft Office 97.

Después de ver las características tan bajas del equipo, hay algo que me da muchísima tristeza. Office arranca mucho, muchísimo más rápido que el OpenOffice de mi PC. Casi cuatro veces más rápido. Aún cuando mi PC tiene 32 veces más memoria que el portátil y un procesador con 20 veces más Mhz. No estoy muy seguro de esto pero, en mi opinión, Office 97 y OpenOffice 2.0 tienen prácticamente la misma funcionalidad.

Después de jugar un rato con el portátil me di cuenta que la velocidad general de sistema, arranque del sistema operativo, apertura de archivos, etc es bastante buena, muy comparable a la de mi PC. Es cierto que hay varias cosas que no pueden ser iguales, por ejemplo, creo que el portátil explotaría antes de poder usar algo como [F-Spot](http://f-spot.org/) o editar imágenes de 8MP con GIMP. La interfaz de mi PC también es más bonita, con más resolución y efectos interesantes. En fin, creo que hay un millón de cosas que no podría ser iguales, pero en el caso de programas como OpenOffice y Office, que son prácticamente iguales, el hecho de que haya un rendimiento similar, o incluso superioridad en el computador de 11 años de edad, me parece algo desgarrador.

¿Qué es lo que pasa? Culpo a los programadores. Somos especialistas en derrochar toda cantidad de recursos que tengamos disponibles. Anteriormente los computadores venían con 32 MB de memoria y los programas tenían que funcionar con eso, y funcionaban. Eso hacía que los programadores se interesaran por mejorar el uso de los recursos. Ahora hay abundancia y se puede derrochar.

Aunque hoy en día tenemos hardware decenas de veces más rápido que hace diez años, parece ser que la calidad y rendimiento de los programas no ha crecido en la misma proporción (si es que ha crecido en algo).

Hay casos mucho más extremos aún. En el mundo del desarrollo de juegos siempre se ha mantenido una tradición de explotar al máximo las capacidades del PC. Es quizás por esto que los juegos son los únicos que parecen mostrar un verdadero avance proporcional a los adelantos en hardware. Recuerdo cuando alguna vez escribí un sencillo juego para PlayStation. El sistema contaba con la miserable cantidad de 1MB de memoria de vídeo y 2MB de memoria de sistema. A mi me parecía demasiado difícil hacer algo con tan pocos recursos, sin embargo los expertos hacían juegos espectaculares con eso. Sabían usar muy bien los recursos.

El tema no necesariamente da para comparar programas viejos con nuevos. Hoy en día también hay buenos programadores que saben utilizar adecuadamente sus recursos. Hay un perfecto ejemplo de dos programas contemporáneos que tienen funcionalidad muy similar pero difieren enormemente en el uso de recursos: [uTorrent](http://www.utorrent.com/) y [Azureus](http://azureus.sourceforge.net/).

La descarga de uTorrent es de 170KB, la de Azureus es de 9.4 MB, eso es 57 veces más, todo esto sin contar detalles como que Azureus requiere un _runtime_ de Java (~50MB) y que viene en un instalador comprimido (bz2) mientras que uTorrent viene en un ejecutable _standalone_ listo para ser ejecutado. El consumo promedio de Memoria de uTorrent es de 4.6MB, mientras que el de Azureus es de 40MB. El consumo de CPU es difícil de medir, pero los desarrolladores de uTorrent dice puede correr hasta en un CPU 486, eso ni siquiera cumple los requisitos mínimos del _runtime_ de Java, en el caso de Azureus.

Ambos programas tienen casi las mismas funcionalidades, Azureus era el más popular, sin embargo, gracias a la superioridad en rendimiento de uTorrent, este le ha ganado el puesto y su popularidad crece en forma exponencial.

Hay otra razón por la cual hay tanta diferencia en estos programas: El lenguaje de programación. Aceptémolo, por más que varios estudios aseguren que la velocidad de los programas escritos en lenguajes como Java, C#, Python, Lisp, etc. sea igual o, algunos se atreven a decir, superior que C o C++, la verdad es que en la práctica todos los programas realmente eficientes están escritos en C o C++. uTorrent está escrito en C++, Microsoft Office está escrito en C++. Azureus está escrito en Java, OpenOffice está en gran parte escrito en Java. Pero ojo, esto no quiere decir que todos los programas de C++ sean necesariamente eficientes.

Es cierto que otros lenguajes hace al programador más productivo y en general más feliz, pero creo que es difícil negar que con C y C++ se puedan obtener programas más rápidos. ¿O tal vez sea mejor decir que con un poco más de esfuerzo a la hora de programar, esfuerzo al que casi siempre nos obliga C++, se obtengan mejores programas?

C++ siempre me encantó y lo usé mucho para muchos proyectos. Hace un tiempo me enamoré de Python y ha pasado bastante tiempo desde la última vez que usé C++ ¿Será que es tiempo de abrir el baúl y volver a sacar esos conocimientos de C++? ¿O será mejor seguir con los lenguajes de alto nivel y más bien tratar de hacer esfuerzos para lograr un balance entre felicidad del programador y eficiencia del programa?
