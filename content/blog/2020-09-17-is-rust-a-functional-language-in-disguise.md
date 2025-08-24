+++
title = "Is Rust a Functional Language in Disguise?"
date = 2020-09-17
+++

This is something I’ve been asking myself while learning Rust. Yes, I know that this sounds like a weird question to ask as it’s no secret that Rust has huge influence from the functional programming world. Closures, iterators, pattern matching, algebraic data types; these are features inspired by FP languages, so obviously you can do functional programming with Rust. But that’s not really my question. What I’m asking is if Rust is a **mainly** functional language.

These days most mainstream imperative languages have functional features, you can do FP in any of them, but that doesn’t mean that those languages are considered functional. On the other hand, some languages are designed mainly to be functional, I’m talking about Haskell, Clojure, OCaml or Erlang. So, to be more clear, I can rephrase my question as: Is Rust a language designed to be used mainly for functional programming? Or is it another imperative language where you can optionally use FP?

At first glance, it looks like the answer is simple. Rust very much looks like an imperative language with support for some popular features from functional languages. But after a closer look at the language, I’ve come to realize that it is closer to a purely functional language than I thought. It is **a functional language disguised as imperative**. I will try to explain what I mean in this post.

## What is functional programming?

Before explaining why I think that Rust is mainly a functional language, it is a good idea to first explain what functional programming is. This is not as easy as it sounds, so first a disclaimer: This is far from a formal definition, but rather a hand-wavy explanation of what I understand as FP.

*Side note: I am making this disclaimer because in the past I’ve experienced some quite angry responses from FP enthusiasts about this point of view. That made me quit FP for a while until I found the very friendly Clojure community. And I’m happy to report that in my first steps with Rust so far I have met an equally friendly community.*

The core ideas behind Functional Programming are immutability and lack of side effects. That’s it. If you mostly use pure functions that receive data and return data without mutating any sort of external state, then you’re doing FP. On the other hand, if you mostly call functions or methods that alter or mutate some external state, then you are doing imperative programming.

To avoid side effects, functional languages use immutable data structures. Let’s jump to some small code examples to illustrate this difference. I know these examples are a bit silly and there are other ways to write them, but I just want a simple code example to illustrate my point. Here is how you use a hash map (dictionary) in Python, which is a mainly imperative language:

```cpy
film = {}
film["title"] = "Fargo"
film["director"] = "Joel Coen"
```

And here is how you use a hash map in Clojure, a mainly functional language:

```clj
(let [film1 {}
      film2 (assoc film1 "title" "Fargo")
      film3 (assoc film2 "director" "Joel Coen")])
```

The main difference between these two approaches is that in Python you create one map, then you mutate it to add some entries to it. In Clojure you can’t mutate the map, instead, what you can do is to create a new map based on the previous one.

Now, let’s check how the same thing looks in Rust:

```rust
let mut film = HashMap::new();
film.insert("title", "fargo");
film.insert("director", "Joel Coen");
```

The Rust example is much closer to the imperative Python than the functional Clojure. And just in case there is any doubt, we have the **mut** keyword right there, which means **mutable**.

