+++
title = "A powerful unused feature of Python: function annotations"
date = 2013-03-12
+++

Something I’ve always missed when using Python (and dynamically typed languages in general) is nice tooling support. C# and Java have powerful IDEs that can improve your productivity significantly. Some people say that [IDEs are a language smell](http://www.recursivity.com/blog/2012/10/28/ides-are-a-language-smell/). I disagree, IDEs are a truly valuable tool and the “nice language or IDE” statement is a [false dilemma](http://en.wikipedia.org/wiki/False_dilemma).

The problem with dynamically typed languages is that it’s impossible for the IDE to infer things about some parts of your code. For example, if you start typing this:

```cpy
def myfunction(a, b):
  ...
```

It’s impossible for the editor to give you any hint about `a` or `b`.

I’ve been playing with [Dart](http://www.dartlang.org/) and [TypeScript](http://www.typescriptlang.org/) recently. These are languages that compile to Javascript and both try to improve tooling support. They’re interesting because, despite being dynamically typed languages, both implement optional type annotations. These have no different purpose than aiding editors and IDEs. Let me show you a simple example of how this can be seriously useful, consider the following Javascript code:

```js
function findTitle(title) {
    var titleElement = document.getElementById('title-' + title);
    return title;
}

var t = findTitle('mytitle');
t.innerHTML = 'New title';
```

The code has a small error that is not very easy to notice. Now let’s see the [TypeScript Web Editor](http://www.typescriptlang.org/Playground) with the same code adding a single type annotation to `findTitle`:

![Image 1: typescript](/images/a-powerful-unused-feature-of-python-function-annotations/typescript3.png)]

TypeScript found an error. By knowing that `title` is a `string`, it knows that `findTitle` is returning a `string` too, and therefore `t` is a `string` and strings don’t have an `innerHTML` method.

Early error detection is one advantage of good tooling support. Another interesting thing is accurate code completion. With good code completion you don’t have to browse huge API docs looking for what you need. You can discover the API while you type and use automatic re-factor tools without worrying about breaking code.

![Image 2: typescript-small](/images/a-powerful-unused-feature-of-python-function-annotations/typescript-small.gif)

Anders Hejlsberg’s [introduction video](http://channel9.msdn.com/posts/Anders-Hejlsberg-Introducing-TypeScript) to TypeScript contains more interesting details about how annotations are really useful.

While playing with TypeScript I couldn’t stop thinking how cool would be to have something like that in Python. Then I realized that Python had syntax for annotations years before TypeScript or Dart were even planned. [PEP 3107](http://www.python.org/dev/peps/pep-3107/)introduced function annotations in Python. Here is a small example:

```cpy
def greet(name: str, age: int) -> str:
    print('Hello {0}, you are {1} years old'.format(name, age))
```

Here I annotated the `greet` function with the types of each argument and return value. Python annotations are completely optional and if you don’t do anything with them, they’re just ignored. However, with some little magic, it’s possible to tell python to check types at run-time:

```
>>> @typechecked
... def greet(name: str, age: int) -> str:
...     print('Hello {0}, you are {1} years old'.format(name, age))
...
>>> greet(1, 28)
Traceback (most recent call last):
    ...
TypeError: Incorrect type for "name"
```

Run-time type checking is not very useful though. However, a static analyzer could use that information to report errors as soon as you type. Also, IDEs and code completion libraries such as [Jedi](https://github.com/davidhalter/jedi) could use that information to provide nice completion tips just like TypeScript does.

Some people might say that this makes the language too verbose. People using dynamic languages often want concise code. But in practice, if you take a look at any medium to large Python project or library, chances are that you’ll find something like this:

```cpy
def attach_volume(self, volume_id, instance_id, device):
    """
    Attach an EBS volume to an EC2 instance.

    :type volume_id: str
    :param volume_id: The ID of the EBS volume to be attached.

    :type instance_id: str
    :param instance_id: The ID of the EC2 instance to which it will
                        be attached.

    :type device: str
    :param device: The device on the instance through which the
                   volume will be exposted (e.g. /dev/sdh)

    :rtype: bool
    :return: True if successful
    """
    params = {'InstanceId': instance_id,
              'VolumeId': volume_id,
              'Device': device}
    return self.get_status('AttachVolume', params, verb='POST')
```

I took this code from the [boto library](https://github.com/boto/boto), they annotate functions using docstrings and [sphinx](http://sphinx-doc.org/). It’s a very common way of annotating public APIs. However, this method has some drawbacks: first, it’s really verbose and you repeat your self a lot writing code like this; second, it’s harder to parse because there are different docstring formats (sphinx, epydoc, pydoctor), so editors don’t bring code completion or early error checking; third, it’s very easy to make mistakes that unsync the docstrings and the code. In this particular example, if you ever run this function, you’ll notice that it returns a string, not a bool as the annotation suggests.

[Google Closure](https://developers.google.com/closure/) uses a similar docstring approach for type annotations in Javascript.

So, if people are already writing verbose docstrings to annotate functions, why not just use real function annotations? They’re completely optional and you don’t have to use them for non-public APIs or small scripts. They’re more concise, easier to process and easier to verify. Function annotations are only available on Python 3, you might say, but there are [some](https://pypi.python.org/pypi/annotate/0.2.4)[approaches](https://pypi.python.org/pypi/anodi/0.0.2) to emulate them in Python 2.x using decorators and it’s still way better than docstrings.

An interesting thing about Python annotations is that they don’t have to be types. In fact, you can use any Python expression as a function annotation. This opens the possibilities for a lot of interesting applications: typechecking, auto documentation, language bridges, object mappers, adaptation, design by contract, etc.

The [typelanguage](https://github.com/kennknowles/python-typelanguage) library defines a whole language for communicating types. This language can be used with just string annotations. For example:

```cpy
def get_keys(a_dict: '{str: int}') -> '[str]':
    ...
```

The downside of this flexibility is that it causes some confusion in the community about how annotations should be used. A recent [discussion](http://mail.python.org/pipermail/python-ideas/2012-December/018088.html) in the Python-ideas mailing list unveiled this problem.

Personally, I would love to see this feature more used in the Python community. It has a lot of potential. I started a [small library to work with type annotations](https://github.com/ceronman/typeannotations). It implements the `typechecked` decorator described before, and some other useful things like structural interfaces, unions and logic predicates that can be used as function annotations. It’s still very immature, but I would like to improve it in the future by adding function overloading and other features. A detailed description of the library probably deserves a whole post for it. I would love to hack Jedi to add some basic support for auto-completion based on annotations.
