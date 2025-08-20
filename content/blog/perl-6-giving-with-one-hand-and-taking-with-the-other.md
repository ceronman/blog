+++
title = "Perl 6: Giving with One Hand and Taking with the Other"
date = 2015-02-23
+++

Perl 6: Giving with One Hand and Taking with the Other
------------------------------------------------------

I’ve been programming Perl full-time for almost two years now. The reason is my new job, where 99% of back-end our code base is Perl. Before that, I had not written a single line of Perl, so the language has been a new experience for me. I think Perl is actually better than its reputation. It is pleasant to write most of the time. I also love to see and understand how many cool features in other languages were inspired by Perl. Nevertheless, it’s undeniable that the language has pitfalls and design problems. This year, during FOSDEM, Larry Wall [announced](https://fosdem.org/2015/schedule/event/get_ready_to_party/) that a first version of Perl 6 will be released before Christmas. For those not familiar with Perl, please notice that it’s not exactly the successor of Perl 5, but it’s rather a completely new and different language. Perl and Perl 6 are called sister languages. The idea of Perl 6 started fifteen years ago, when Larry Wall and others decided to design and implement a new language from scratch. The idea was to keep Perl’s essence, while fixing all of its design issues and quirks. I decided to give Perl 6 a try. Mostly because I was curious to see if it actually fixed the problems of Perl 5. I haven’t started a serious project or anything, I’ve been just playing with the language and solving some [Project Euler](https://projecteuler.net/) problems. Also, I’ve started my tests with a pre-release version of Perl 6 (Rakudo Star with MoarVM version 2015.01), some things are not implemented and some others are not properly documented. If any Perl 6 dev ever reads this, please forgive me if something is wrong. I’ll be happy to be corrected. Both Perl 5 and Perl 6 languages are pretty big. The motto of these languages is “There is more than one way to do it” ([TIMTOWTDI](http://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it)). So there are tons of features, many of them just to do the same things. I will only discuss a few of them. In particular, I will discuss how Perl 6 addresses those that I consider the biggest problems of Perl 5: context and references.

First Big Problem: Context Variable Behavior
--------------------------------------------

Context is something very unique to Perl as far as I know. It’s a way to mimic spoken language where the meaning of some words depends on the context they’re used in. Perl 5 has 3 contexts: scalar, list and void. So for example, a function might do and return something completely different depending on the context of the call:

```pl
my $x = do_something(); # Scalar context: returns one thing.
print do_something();   # List context: might return other thing.
do_something();         # Void context: a third possibility.
```

When implementing a function, you can use the special _wantarray_ construct to know in which context the function is being called. For example:

```pl
sub do_something {
  if (wantarray) {
    # this will run if called in List context
  } elsif (defined wantarray) {
    # this will run if called in Scalar context
  } else {
    # this will run if called in Void context
  }
}
```

The reason I consider context one of the biggest problems of Perl 5 is because, unlike other bad “features”, it’s pretty much impossible to avoid. The concept is so fundamental to the language and its core libraries that you just have to learn to live with it. It’s important to be very careful of how you are calling your functions all the time, otherwise you might introduce bugs or even [security issues](http://blog.gerv.net/2014/10/new-class-of-vulnerability-in-perl-web-applications/). Unfortunatelly, there doesn’t seem to be a convention on what functions should return in each context. For example, the built-in function _keys_ return the list keys of a hash table / dictionary when called in list context, but instead returns then number of keys if called in scalar context. However, the _splice_ function removes elements from an array and returns them in list context but it only returns the last element in scalar context. Similarly, the regexp match operator returns a Boolean if the string matches in scalar context, but the matching groups in list context (only if groups were defined). And so on. All this makes Perl hard to learn because you have to read and memorize the documentation of all the functions, and their behaviors on different contexts. Things are rarely intuitive and I’ve seen developers with many years of Perl experience bitten by this from time to time.

Second Big Problem: References
------------------------------

The other big problem with Perl, in my opinion, are references. More specifically, array and hash references. To explain why these are a problem, first I have to describe Lists. Lists are a language construct in Perl that can be used to initialize data structures, passing arguments to functions or assigning variables. A list is basically a group of expressions separated by commas. For example:

```pl
my @array = (1, 2, 3);       # Initialize an array.
my ($one, $two) = (1, 2);    # Assign variables.
join('/', 'home', 'manuel'); # Arguments to a function.
```

One important thing about lists is that they flatten all the inner lists. For example, the following lines are equivalent:

```pl
my @array = (1, 2, 3, 4);
my @array = (1, (2, (3, 4)));
```

The flattening also happens if you use arrays as expressions, for example:

```pl
my @end = (3, 4);
my @array = (1, 2, @end); # same as (1, 2, 3, 4);
```

List flattening is actually a nice feature, it allows a lot of cool things such as destructuring of assignment and function arguments. However, it has a problem: it makes it difficult to create nested data structures such as arrays of arrays. To fix this, Perl introduced the concept of references. References are some sort of high level pointers. Instead of storing the actual data, references store a pseudo address which points to the data. The important aspect of references, in relation to the problem described above, is that they’re scalars, and as such they can be taken as a single element of an array. So you can’t have arrays of arrays in Perl because of the flattening feature, but you can have arrays of array references, which are a good substitute. For example:

```pl
my @a = (1, 2);
my @b = (3, 4);
my @parts = (\@a, \@b); # Two elements. Doesn't flatten.
```

Perl also provides a nice syntax for defining array references, so the code above could be better written as:

```pl
my @parts = ([1, 2], [3, 4]); # an array of two arrayrefs.
```

Or you can write it as a single array reference and the syntax is very similar to other programming languages:

```pl
my $arrayref = [ [1, 2], [3, 4] ];
```

A similar thing happens with hashes/dictionaries, which are constructed also with lists. To have nested hashes you have to use hash references. The problem with array references is that they behave completely differently in both list and scalar contexts. So every time you want to do something with them you have to know if you’re dealing with a real array or a reference. Just like context, this problem is unavoidable in Perl because you need references every time you need nested arrays, but you can’t use only references because most built-in functions to operate with collections accept real arrays instead. To illustrate this problem, let’s assume that you’re using an API with a get_employees() function, and you want to print the name of each one. Your code is different depending on whether the function returns an array or an arrayref:

```pl
# Array version:
my @employees = get_employes();
for my $employee (@employees) {
  print $employee->name;
}

# Arrayref version:
my $employees = get_employes();
for my $employee (@{$employees}) {
  print $employee->name;
}
```

So for every function returning a collection, you have to read the documentation and memorize if they return a reference or an array. Some libraries help you with this, for example, DBI (the database interface for Perl) adds a suffix to some functions indicating which kind of value they return:

```pl
@row = $sth->fetchrow_array();
$row = $sth->fetchrow_arrayref();
```

Other libraries make use of the _wantarray_ special function to return an array when in list context or a reference when in scalar context. This sometimes helps, but it also creates even more confusion because it’s not a widespread idiom, so you have to check the documentation carefully anyway. To make things worse, Perl built-in functions usually work in a way that’s completely counterintuitive for people used to all this lists/array logic. For example, the _push_ function can be used to add one or more elements to an array:

```pl
my @array = (1, 2, 3);
push(@array, 4, 5, 6); # will be (1, 2, 3, 4, 5, 6)
```

This looks perfectly fine, however, if you were paying attention at how lists work in Perl, you know that arguments passed to a function are lists, and lists flatten. So applying the flattening logic to the _push_ function, these two lines should be equivalent:

```pl
push(@array, 4, 5, 6);
push(1, 2, 3, 4, 5, 6);
```

So how does Perl know when the array part of the arguments ends and the elements part starts? If you use the list/array logic, to make this work, the first element should be a reference. That way, you will know that the array to push into is the first element of the list. You’d use it like this:

```pl
push(\@array, 4, 5, 6);
```

But that’s not how the built-in _push_ function works in Perl. So, how does it work? A very experienced Perl developer once told me that in general, I should not assume that built-in functions behave as regular functions, some times they use some magic. However, there is a feature that explains this: function prototypes. These are small specs added to each function specifying what each argument is. It allows you to override the flattening logic. For example, if you want to have a function that behaves like push, you have to use:

```pl
sub my_push(\@@) {
  my ($array, @elements) = @_;
  push @$array, @elements;
}
```

One more thing to look for when reading API documentation. Fortunately, it’s not common that libraries abuse this feature.

Perl 6 to the Rescue?
---------------------

Let’s finally talk about Perl 6. Good news is that it addresses these issues. Although Perl 6 still has a concept of context, it’s completely different from what Perl 5 uses. In practical terms this means that there is no _wantarray_ function (yay!). Instead context flows outwards. That means that functions just return objects that know how to behave in different scenarios using methods for it. For example, if you want to represent an object as a string, you implement an _Str_ method. If you want it as a number, you implement a _Numeric_ method and so on. That’s not much different from what other languages do, it’s a well known pattern. Perl 6 also drops references. Everything is an object now. In fact you can assign arrays to scalar variables and use them almost in the same way as regular arrays:

```pl
$./perl6
> my @array = 1, 2, 3, 4;
1 2 3 4
> @array.elems # returns the number of elements in the array.
4
> @array[0] # element access
1
> @array[0] = 10 # assigning an element
10
> say @array;
10 2 3 4
>
> # scalars work in the same way:
> my $scalar = @array;
10 2 3 4
> $scalar.elems
4
> $scalar[0]
10
> $scalar[0] = 1
1
> say $scalar
1 2 3 4
```

So, if arrays behave like objects, and you can assign them to scalar variables and use them in the same way, why does Perl 6 still use sigils (the symbol before the variable name) to differentiate arrays from scalars? The answer is that, unfortunately, we still have context in Perl 6. And we still have flattening lists, and everything is mixed in a very confusing cocktail. Let’s start with the context part. A list, just as in Perl 5, it’s a series of items separated by commas. When assigning a list to something, the value will be different depending on the context:

```pl
my @array = 1, 2, 3; # list context assigns all the items
my $array = 1, 2, 3; # item context: assigns only the first item
```

List also flatten, so these two arrays are the same:

```pl
my @array1 = 1, 2, 3, 4;   # four elements
my @array2 = 1, 2, (3, 4); # also four elements
```

Because there are no references in Perl 6, if you want to have nested arrays, you have to explicitly ask for item context:

```pl
my @array2 = 1, 2, $(3, 4); # three elements
my @array2 = 1, 2, [3, 4];  # brackets also work. TIMTOWTDI
```

So far, sounds reasonable. But there is one problem: in addition to Lists, Perl 6 introduces another construct called [parcels](http://doc.perl6.org/type/Parcel), which stands for _Parenthesis Cells_. Just as lists, they can have elements separated by commas, but they behave differently: while Lists flatten, Parcels don’t. The fact that both constructs are dangerously similar, creates a lot of confusion.

```pl
my $a = 1, 2, 3, 4;       # $a is a single integer = 1.
my $b = (1, 2, 3, 4);     # $b is a parcel with 4 elements
my $c = ((1, 2), (3, 4)); # $c is a parcel with 2 elements

my @a = 1, 2, 3, 4;       # @a is an array with four elements
my @a = (1, 2, 3, 4);     # @b is also an array with 4 elements
my @a = ((1, 2), (3, 4)); # @c is also an array with 4 elements
```

How does Perl 6 know if a list of things surrounding by parenthesis and delimited by commas are lists or parcels? It depends of the context, in this case the sigil of the variable being assigned. Note that in the case of scalar context, the parenthesis surrounding the expression are fundamental to determine if the value assigned is a parcel or just the first element of the list. You might think the key to recognize parcels are the parenthesis, after all, they’re called _Parenthesis Cells_ for a reason. But this is not the case. First, in list context parenthesis are pretty much ignored. And even in scalar context, some things can be parcels even if they don’t have parenthesis. For example the value returned by a function:

```pl
sub my_function { 1, 2, 3 }
my $a = my_function(); # $a is a parcel with three elements.
```

Sometimes it’s harder to determine if a list or a parcel is going to be used, because you don’t have a sigil to determine it. For example, when you do something like this:

```pl
((1, 2), (3, 4))[0] # returns 1 2
```

In this case Perl 6 assumes it’s a parcel, hence the items are not flattened. Same thing seems to happen when trying to call methods:

```pl
((1, 2), (3, 4)).elems # returns 2
```

However, sometimes it seems to take the value as a list:

```pl
((1, 2), (3, 4)).map({ say $_ }) # flattens and print four lines.
```

I don’t know how this is possible at all, since parcels don’t even have a _map_ method. And I haven’t figured out how could Perl 6 interpret this as a list. I suspect this is either a bug or an exception hard coded in Rakudo (there are a few of those). Do you think that’s all? Of course not. Perl 6 has a third construct for comma separated items: [Captures](http://doc.perl6.org/type/Capture). These are used for function arguments. The rules for flattening Captures are variable, they depend on a [Signature](http://doc.perl6.org/type/Signature) object associated with it. Each case is unique. I’m not going to describe how Captures work, they’re really complex. You can read the [documentation](http://design.perl6.org/S06.html) if you’re curious.

Conclusion
----------

Perl 6 is definitely an improvement over Perl 5 in many areas. It would require many posts to describe all the nice fixes in design. However, my feeling is that while some issues have been fixed, new quirks have been introduced. Of course, Perl 6 has not been released yet and some of these things might change. Also, I have not tried all the features to have a solid opinion on it. I think I’ll take a look again in a year when version 6.0.0 is out there.

### Update:

Thanks to [Reddit](http://www.reddit.com/r/perl6/comments/2x10fq/perl_6_giving_with_one_hand_and_taking_with_the/), I just found out that most of the issues mentioned here about Perl 6 are going to be fixed. More specifically, the flattening of lists and the elimination of parcels. This is called The [Great List Refactor](http://pmthium.com/2014/10/apw2014/) and it’s supposed to be there before the final release of the language.
