Title: Ctrlp.vim - A Comprehensive File Finder for VIM
Published: 07-12-2012
Tags: VIM

> Look for the file by the name ???, the file must be in the directory ???, the file starts (or ends)  with ???

These thoughts constantly passes one's mind or are uttered by colleagues while
editing code, fixing bugs or during pair programming sessions. These operations
have to be performed multiple times (many times a minute) and to be productive
the IDE in use has to be able to perform them fast and cover all the above
requirements.

<more/>

Initially I used NERDTree, it is an excellent file/directory explorer. You
could browser through the directories, open, delete, copy, move files or
directories. Further frequently visited directories can be bookmarked. However
in situations like the above it fails miserably.

A few months back I came across Command-T. Command-T is a good file finder. It
was fast however I could not use regex in search input, also its reliant on
Ruby was a hassle.

A few weeks back, I began to look for an alternative. There were few
alternatives such as Lusty Explorer, Fuzzy Finder etc... Ctrlp caught my
attention. Used it for a day at home and the last few days I have been using at
work and am quite impressed with it.

When compared to the alternatives mentioned above,
[Ctrlp](http://kien.github.com/ctrlp.vim/) seems to be the most
comprehensive file finder vim plugin. Why? (I hear you ask)

###File or Path Search
While searching for a file one either remembers the name of the file or the
path of the file. In Ctrlp you can specify whether you are searching for a file
and it scans the file name index or alternatively a path can be specified. It
autocompletes path names.

###Regex in Search
Most of the times we don't remember the entire file name or the path. Regex
comes to the rescure here. It supports vim regex syntax.

###Searching for files in Buffer or MRU List
VIM users use buffers instead of opening a large number of tabs. Search can be
performed within the buffer. Further it maintains a list of mostly recently
used files and searches can be performed within the MRU list as well.

I find the above three features as the most essentials ones and this plugin
does it in a robust manner. However, in addition to the above it offers a few
extra which sweetens the deal:

###Multiple File Selection
During a search you could select multiple files and open them in either in
split (horizontal or vertical) windows or tabs. Further after selecting
mutliple files you could type ":diffthis" in the prompt and view a diff of all
the selected files.

###Create and delete files
Yeah, you heard me right ;).

###Using yanked text in search
The yanked text can be pasted in the search prompt.

A noticeable issue with this tools is that the first time Ctrlp buffer is
opened depending on the number of files in the project it could take a while
to initialize. I have not investigated the cause of it, but I guess it
performs some sort of indexing or refreshes the existing index.

Now head-over to the official [site](http://kien.github.com/ctrlp.vim/) and try
it out.

Happy coding :)
