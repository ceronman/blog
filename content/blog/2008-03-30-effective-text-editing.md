+++
title = "Effective Text Editing"
date = 2008-03-30
+++

I saw the video [7 Habits For Effective Text Editing 2.0](https://www.youtube.com/watch?v=p6K4iIMlouI) that arhuaco [recommended](http://wiki.freaks-unidos.net/weblogs/arhuaco/poder-de-computo-humano) months ago. I was tempted to start learning Vim, but after thinking for a while, I came to the conclusion that there is no good reason for learning Vim. I still don’t get why people likes Vim that much. Most of the features that Bram Mooleenar showed in the video have been present in other tools for years and, in my humble opinion, they work much better than in Vim. Other things Bram talked about are just too crazy for me (He suggested that word processing would be more productive if we edit every paragraph in Vim and then copy-paste it on Microsoft Word… WTF!!)

Here are my habits for effective text editing:

Golden Rule: Use the best tool for the Job. I have learned that using a generic text editor for everything leads to be very unproductive. I like to use JEdit as my generic Text Editor. I love it for things like XML, C/C++, this weblog, etc. It has all the advanced features I need in a text editor. I used to use it for C# and Python but I discovered that using an specialized IDE for these languages is thousands of times more productive. Now I use MonoDevelop for C# and PyDev for Python.

The most important features I need when editing source code that can be hardly founded in a generic text editor are:

*   **Good** Code Completion. Note the "Good" word is remarked. Some generic text editors have support for code completion but most of the time is very, very poor. For C#, MonoDevelop is the open source tool with the best code completion out there (ok, maybe #develop has good code completion too). For Python it’s a bit more difficult due the dynamic nature of the language. I have tested many editors and IDEs and I think PyDev has the best code completion (I’ve heard that Wing IDE has good support too). Code completion is specially useful when you’re working with large libraries like GTK+.

*   Refactoring Operations. Rename, go to definition, go to parent definition, encapsulate, look for references, etc. They are essential features, it’s impossible to be effective without them.

*   Integrated Debugger. This one is missing from MonoDevelop. Hopefully will be there for the next release. It’s lovely how with a simple click you can create a break point in your code, run it, and it will stop right there, then you can easily watch every object state and even add some code (on dynamic languages).

*   Version Control Integration. Automatic add, remove, rename subversion files. Easily track the changes on the files. I love the ChangeLog integration of MonoDevelop. Eclipse has a good support for Subversion too.

*   Integrated UI Editors. It saves a lot of time if you’re writing GUI applications.

*   Task list. If you put notes on your source code comments such as: TODO, FIXME, NOTE, HACK, etc. It will generate a list with all notes present on all files, so you can look for pending things easily. This feature is present in MonoDevelop, PyDev and JEdit. I love it.

*   Integrated Help. Put the cursor on a word, hit F1 and automatically open the help browser with the page for the class or method description for the object or definition you selected.

There are other cool features that I like and most of the time are present in a good generic text editor:

*   Code folding.

*   Easy comment, uncomment of lines.

*   Advanced search and replace

*   Diff viewers. JEdit has a Diff plug in, but I prefer [Meld](http://meld.sourceforge.net/).

*   Splits. Actually I have not seen a tool with a split support as good as JEdit.
