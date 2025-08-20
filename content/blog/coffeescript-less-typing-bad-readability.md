+++
title = "CoffeeScript: less typing, bad readability"
date = 2012-09-17
+++

I’ve used CoffeeScript for a few months now. Coming from Python, I felt that CoffeeScript was more concise than Javascript, so I decided to use it for a few small projects. Initially, it was a nice experience, but then I gradually realized that, while writing CoffeeScript code was very pleasant, reading it wasn’t so. I started to notice that it was hard to read my own code a few months later. It was even harder to read other people’s code. I often found my self reading the translated JavaScript code to understand a line or two of CoffeeScript. I concluded that CoffeeScript was a language designed for writability at the cost of readability, easier to write, but harder to read.

The roots of CoffeeScript readability problems are two principles applied to the design of the language:

*   _Implicit is better than explicit_
*   _There is more than one way to do it_

## 1. Implicit is better than explicit.

Implicit or optional tokens in a programming language usually bring readability problems. For example, in C-like languages, you can omit curly brackets after a conditional expression if you only have one statement:

```c
if (condition)
    action();
```

But what happens if we add a new statement:

```c
if (condition)
    action();
    action2();
```

Now let’s take a look at a classic problem associated with implicit semicolon insertion in Javascript:

```js
function foo() {
  return
    {
      foo: 1
    }
}
```

Both examples show cases where, at first glance, the code looks like it’s doing something, but after looking more carefully it’s doing something completely different. Even if you know the rules, it’s easy to fall into this trap if you’re an unwary reader. That’s a readability problem.

CoffeeScript introduces multiple implicit or optional tokens that create a lot of situations like these ones. And that’s something you can easily see in real code. For example, take this statement:

```js
action(true, {
   option1: 1,
   option2: 2
})
```

In CoffeeScript, you can omit the **parenthesis**, the **curly brackets** and the **commas**. They’re optional. So you can rewrite the statement above as this:

```js
action true
   option1: 1
   option2: 2
```

### Problems with optional parenthesis

Take a look at these two snippets. Next to the CoffeeScript code is the resulting JavaScript:


```js
// CoffeeScript                          JavaScript
doSomething () ->  'hello'               doSomething(function() {
                                             return 'hello';
                                         });
```

```js
// CoffeeScript                          JavaScript
doSomething() ->  'hello'                doSomething()(function() {
                                             return 'hello';
                                         });
```

Both statements do completely different different things, although they look very similar. The first one takes the space after the function name and applies implicit parenthesis to the function call, taking the function as a single parameter. The second one interprets the parenthesis as a function call with no arguments and applies implicit parenthesis on that result. Note that in CoffeeScript parenthesis are also optional in function definitions with no arguments. That means that the following two statements have exactly the same meaning:

```js
x = -> 'result'
x = () -> 'result'
```

Something curious about the rules used by CoffeeScript for implicit parenthesis is that the case for function calling is exactly the opposite of the case for function definition. In function calling you can omit parenthesis except when the function takes no arguments, whereas in function definition you can omit parenthesis only when the function has no arguments.

Now let’s take a look at some interesting case of how implicit parenthesis make things harder to read. This a small snippet taken directly from the CoffeeScript source code:

```js
action = (token, i) ->
      @tokens.splice i, 0, @generate 'CALL_END', ')', token[2]
```

The `@tokens.splice` function call has five elements separated by commas. At first glance you can think that the function is taking five arguments, but if you read carefully, you will notice that there is another function call as an argument: `@generate`. The last two arguments are for `@generate` not for `@token.splice`. A more readable way of writing this would have been:

```js
action = (token, i) ->
      @tokens.splice i, 0, @generate('CALL_END', ')', token[2])
```

### Problems with optional commas

In CoffeeScript you can omit commas for separating function arguments if you put them in a new line. For example the following two statements are equivalent:

```js
moveTo 10, 20, 10
moveTo 10,
  20
  10
```

The comma after the first argument is mandatory, except if the next argument is an object definition:

```js
moveTo(10, {key: value})

moveTo 10
  key: value
```

Also, if you’re not using explicit parenthesis, indentation is important, but not alignment, take a look at these examples with the resulting JavaScript next to them:

```js
// CoffeeScript                          JavaScript
doSomething 1,                           doSomething(1, 2, 3, 4);
  2
  3
  4


doSomething 1,                           doSomething(1, 2);
2                                        3;
3                                        4;
4


doSomething 1,                           doSomething(1, 2, 3, 4);
  2
    3
   4
```

You’re not safe from indentation problems if you use parenthesis, for example:

