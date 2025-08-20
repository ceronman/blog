+++
title = "Super Mario Bros"
date = 2010-12-04
+++

Hace unas semanas se celebró el aniversario 25 de Super Mario Bros. Hace unos días, alguien preguntó en StackExchange en qué lenguaje de programación estaba escrito. En Reddit surgieron [varios comentarios interesantes](http://www.reddit.com/r/programming/comments/effi0/what_programming_language_was_super_mario_bros/):


> Hi, I am a NES programmer! It is actually not that hard if you grok manual memory management. The 6502 instruction set is simple (but not at all orthogonal) and the NES has a lot of
>
>  hardware registers that do Interesting Things for you. The only serious limitation in my mind is the extremely limited color capabilities of the PPU, the NES’s equivalent of a GPU.

> NES in a nutshell: you have 2Kb of onboard RAM. There’s an 8Kb window where your cartridge can patch more in. It can even bankswitch to have different sets of 8Kb. You have a 32Kb program
>
>  ROM window and that too can be bankswitched, usually in 8 or 16Kb sections. Graphics have an 8Kb window, two pages of 256 8×8 tiles. The remaining space in the 64Kb memory is various
>
>  hardware registers where you do your IO and configuring the graphics and sound generators. There is only one timer available, the TV refresh signal. On an NTSC NES it will raise an
>
>  interrupt 60 times a second, and on a PAL one, 50.

El CPU 6502 corría a sólo 1.79Mhz. Las limitaciones técnicas eran grandes. Aún así, Super Mario Bros no fue el mejor juego logrado para el NES. El mejor, en mi opinión, fue tal vez Super Mario Bros 3, una verdadera joya.

![Image 1: smb3](/images/super-mario-bros/smb3.jpg)

Creo que programar con limitaciones es más divertido, aunque no más productivo. En ese sentimiento se inspiran concursos como [Java 4k](http://www.java4k.com/) o [Sizehack](http://trent.gamblin.ca/sizehack/). De vez en cuando es bueno programar por diversión, y sólo por diversión.

Por aquí está un clon de Super Mario Bros escrito en Javascript y HTML:

[http://jsmario.com.ar/](http://jsmario.com.ar/)

Me pregunto cuales serán sus requerimientos mínimos.
