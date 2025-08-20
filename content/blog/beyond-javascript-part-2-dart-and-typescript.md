+++
title = "Beyond Javascript part 2: Dart and Typescript"
date = 2012-10-08
+++

I was glad to see the release of Microsoft TypeScript last week. After Google with Dart, it’s nice to see one more big player trying to create new languages for client side web development.

I’ve been playing with Dart for a while and TypeScript really impressed me. In terms of syntax, I feel that TS got some bits much better than Dart. Anders Hejlsberg has a true talent for language design. Some things I like about TypeScript:

*   Full interoperability with the JavaScript world. This is both ways: from JS to TS and vice-versa. There is a huge ecosystem of code available for JS.
*   Better syntax. For example: type annotations are much more flexible, and they look nicer. Interfaces are better too, they cover all the cases and there is no need for ugly constructs such as “typedef” in Dart.
*   They offer support for private things, both in classes and modules. Although, this is only useful at compile time.
*   The web playground is really cool. It has auto completion, error highlighting and side by side compilation. It even has nice key bindings, almost like a good IDE.
*   The Visual Studio support and the online playground showed an amazing type inference engine. I have not seen that with Dart.
*   The module system looks better, it’s possible to explicitly importonly the things you need from a module. I like that.

As a side note, I really like they way Microsoft is approaching open source with this project. They have open sourced a lot of things in the past, but this time it feels different. They used an Apache license, added a node.js package, Chrome and MongoDB were used in the demo. It shows a MS less afraid of interoperating with competing open source products and more interesting in truly participating in the community process.

Dart, on the other side, is a more ambitious project in my opinion. Although many of the cool promised features are not really there yet. For example: mirrors and tree shaking.

There are some things that I think Dart got better than TypeScript:

*   It really fixes all the insanity of JavaScript: it has sane equality operators, real arrays, real hash maps, sane comparisons, sane scope, lexical “this” and many more things. TypeScript doesn’t fix any of these problems.
*   More features: operator overloading, string formatting, for-in loops, better collections, isolates, annotations, generics.
*   It improves the DOM interface. This is one of my favorite features.
*   Multiplatform IDE. Visual Studio is cool, but I don’t want to use Windows.

Dart also provides a new VM. This is interesting because it allows optimizations based on type inference, direct debugging and other cool things. However, I think it’s very unlikely that other browsers ever implement the Dart VM. Dart2js will be the only option for a long time.

Another thing I like about Dart is how fast the project moves. Almost every week you see language changes and improvements for the IDE. I wonder if TypeScript is going to be as dynamic.

I’m currently working on a small personal project written in Dart. I would like to play with TypeScript but I don’t want to use Visual Studio. I think some traction is needed before support for other IDEs and editors appears. I guess I have to wait.