```js
// CoffeeScript                          JavaScript
doSomething (->                          doSomething((function() {}, 'hello'), 1);
'hello'), 1


doSomething (->                          doSomething((function() {
  'hello'), 1                                return 'hello';
                                         }), 1);
```



In the first case, the line break after the function definition is replaced by an implicit comma, the parenthesis seem to be ignored.

### Problems with optional curly brackets

Suppose that you have a function that takes two objects as arguments:

```js
action({key: value}, {option: value}, otherValue)
```

If you omit the curly brackets, you might think you get the same result:

```js
action(key: value, option: value, otherValue)
```

However, in this case CoffeeScript will take the first comma as a separator for object properties instead of a separator for arguments. The second comma however, it is taken as argument separator because it’s not an explicit key-value pair. The code will be translated to the following Javascript:

```js
action({key: value, option: value}, otherValue);
```

Something curious here is that in CoffeeScript, explicit key-value pairs are optional in object definitions, but only if you use explicit curly brackets. That means that you can write something like this:

```js
// CoffeeScript                          JavaScript
x = {                                    x = {
  key1                                       key1: key1,
  key2                                       key2: key2,
  key3: value3                               key3: value3
}                                        };
```

## 2. There is more than one way to do it (TIMTOWTDI)

In CoffeeScript TIMTOWTDI is a strong principle. For example, instead of just having `true` and `false` keywords for boolean values, you can also have `yes` and `no`, `on` and `off`.

Also, you can write a simple conditional statement in multiple ways:

```perl
x = 1 if y != 0

if y != 0
  x = 1

x = 1 unless y == 0

unless y == 0
  x = 1
```

All the four statements above do exactly the same thing.

The problem with having multiple ways of doing one thing, is that the language end up with too many idioms. This makes code harder to read because a programmer trying to understand a piece of code must be familiar with all those idioms.

When we combine multiple idioms with implicit stuff and the fact that everything is an expression, the result is a bomb for readability. Here are a few examples taken directly from CoffeeScript’s source code.

### Fancy for loop

```perl
  break for [tag], i in @tokens when tag isnt 'TERMINATOR'
  @tokens.splice 0, i if i
```

This code deletes leading newlines from the list of tokens. The `for` loop is

 just a _cool_ one liner to write this:

```perl
  for [tag], i in @tokens
    if tag is 'TERMINATOR'
      break
```

### Tricky while

```rb
i += block.call this, token, i, tokens while token = tokens[i]
```

In CoffeeScript everything is an expression. In the code above, is the `while` expresion an argument of `block.call`? or is it acting as `while` for the whole statement? When we translate it to Javascript, this is what we get:


```js
while (token = tokens[i]) {
  i += block.call(this, token, i, tokens);
}
```

Much easier to read in my opinion. Also, note that the while expression is using an assignment operator instead of a comparision one. That adds 10 points to the readability bomb.

### Tricky if

```perl
@detectEnd i + 1, condition, action if token[0] is 'CALL_START'
```

Here is a similar example, but this time, we’re using an `if` statement. As in the previous example, the `if` here is acting over the whole statement:

```js
if (token[0] === 'CALL_START') {
  this.detectEnd(i + 1, condition, action);
}
```

But what happens if we add an `else` to the `if`?

```perl
@detectEnd i + 1, condition, action if token[0] is 'CALL_START' else false
```

Now the `if` is assumed as an expression argument for the `@detectEnd` function:

```js
this.detectEnd(i + 1, condition, action(token[0] === 'CALL_START' ? void 0 : false));
```

### Fancy redefinition

```js
mainModule.moduleCache and= {}
```

This code clears the module cache only if the value is not null (or something falsy). This could have been writen this way:

```js
if mainModule.moduleCache
  moduleCache = {}
```

But short and original code is much cooler. This is a good example of how TIMTOWTDI kills readability.

### Nested made flat

```js
js = (parser.parse lexer.tokenize code).compile options
```

In this example we see how a nested chain of calls looks flat thanks to the magic of implicit parenthesis. The code translates to the following Javascript:

```js
js = (parser.parse(lexer.tokenize(code))).compile(options);
```

When the nested calls are explicit, the code becomes easier to read.

## Conclusion

Of course readability is a very subjective topic. The problems described here might not apply to you if you come from a different background. I come from Python, C# and C++. But if you come from Ruby or Perl, you might think these are not problems but actually cool features.

I think that readability is more important than writability for a programming language. Code is usually written once, but read many times. Given that CoffeeScript doesn’t fix any of the fundamental problems of JavaScript, but damages readability, I decided not to use it anymore.

Update:
-------

Another interesting post with some other readability problems in CoffeeScript:[http://ryanflorence.com/2011/case-against-coffeescript/](http://ryanflorence.com/2011/case-against-coffeescript/)
