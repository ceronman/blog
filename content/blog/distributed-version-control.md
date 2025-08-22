+++
title = "Distributed Version Control"
date = 2008-04-14
+++

Actualmente se está dando una avalancha de migraciones desde sistemas de control de versiones centralizados ([Subversion](http://subversion.tigris.org/)) hacia sistemas distribuidos. Prácticamente todos los grandes proyectos de software libre o ya migraron o están en discusiones sobre la migración o están usando sistemas paralelos.

A diferencia de lo que sucedió con Subversion, donde también hubo una avalancha de migraciones desde [CVS](http://en.wikipedia.org/wiki/Concurrent_Versions_System), en esta ocasión hay varias buenas alternativas, lo que hace la cosa mucho más interesante. La _guerra_ entre [Git](http://git.or.cz/), [Mercurial](http://www.selenic.com/mercurial/) y [Bazaar](http://bazaar-vcs.org/), está generando un montón de innovaciones en el campo del control de versiones. Nos está beneficiando mucho a nosotros los usuarios.

La carrera por popularidad la va ganando Git con proyectos como Linux, X.org, freedesktop.org, Wine, OLPC,[entre otros](http://git.or.cz/gitwiki/GitProjects). Mercurial va muy cerca con proyectos como Mozilla, OpenSolaris, OpenJDK, Xen, [entre otros](http://www.selenic.com/mercurial/wiki/index.cgi/ProjectsUsingMercurial). Bazaar va en último lugar siendo usado por Ubuntu y [otros más](http://bazaar-vcs.org/WhoUsesBzr).

Git está escrito en C y muchos de sus comandos son scripts de Shell y Perl. En consecuencia, el soporte de Git en Windows es muy pobre. Mercurial está escrito principalmente en Python. Algunas rutinas cuello de botella están escritas en C. Mercurial funciona muy bien en Windows. Bazaar es 100% Python. Funciona muy bien en Windows. Mercurial y Bazaar son extensibles via Python.

Git va en primer lugar en cuanto a velocidad, Mercurial de segundo, Bazaar de tercero.

Git tiene una interfaz de usuario difícil de comprender. Mercurial y Bazaar son muy fáciles de usar.

En cuestión de documentación, Mercurial se lleva el primer puesto, Bazaar el segundo y Git, de lejos, el tercero.

Elegir uno de los tres es una tarea complicada. Hay un millón de páginas y entradas de blog que hablan a favor de uno u otro. Como van las cosas es muy posible que haya que aprender a usar los tres, al menos a un nivel básico. Mi elección personal ha sido Mercurial, por su documentación, facilidad de uso y velocidad.

Mi experiencia en las últimas semanas con Mercurial ha sido muy placentera. Los sistemas distribuidos no solo dan una gran ventaja para proyectos grandes y con muchos contribuyentes, sino también hace las cosas mucho más fáciles en proyectos pequeños de uno o pocos desarrolladores. Empezar a _versionar_ un proyecto nunca fue más fácil.

Tengo muchos pequeños proyectos que no están _versionados_, por ejemplo los de PyWeek. No lo hago porque me da pereza arrancar un nuevo repositorio de Subversion, importar, hacer checkout… Con Mercurial es tan fácil comenzar un nuevo repositorio que nunca más tendré un proyecto no _versionado_.

La velocidad es un factor muy importante a la hora de que a uno no le de pereza usar un sistema de control de versiones. Con Mercurial todas las operaciones se sienten instantáneas. En cambio Subversion se siente taaan lento, incluso usado localmente.

El poder clonar repositorios fácilmente me da más seguridad. Sé que es menos probable que se pierdan datos. Sitios como [freehg.org](http://freehg.org/) y [github.com](http://github.com/) son lo máximo.

Trabajar al estilo _Branchy Development_ se siente muy bien. Ahora tengo la costumbre de crear un _branch_ por cada nueva característica, por pequeña que sea. Trabajar paralelamente cada cosa en un _branch_ aparte es muy cómodo, ya que una cosa no rompe la otra. Además todo el historial termina mucho más organizado. Luego cuando todo está listo, un _merge_ sin traumas.

A la hora de colaborar a un proyecto de software libre, me parece fundamental el hecho de que uno siempre tiene acceso al sistema de control de versiones. A diferencia de Subversión donde sólo el que tiene acceso de _commit_ puede usarlo. El sistema de red de confianza del que hablaba Linus Torvals en [el famoso vídeo de Git](http://www.youtube.com/watch?v=4XpnKHJAok8), también me parece una forma más natural de hacer las cosas.

Hay dos cosas que no me gustan de Mercurial. Una es que el soporte para Subversion es bastante pobre. No hay algo tan bueno como [Git-svn](http://utsl.gen.nz/talks/git-svn/intro.html). La otra es que la forma de hacer _branches_ haciendo clones todavía se siente muy Subversion, me gusta más el estilo Git ([Ivan habla de ello más detalladamente](http://i-nz.net/2008/04/02/mercurial-my-2-cents/)). No uso Git porque en el trabajo eventualmente me toca hacer ciertas operaciones en Windows. Sin embargo, como dije antes parece que dominar Git va ser esencial pronto. De todos modos aprender Mercurial me ha servido para entender muchos conceptos que no entendí bien cuando comencé a leer sobre Git.