*Side note: Unlike some other languages that also have keywords to distinguish mutable and immutable values (**final** in java, **const** in JavaScript, **readonly** in C#, **val** in Kotlin), one interesting thing about Rust is that this applies to the whole value, not just the superficial reference. In Java, nothing prevents you from mutating a HashMap in a final reference. Rust won’t allow any sort of mutation unless you use **mut** (I’m going to conveniently ignore Interior Mutability for now, mostly because I think I don’t fully understand it yet).*

So after looking at the code examples, we can conclude that Rust is mainly an imperative language. Or is it? I know that this sounds very counter intuitive, but I think that the Rust example is actually closer to the functional style than the imperative one. Yes, I’ll explain why at some point, please be patient.

## If a tree falls in the woods, does it make a sound?

Here is the thing, pure Functional Programming is an illusion, it’s not real. Even the purest of the FP languages are mutating things and producing some side effects behind the scenes. Real computers are imperative machines. Your pure functions have to change registries, push stack frames, etc. So we can say that FP languages are merely an emulation, they are not  the real thing. This doesn’t mean that FP doesn’t have any value, I actually think there is a lot of value in it. Especially in the fact that FP produces programs that are easier to understand and to maintain. But it’s important to understand that purity is unachievable.

Let’s take another look at my previous Clojure code example:

```clj
(let [film1 {}
      film2 (assoc film1 "title" "Fargo")
      film3 (assoc film2 "director" "Joel Coen")])
```

Here Clojure doesn’t really create entirely new data structures on every operation. That would be very inefficient. Instead, Clojure internally uses something called [Hash Array Mapped Tries (HAMT)](http://lampwww.epfl.ch/papers/idealhashtrees.pdf). When you use **assoc** in Clojure to add an entry to a map, it looks like it’s generating a completely new map, but in reality, both maps share most of the same internal structure, they are really one single HAMT, and **assoc** is actually mutating that HAMT.

So data structures in Clojure are actually mutable, but that doesn’t really matter because their interface is side effect free for the external world. Clojure is still a mainly functional language. And that’s a key aspect of FP; it’s not about completely avoiding mutation, that is impossible in real computers, it’s about hiding those mutations in a way that they don’t create side effects for the rest of the code. In FP we want our units of computation (functions) to depend only on their inputs and not on some external state. That’s what makes them easier to reason about.

Now back to our small Python example:

```cpy
film["title"] = "Fargo"
film["director"] = "Joel Coen"
```

The key difference here, compared to the Clojure example, is that the world is not shielded from this mutation. We could have some class or other part of the code holding a reference to this map, and as soon as we mutate this we are creating a side effect for those parts of the code. This makes code harder to reason about. It’s the same reason why global variables are considered a bad practice, and it’s also the reason why many programmers prefer to use FP.

Let’s go back to the Rust example. This time I added a reference to the map, which will be the observer of the mutation side effect:

```rust
let mut film = HashMap::new();
let observer = &film;
film.insert("title", "fargo");
film.insert("director", "Joel Coen");
println!("{}", observer.len());
```

If you are a Rust programmer you of course know that **this code won’t compile**. Here is what the awesome Rust compiler says about it:

```
error[E0502]: cannot borrow `film` as mutable because it is also borrowed as immutable
 --> src/main.rs:6:5
  |
5 |     let observer = &film;
  |                    ----- immutable borrow occurs here
6 |     film.insert("title", "fargo");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ mutable borrow occurs here
7 |     film.insert("director", "Joel Coen");
8 |     println!("{}", observer.len());
  |                    -------- immutable borrow later used here
```

This error happens because Rust’s ownership and borrowing rules only allow either one single mutable reference or many immutable ones. In other words, **if you are going to mutate an object in Rust, you can’t have any other part of the code holding a reference to that object**. This is mostly checked statically by the compiler. So mutation in Rust is like a tree falling in the forest where there is no one to hear it. It’s a mutation that doesn’t produce side effects. And this is exactly what FP is about.

## The struggles of learning a language

Rust has not been as easy to learn for me as other languages. The borrow checker, which is the part that verifies the mutability and lifetime of references, is famous among Rust beginners as the toughest part to get used to.

While struggling with the borrow checker I started to notice something: the kinds of patterns that caused me trouble with the borrow checker are very similar to the ones that caused me trouble when learning functional programming. For example, when I was learning Clojure by solving some [Advent of Code](https://adventofcode.com/) problems, I got to a problem where the best solution was to use a circularly linked list. I was trying to solve the problems using pure FP and I quickly hit a wall. Later on, when I needed a similar data structure in Rust I also hit a wall. This kind of data structures are hard to implement both in pure FP and in Rust.

*Side note: There is a fantastic tutorial called [Learning Rust with Entirely Too Many Linked Lists](https://rust-unofficial.github.io/too-many-lists/), by Alexis Beingessner. It’s a great resource for learning to deal with the borrow checker in a practical way. This has been a lifesaver!*

The similarity in the struggles is what made me think that perhaps Rust is way more functional than it appears to be and that approaching Rust in an imperative way is only a sure path to borrow checker headaches. But this is hard to realize because Rust does look very imperative, so your intuition is to use it in that way.

There is one huge positive aspect of this imperative appearance though: It’s much easier to reason about performance. Once you pass the borrow checker, your code just looks very similar to some imperative C. This contrasts with the deep abstractions that you often find in functional languages (e.g. HAMTs, lazy sequences) where unless you are well versed in the internals, it’s hard to predict how a given piece of code will perform.

## Verdict

Back to the beginning, is Rust a mainly functional language? Well, I don’t know. The borrow checker certainly makes it very different from traditional imperative languages. But there is more to FP than mutation side effects. *IO* is another common cause of side effects. Printing to the screen, writing a file, sending a network request. The more pure functional languages like Haskell take these into account, but others like Clojure ignore them, letting you create these side effects from any function without ceremony. And so does Rust, so I wouldn’t rule it out of the FP category.

Functional composition is another key aspect of FP. There is **map**, **filter** and **fold** in Rust, but functional composition doesn’t seem to be as idiomatic as in FP languages. Recursion is also not very idiomatic in Rust. This is mostly because you actually have **mut**, so you can have imperative loops, whereas in FP languages you can’t mutate local variables so recursion is your only choice. At the smaller scale, Rust is definitely imperative. But I personally think that FP doesn’t bring any advantage at the small scale. It’s at the big scale when avoiding side effects really pays off. That’s the big advantage that FP brings to the table, and that one is covered by Rust’s borrowing rules.

So the verdict is not definitive. I can’t fully say that Rust is a functional language. But one thing that I’m sure of is that Rust is one of the most interesting languages that I have learned so far. The ownership and borrowing system is an amazing innovation that goes way beyond allowing memory safety without garbage collection. This system is actually bringing the best of the functional and imperative worlds together. And I’m very much looking forward to using and learning more about Rust.

### Update:

 - [Discussion on Reddit](https://www.reddit.com/r/rust/comments/iur9ly/is_rust_a_functional_language_in_disguise/)
