+++
title = "Dolor de cabeza con Python"
date = 2007-05-31
+++

Un problema de usar lenguajes dinámicos es que, al no tener etapa de compilación, no es posible detectar muchos de los errores sino hasta que se lanza alguna excepción mientras el programa se ejecuta. Un problema peor es cuando por alguna razón el error no produce una excepción y el programa termina funcionando erróneamente si dar ninguna pista sobre dónde puede estar el problema.

Examinen este pedazo de código en Python:

```cpy
class MyClass:
    pass

if MyClass() < 1:
    do_something()
else:
    do_something_else()
```

o algo más curioso todavía:

```cpy
if MyClass() < float('-infinity'):
    do_something()
```

siempre se ejecuta.

Lo correcto debería ser que al hacer este tipo de comparaciones se lanzara una excepción. La única forma de poderlo hacer debería se cuando sea explícito que el objeto puede compararse.

Noten que este código si lanza una excepción del tipo `TypeError`:

```cpy
a = MyClass() + 1
```

Según lo que me dijeron en _#python_, parece ser que todos los objetos en Python están habilitados para hacer comparaciones. Esta es la razón por la cual se pueden ordenar fácilmente listas con cualquier tipo de datos en ellas. Debido a que arreglar esto supondría un corte con la compatibilidad hacia atrás, sólo podremos disfrutar de una adecuado comportamiento hasta que tengamos Python 3.0. Si esto hubiera estado listo ahora mismo me habría ahorrado un gran dolor de cabeza buscando un error.
