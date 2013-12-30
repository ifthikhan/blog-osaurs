Title: The Python Object Model By Alex Martelli
Published: 06-10-2012
Tags: Python, Video

http://youtu.be/VOzvpHoYQoo

A great presentation by Alex Martelli where he describes python's object model
in detail. The talk is divided into 4 major parts:

<more/>

1. Package State and Behaviour
2. Delegation
3. Polymorphism
4. Instantiation

The most interesting part from my perspective was delegation, he describes the
attribute look-up process in detail. He spends a fair amount time detailing on
descriptors; it's semantics, functions are descriptors and the creation and
usage of custom descriptors.

He also talks about the concept of "Hold vs Wrap". Hold an object as an
instance of another and expose it as a part of the API and the evils of this
practice. The merits of the idea of wrapping an external object's calls within
the current object and avoiding the boilerplate code via __getattr__.

Under polymorphism he talks about functors and lexical closures and when to
choose what.

The last part of the talk is about instantiation in OOP. He speaks about
monostate and proposesit as a replacement for the singleton pattern.
