+++
title = "Summer of Code: Lunar Eclipse Final Report"
date = 2008-09-05
+++

I had a lot of fun participating in the Google Summer of Code. As I said before, I worked improving Lunar Eclipse, an open source visual designer for Silverlight/Moonlight. This is what I achieved during the summer:

**Tools & Handle Support**:

I worked on editing support for the following Silverlight Elements:

Circle, Ellipse, Rectangle and Square: These are the basic boxed shapes. Previous version of Lunar Eclipse already had support for this elements. Anyway I almost refactored the entire Handle & Tool subsystem. This helped me to adapt it to more complex shapes like bezier paths.

Line and PolyLine: Simple two point line and multiple point line.

Bezier Path and Pen Tool: I worked on two tools for creating Path figures. One let you create a path using Bezier Segments. This is working fine but there are a couple of bugs regarding translations of points. I also implemented a Pen tool for creating paths based on manual movement, it’s working, but it needs to be optimized to produce less nodes.

TextBox: I have partial TextBox support. I couldn’t implement graphical text editing because the Entry control is not yet implemented in Moonlight.

I also tried to add Image support. But it was impossible to use the Downloader and set media to objects using the GtkSilver widget (used for creating Desktop Moonlight applications).

![Image 1: le-screenshot1](/images/lunar-eclipse/le-screenshot1.png)

![Image 2: le-screenshot2](/images/lunar-eclipse/le-screenshot2.png)

**Other features**

Selection Rect – Select All – Clear Selection – Delete Selection: I improved the selection rectangle and all the selection subsystem. This was important in order to implement other operations such as ordering and alignment. The use of keys for selection (like control to add to selection) is not working because the Keyboard class was not implemented in Moonlight at the time.

Property Panel: The properties panel was fixed. I believe that in the future, Lunar Eclipse will use the toolbox system of MonoDevelop, but some of the internal parts of this work, such as property introspection, can be reused in the future.

Infinite Undo Redo: Undo and Redo was implemented in previous versions of Lunar Eclipse, anyway, I fixed a lot of bugs related with this and implemented Undo – Redo support for all tools and operations.

File Open / Save: As simple as that. Files can now be saved and loaded 🙂

Zooming and Scrolling: Zooming is now possible. There are some ugly effects caused by the GtkSilver implementation. I guess this will be fixed in the future. Scrolling is working good but it needs improvements to be more usable.

Ordering and Alignment: Send to Front, Send Backwards, Align Right, etc.

Serialization and Back: Serialization has been fixed. Loading from XAML is working too so you can move back and forth between Xaml and Design. Serialization still need a lot of love. Output is too verbose and the text indentation structure is not ‘remembered’ by the serlializator. I want something similar to the MS Expression Blend’s system, which is awesome.

Copy – Paste – Clone: Clipboard operations. Copy was a bit difficult because Silverlight elements don’t have a clone method. I Implemented my own Clone method based on the serialization work.

New interface: This wasn’t a critical feature, but I rewrote the GTK# based user interface. This was an easy task thanks to the awesome MonoDevelop.

**Video Demo:**

Here is a demo video showing some of the features of Lunar Eclipse:

<video width="640" height="480" controls>
  <source src="/images/lunar-eclipse/le-video.mp4" type="video/mp4">
</video>

**Future**

It was really difficult to work on Lunar Eclipse the last weeks of the Summer of Code. Moonlight hackers started to work heavily on the 2.0 version. Moonlight became very unstable and its API changed a lot, (besides Silverlight 2 Beta 2 API changed too). All these changes broke Lunar Eclipse. The last objective, animation support, was not completed. Anyway, I definitely want to keep working on this project. I decided to freeze Lunar Eclipse while Moonlight gets more stable, but I started to work on adding support for Silverlight projects to MonoDevelop. After that, I want to fix bugs in LE and start isolating the design surface to be easily plugged in applications such as MonoDevelop or a Web Based Lunar Eclipse.
