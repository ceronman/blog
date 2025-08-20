+++
title = "Optimizing a Python Program"
date = 2009-03-08
+++

These days, I’ve been optimizing a Python program I wrote. Optimizing is a fun task, but very difficult. Most of the time, the first solution I think is even worse than the previous situation. I need more experience.

Some processes were too slow in my program and I realized it was because I was performing too much disk I/O operations. I thought a solution could be read more data in memory and operate there. Now I have excessive memory consumption.

Here is a very simplified description of my memory consumption problem:

I have a text file. Each line in the file represents an item of a large list. Each line has two string values separated by a character. Something like a CSV file. I have to read the file content and put it in a list.

A line in the file looks like this:

```
Content of the first value|Content of the second value
```

The separator is `|`

Here is a simple Python program that reads the file:

```cpy
class Field:
    def __init__(self, line):
        self.value1, self.value2 = line.split('|')

fields = []

with open('test_data') as file_:
    for line in file_:
        fields.append(Field(line))
```

Running this program with a test file of about 42 MB gives this results:

```
Execution time (time): 0m4.108s
Memory consumed (pmap): 166652K
```

I was surprised by the high memory usage of the program. If the file is 42MiB, I thought the program should use a similar amount of memory, obviously a higher amount, but not almost four times the size of the file.

An equivalent program in C (error checking is omitted):

```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define VALUE1_MAX 30
#define VALUE2_MAX 80
#define LINE_SIZE VALUE1_MAX + VALUE2_MAX + 3
#define BUFFER 10000

typedef struct
{
    char value1[VALUE1_MAX+1];
    char value2[VALUE2_MAX+1];
} field;

int main()
{
    FILE *file = fopen("test_data", "r");

    field *fields = (field*) malloc(BUFFER*sizeof(field));
    char line[LINE_SIZE];
    char *part;
    long i=0;
    long size = BUFFER;
    while(fgets(line, LINE_SIZE, file) != NULL) {
        part = strtok(line, "|");
        strcpy(fields[i].value1, part);
        part = strtok(NULL, "|");
        strcpy(fields[i].value2, part);

        i++;
        if (i == size) {
            size += BUFFER;
            fields = (field*) realloc(fields, size*sizeof(field));
        }
    }
    fclose(file);
    free(fields);
    return 0;
}
```

Results for the C program:

```
Execution time (time): 0m0.537s
Memory consumed (pmap): 57548K
```

This is much better.

The problem with the Python program seems to be the `Field` objects using more memory than they need. Testing the program without the `Field` creations, changing `fields.append(Field(line))` with `fields.append(line)` seems to perform better:

```
Execution time (time): 0m0.575s
Memory consumed (pmap): 66808K
```

Clearly, the `Field` object is the bottleneck both in memory consumption and execution time. This is probably because of some default memory allocations that Python makes for the object and its fields. Python is a really cool language, but it doesn’t let you control the way the memory is used. This is a positive thing in most of the cases, but in some of them, like this one, is negative.

Most of the times, there are only very small parts of a program that really need to be optimized. And a programmer is much more productive with Python than with C. It doesn’t make sense to rewrite the program in C. Instead, a C module could be written for the bottlenecks.

I was too lazy to learn how to use the Python C API, so I looked a this project called [Cython](http://www.cython.org/). Cython is a language designed for writing Python extensions. It’s very similar to Python, but is translated to C and compiled to an easy to use Python module. Cython also lets you mix C code and Python code easily. It lets you use high level python objects or low level C data types as you need and mix them properly.

I decided to rewrite the `Field` class in Cython:

```
#field.pyx
DEF VALUE1_MAX = 30
DEF VALUE2_MAX = 80

cdef extern from "string.h":
    char *strcpy(char *dest, char *src)

cdef class Field:
    cdef readonly char value1[VALUE1_MAX+1]
    cdef readonly char value2[VALUE2_MAX+1]
    def __init__(self, line):
        v1, v2 = line.split('|')
        strcpy(self.value1, v1)
        strcpy(self.value2, v2)
```

This extension type can be used almost in the same way than a real Python object:

```
>>> f = Field('Hello|World')
>>> f.value1
'Hello'
>>> f.value2
'World'
>>>
```

I had to modify the original Python script to use the new module:

```cpy
from field import Field

fields = []

with open('test_data') as file_:
    for line in file_:
        fields.append(Field(line))
```

Results of the new program:

```
Execution time (time): 0m1.257s
Memory consumed (pmap): 69800K
```

This is a huge improvement. With a very small change, the program now consumes almost 100MB less memory and it runs three times faster. I could write more parts in Cython, using strtok()instead of str.split(), or even rewriting the entire list and reading process. I would probable get a performance very similar to the C program. But I’m comfortable with the results now. I’m still surprised with the small effort compared to the awesome results.

If you want to do your own tests. Here is a simple script to generate a test file with 500k values:

```cpy
import string
import random

with open('test_data', 'w') as f:
    for i in range(500000):
        value1 = ''.join(random.choice(string.letters)
                         for s in range(random.randint(15, 30)))
        value2 = ''.join(random.choice(string.letters)
                         for s in range(random.randint(50, 80)))
        f.write(value1 + '|' + value2 + '\n')
```
