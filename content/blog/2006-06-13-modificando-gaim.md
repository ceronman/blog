+++
title = "Modificando Gaim"
date = 2006-06-13
+++

Uso [Gaim](http://gaim.sourceforge.net/) para manejar todas mis conversaciones de mensajería instantánea. Me gusta tener todas las conversaciones en la misma ventana, no importa de qué red sea. Gaim me permite tener mis conversaciones de IRC, MSN, Yahoo y Google en la misma ventana. Sin embargo, hay algo que siempre me ha molestado de usar Gaim como cliente de IRC: No se puede ver en la lista de usuarios quién está ausente o _away._ Otros clientes como [XChat](http://www.xchat.org/) o [Chatzilla](http://www.mozilla.org/projects/rt-messaging/chatzilla/) si hacen esto. Así que decidí aprovechar las ventajas del software libre y me propuse modificar Gaim para realizara esta tarea.

Aquí hay un pantallazo de XChat mostrando los usuarios _away_ (en gris).

![Image 1: Pantallazo-XChat](/images/modificando-gaim/xchat.png)

En un principio pensé que sería un cambio bastante fácil. Sin embargo, poco a poco me di cuenta de que había una razón por la cual un cambio tan aparentemente sencillo no se había hecho ya. El problema viene directamente desde el [protocolo IRC](http://www.irchelp.org/irchelp/rfc/rfc.html). A diferencia de estados como de operador (_op_) o de voz (_voice_), el estado de ausencia (_away_) no puede obtenerse con un [mensaje names](http://www.irchelp.org/irchelp/rfc/chapter4.html#c4_2_5). Para conocer si un usuario esta _away_ hay que mandar un [mensaje whois](http://www.irchelp.org/irchelp/rfc/chapter4.html#c4_5_2). La solución entonces para conocer qué usuarios están _away_ es mandar un mensaje _whois_ por cada usuario de un canal y, en base a su respuesta, colocar una etiqueta al usuario para indicar que esta _away_. La serie de mensajes _whois_ tendría que mandarse cada cierto tiempo para mantener la lista actualizada. El problema de este enfoque es que se genera un gran _overhead_ al tener que hacer los _whois_ a cada rato. Por esta misma razón fué que a el mantenedor del módulo de IRC de Gaim, [Ethan Blanton](http://irg.cs.ohiou.edu/%7Eeblanton/index.html), no le sonó la idea de implementar esta característica. Cuando le dije que todos los clientes hacen eso, me dijo: _if everybody else jumped off a bridge, would you?_ Creo que estaba de mal genio, cuando le pregunté en #gaim, estaba embolatado con el sistema de señales. Otro día tengo que insistir.

Definitivamente ver el código fuente de proyectos de software libre es una gran experiencia. Uno aprende muchas cosas. El código de Gaim me pareció muy bonito, organizado y fácil de entender. El código de XChat me pareció horrible. Husmear en el código de los programas también sirve para encontrar pequeños _huevos de pascua_ muy curiosos, como lo que hace este pequeño fragmento del código del mensaje _whois_ del módulo IRC de Gaim:

```c
if (!strcmp(irc->whois.nick, "Paco-Paco")) {
    g_string_append_printf(info, _("<br><b>Defining adjective:</b> Glorious<br>"));
}
```

Lo que hace este pedazo de código es que cada vez que se hace un _whois_ al usuario Paco-Paco (Ethan Blanton), le colocaa al final del mensaje “Defining adjective: Glorious”. Algo más curioso aún es que es una cadena traducible, por lo tanto, los traductores lo han traducido sin darse cuenta. Aquí hay un pantallazo de un whois a Paco-Paco:

![Image 2: Pantallazo-Gaim](/images/modificando-gaim/gaim.png)
