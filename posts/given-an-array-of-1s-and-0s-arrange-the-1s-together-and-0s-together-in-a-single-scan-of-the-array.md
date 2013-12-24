Title: Given an array of 1s and 0s arrange the 1s together and 0s together in a single scan of the array
Published: 04-05-2011
Tags: Algorithms, Interview questions, Programming, Python

if you google for common interview questions for pogrammers you are most likely
to encounter this one. I first encountered this question at
[http://www.techinterviews.com/basic-programming-questions](http://www.techinterviews.com/basic-programming-questions).
The complete question is:

> Given an array of 1s and 0s arrange the 1s together and 0s together in a single scan of the array. Optimize the boundary conditions.
<more/>

I attempted to solve the problem using python.

My first attempt was to maintain another list and while iterating the original
one. Whenever I come across a "1", its index is recorded and proceed with the
iteration. As soon as a "0" is encountered the positions of the current element
(i.e 0) will be replaced with previously encountered "1". With a single scan
the the top indexes would contain zeroes where as the lower order would contain
ones.

    ls = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    print(ls)
    i, last_encountered = 0, []
    for item in ls:
        if item == 1:
            last_encountered.append(i)
        elif last_encountered:
            ls[last_encountered.pop(0)] = 0
            ls[i] = 1
            last_encountered.append(i)
        i += 1
    print(ls)

Although this solution works, it's inefficient as the list to track the
position of "1"'s would result in increased memory usage.

Further research revealed that a solution could be implemented using the
partition operation of [quick sort](http://en.wikipedia.org/wiki/Quicksort).

Quick sort picks an index position called the "pivot" and on the first run
orders the elements less than the one found in the pivot to its left and the
ones greater than the pivot to its right. This operation is known as the
partition operation. Since our data consists of only "1"'s and "0"'s we can
sort the entire list in the first run.

    ls = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    print(ls)
    pivot, i = 0, 1
    while i < len(ls):
        if ls[pivot] > ls[i]:
            ls[pivot] = 0
            ls[i] = 1
            pivot += 1
        i += 1
    print(ls)

The second solution uses less lines of code in comparison to the first and does
not use extra memory. It's elegant, simple and robust.

Hope anyone searching a solution to this question would find this post useful.

Happy coding :)
