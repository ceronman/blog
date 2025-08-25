+++
title = "Ceronman IV"
date = 2025-08-24
+++

Este blog se ha mudado de nuevo. Esta es la cuarta mudanza. También me di cuenta de que este blog ya cumplió los **21 años** (es una pena que se me pasaran los 20). Y sí, es cierto que los últimos años han estado bastante escasos de contenido, pero bueno, el blog todavía respira y no se muere hasta que se muera. Durante la mudanza me dio nostalgia leer muchas de las cosas que he escrito a lo largo de estos años. También me dio envidia de mi yo del pasado y su menor prevención.

Esta entrada es acerca de las distintas versiones de este blog. Quise escribir en español porque hace tiempo que no lo hacía. Sé que algunos de los poquísimos lectores de esta diminuta partícula del internet no hablan español, pero afortunadamente las máquinas se han vuelto muy buenas para traducir 😀.

## Ceronman I

La primera versión de este blog comenzó en [Blogspot](https://ceronman.blogspot.com/). Todavía existe esa versión, nunca quise cerrarla. Para ese entonces era estudiante y dedicaba mucho tiempo al [Grupo de Usuarios de Linux de la Universidad](http://gluc.unicauca.edu.co). Uno de los objetivos de ese blog, aparte de divertirse con el Internet de principios de los 2000, era practicar mi inglés, que como se puede ver en las entradas de esa época, era pésimo. Al principio el blog era una especie de bitácora (como eran los blogs antes) de la vida diaria. Pero poco a poco fue cambiando para escribir sobre los proyectos o intereses que pasaban por mi mente. O cosas de tecnología que conocía y me causaban curiosidad. Eventualmente también empecé a escribir en español porque sencillamente era más fácil para mi. Este fue el periodo más activo de este blog.

## Ceronman II

En 2006, Alejandro Forero me convenció de mudar mi blog a [svnwiki](https://web.archive.org/web/20071011151759/http://wiki.freaks-unidos.net/svnwiki/) (antes conocido como *svnblog*). *svnwiki* era un sistema genial y adelantado a su tiempo que Alejandro había escrito en su tiempo libre. Era algo muy parecido al flujo de trabajo que hoy en día se tiene con los generadores de sitios web estáticos como [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/) o [Zola](https://www.getzola.org/). Pero esto fue en 2006, antes de que [Git](https://en.wikipedia.org/wiki/Git) o [Markdown](https://en.wikipedia.org/wiki/Markdown) fueran populares. [GitHub](http://github.com/) ni siquiera existía.

*svnwiki* estaba basado en [Subversion](https://subversion.apache.org/), el sistema de versiones más popular de la época. Y también usaba su propio lenguaje de marcado ligero inspirado en el de [Wikipedia/Mediawiki](https://www.mediawiki.org/wiki/Help:Formatting), no muy diferente del Markdown actual. Escribir en el blog era cuestión de hacer *checkout* del repositorio, que contenía todos los posts como simples archivos de texto plano, agregar uno y hacer *push* (o bueno, *commit*, SVN no tenía el concepto de *push*). Esto disparaba el sistema de generación de contenido estático que actualizaba el blog o la web inmediatamente. Un flujo de trabajo con cero fricción y realmente genial. Alejandro es una de las personas más brillantes que he conocido. Me encantaba como funcionaba mi blog en esta época.

## Ceronman III

A finales de 2011, el VPS donde estaba alojado *svnwiki* implosionó. Bueno, realmente no recuerdo qué le pasó. Tal vez se le quemó el disco duro o algo parecido. El caso es que todo el contenido se perdió y no había backups. La magia de la [indie web](https://indieweb.org/). Alejandro ya no estaba muy interesado en el proyecto, así que hasta ahí llegó.

Para ese entonces, yo ya no escribía tanto. Me tomó algún tiempo darme cuenta de que el blog se había caído. Llevaba varios años usando Twitter, y este se había apoderado de buena parte de mis hábitos de escritura. Todo era más fácil, más superficial, había que pensar menos, había más dopamina.

Sin embargo decidí mudarme de nuevo. De vez en cuando seguía teniendo cosas que escribir que no cabían en un trino. Mientras haya un aliento, el blog no ha muerto. Entonces abrí [uno nuevo en Wordpress](https://ceronman.wordpress.com/).

En un golpe de suerte, pude recuperar todos los posts de mi antiguo blog de *svnwiki*. Esto fue gracias al (ahora también difunto) [Google Reader](https://en.wikipedia.org/wiki/Google_Reader). Yo estaba suscrito a mi propio blog y, afortunadamente, el *reader* había guardado una copia de todos mis posts. Gracias a eso, pude migrarlos a mi nuevo blog de Wordpress. También migré los viejos posts de Blogspot.

Esta época tuvo un contenido bastante escaso, pero también creo que tuve buenos posts. Esta fue la primera vez que uno de mis posts llegó a la portada de [Hacker News](https://news.ycombinator.com/). Algo muy chévere de Wordpress es que tenía muy buenas estadísticas de las visitas y es increíblemente emocionante ver cómo se disparan después de que una entrada se vuelve medio viral.

En retrospectiva, el lado negativo de esto es que me creó una cierta prevención para escribir. Tal vez porque las expectativas eran altas. Por eso dije al principio que me dio nostalgia ver lo desprevenido que era antes.  Además de eso, hay que sumar que para esa época ya no era estudiante y tenía menos tiempo para escribir. También debo aceptar que las redes sociales se volvieron una adicción, y la mayoría de mis escritos se fueron a sitios como Twitter, Facebook, Reddit y HN, donde recibía más dopamina. La adicción también hace que se consuma mucho más contenido del que se produce.

Otra cosa notable de este blog es que fue el primero en tener su propio dominio: [ceronman.com](https://ceronman.com) (que ahora dirige aquí).

## Ceronman IV: The Quest for Peace

Y por fin llegamos a la versión actual de este blog.

De Wordpress me gustaban sus estadísticas, pero prácticamente odiaba todo lo demás. Su interfaz es un caos y sus múltiples sistemas nuevos y legacy de escribir son un despelote. Escribir posts con código siempre era tedioso y nunca quedaba como quería. Todo esto mientras pagaba una suscripción relativamente cara. Llevaba mucho tiempo queriendo pasarme a otra cosa, algo donde tuviera más control y el flujo de trabajo fuera más parecido a lo que tenía con *svnwiki*. Y que fuera un poco más *indie*.

Esta versión usa el generador de webs estáticas [Zola](https://www.getzola.org/). El contenido del blog está en [Github](https://github.com/ceronman/blog), por ahora, y se aloja en [statichost](https://www.statichost.eu/), un servicio de *web hosting* orientado a la privacidad. El flujo de trabajo está bastante bien y tengo buen control de cómo se ve todo. Todavía faltan varios ajustes, pero me gusta mucho esta versión minimalista. Este blog no tiene estadísticas, pero en el futuro me gustaría implementar alguna solución que me permita tenerlas respetando la privacidad de los lectores como [Plausible](https://plausible.io/).

Logré migrar todos mis posts anteriores, aunque no fue muy fácil. Traté de automatizarlo usando IA, pero fracasé. Noté que muchos de mis viejos posts tienen enlaces e imágenes rotos. Traté de recuperar lo que pude, pero hay muchas cosas que se han perdido para siempre. Así es como la web se va pudriendo y no hay mucho que hacer.

Prefiero no generar grandes expectativas sobre lo que será el blog de aquí en adelante. Será lo que tenga que ser. Pero debo decir que me divertí escribiendo esta entrada 🙂.

Este blog no tiene comentarios, pero pueden escribirme en el [Fediverso](https://col.social/@manuelceron) o por cualquier otro medio.
