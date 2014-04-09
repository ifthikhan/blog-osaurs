Title: Counting Sort
Published: 08-04-2014
Tags: Algorithms
Visibility: public

Lately I have been reading [Steve Skiena's](http://en.wikipedia.org/wiki/Steven_Skiena)
[The Algorithm
DesignManual](http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1848000693).
The chapter on Sorting and Searching has a few use cases of [Counting Sort](http://en.wikipedia.org/wiki/Counting_sort) and wanted to impart a quick tip to detect when it's screaming at the top of it's voice to be used :).

###Detect!

> We seek to sort a sequence S of n integers with many duplications, such that the number of distinct integers in S is O(logn). Give an O(nloglogn) worst-case time algorithm to sort such sequences.

> Assume that the array A[1..n] only has numbers from \{1,\ldots, n^2\} but that at most loglogn of these numbers ever appear. Devise an algorithm that sorts A in substantially less than O(nlogn).

Both the questions above indicate that there are multiple duplicates either directly or indirectly.

###Solution
In such cases it's efficient to sort by iterating through the entire collection
and recording each distinct value as a key in a dictionary and the number of
occurences as its value. Once the iteration is complete the original list can
be overwritten by replicating each key corresponding to the recorded value.

A self balancing binary tree can be used instead of a dictionary which will
allow to fetch the values in sorted order thus eliminating the step of sorting
the keys when using a dictionary.

Happy hacking :)
