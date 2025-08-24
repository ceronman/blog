+++
title = "Python vs C#: Queries"
date = 2008-08-14
+++

One of the most beloved C# 3.0 features is Linq. Linq brings great power to C#, it allows you to easily write structured queries over collections or remote data sources. Now with C# is possible to make queries as easy as with other languages like Python. I decided to compare the way you make queries with C# and with Python. I found a great page showing 101 Linq examples, I decided to write Python versions of this examples. Which version do you like more?

[Where – Simple 1](http://msdn.microsoft.com/en-us/vcsharp/aa336760#WhereSimple1)

C# version:

```cs
int[] numbers = { 5, 4, 1, 3, 9, 8, 6, 7, 2, 0 };
var lowNums = from n in numbers where n < 5 select n;
```

Python version:

```cpy
numbers = [5, 4, 1, 3, 9, 8, 6, 7, 2, 0]
low_nums = (n for n in numbers if n < 5)
```

[Where – Indexed](http://msdn.microsoft.com/en-us/vcsharp/aa336760#WhereIndexed)

C# version:

```cs
string[] digits = { "zero", "one", "two", "three", "four",
                    "five", "six", "seven", "eight", "nine" };
var shortDigits = digits.Where((digit, index) => digit.Length < index);
```

Python version:

```cpy
digits = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']
short_digits = (digit for index, digit in enumerate(digits) if len(digit) < index)
```

[Select – Simple 1](http://msdn.microsoft.com/en-us/vcsharp/aa336758#SelectSimple1)

C# version:

```cs
var numsPlusOne = from n in numbers select n + 1;
```

Python version:


```cpy
nums_plus_one = (n + 1 for n in numbers)
```

[Select – Anonymous Types 1](http://msdn.microsoft.com/en-us/vcsharp/aa336758#SelectAnonymousTypes1)

C# version:

```cs
string[] words = { "aPPLE", "BlUeBeRrY", "cHeRry" };

var upperLowerWords =
    from w in words
    select new {Upper = w.ToUpper(), Lower = w.ToLower()};
```

Python version:

The exact Python version would be something like:

```cpy
words = ['aPPLE', 'BlUeBeRrY', 'cHeRry']

upper_lower_words = ( type('', (), {'upper': w.upper(), 'lower': w.upper() })
                      for w in words)
```

But I feel more Pythonic this:

```cpy
upper_lower_words = ( (w.lower(), w.upper()) for w in words)
```

Or even this:

```cpy
upper_lower_words = ( {'upper': w.upper(), 'lower': w.upper() }
                      for w in words)
```

[SelectMany – Compound from 1](http://msdn.microsoft.com/en-us/vcsharp/aa336758#SelectManyCompoundfrom1)

C# version:

```cs
int[] numbersA = { 0, 2, 4, 5, 6, 8, 9 };
int[] numbersB = { 1, 3, 5, 7, 8 };

var pairs =
    from a in numbersA,
         b in numbersB
    where a < b
    select new {a, b};
```

Python version:

```cpy
numbersA = [0, 2, 4, 5, 6, 8, 9]
numbersB = [1, 3, 5, 7, 8 ]

pairs = ( (a, b) for a in numbersA
                 for b in numbersB
                 if a < b)
```

[SelectMany – from Assignment](http://msdn.microsoft.com/en-us/vcsharp/aa336758.aspx#SelectManyfromAssignment)

C# version:

```cs
var orders = from c in customers,
                  o in c.Orders,
                  total = o.Total
             where total >= 2000.0M
             select new {c.CustomerID, o.OrderID, total};
```

Python version:

I couldn’t find how to make the assignment in Python, so the version is:

```cpy
orders = ( {'customer_id': c.customer_id,
            'order_id': o.order_id,
            'total': o.total }
           for c in customers
           for o in c.orders
           if o.total > 2000)
```

[SelectMany – Multiple from](http://msdn.microsoft.com/en-us/vcsharp/aa336758#SelectManyMultiplefrom)

C# version:

```cs
var orders = from c in customers
             where c.Region == "WA"
             from o in c.Orders
             where o.OrderDate >= cutoffDate
             select new {c.CustomerID, o.OrderID};
```

Python version:

```cpy
orders = ( (c.customer_id, o.order_id)
           for c in customers if c.region == 'WA'
           for o in c.orders if o.date >= cutoff_date)
```

[Take Simple](http://msdn.microsoft.com/en-us/vcsharp/aa336757#TakeSimple)

C# version:

```cs
var first3Numbers = numbers.Take(3);
```

Python version:

if we are working with something like a list, we could do:

```cpy
first_3_numbers = numbers[:3]
```

but, if we are working with iterators, we must do:

```cpy
first_3_numbers = itertools.islice(numbers, None, 3)
```

[Skip – Simple](http://msdn.microsoft.com/en-us/vcsharp/aa336757#SkipSimple)

C# version:

```cs
var allButFirst4Numbers = numbers.Skip(4);
```

Python version:

```cpy
all_but_fist_4_numbers = numbers[4:]                         # list version
all_but_fist_4_numbers = itertools.islice(numbers, 4, None)  # iterator version
```

[TakeWhile – Simple](http://msdn.microsoft.com/en-us/vcsharp/aa336757#TakeWhileSimple)

C# version:

```cs
var firstNumbersLessThan6 = numbers.TakeWhile(n => n < 6);
```

Python version:

```cpy
fist_numbers_less_that_6 = itertools.takewhile(lambda x: x < 6, numbers)
```

[SkipWhile – Simple](http://msdn.microsoft.com/en-us/vcsharp/aa336757#SkipWhileSimple)

C# version:

```cs
var allButFirst3Numbers = numbers.SkipWhile(n => n % 3 != 0);
```

Python version:

```cpy
all_but_first_3_numbers = itertools.dropwhile(lambda x: x % 3 != 0, numbers)
```

[First & Last](http://msdn.microsoft.com/en-us/vcsharp/aa336750#FirstSimple)

C# version:

```cs
numbers.First()
numbers.Last()
```

Python version:

```cpy
numbers[0]         # first for a list_numbers[-1] _# last for a list
numbers.next()     # first for iterator_list(numbers)[0] _# first for iterator
list(numbers)[-1]  # last for iterator
```

[First – Indexed](http://msdn.microsoft.com/en-us/vcsharp/aa336750#FirstIndexed)

C# version:

```cs
int evenNum = numbers.First((num, index) => (num % 2 == 0) && (index % 2 == 0));
```

Python version:

```cpy
even_num = [n **for** i, n **in** enumerate(numbers) **if** n%2 == 0 **and** i%2 == 0][0]
```

or:

```cpy
even_num = (n **for** i, n **in** enumerate(numbers) **if** n%2 == 0 **and** i%2 == 0).next()
```

to be continued…
