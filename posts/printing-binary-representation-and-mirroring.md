Title: Creating a mirror of a given bit pattern
Published: 25-05-2012
Tags: Alogrithms, Python

Weird ideas tend to creep into ones mind when the GRUNT WORK at work seems
infinite.

A while back I was reading the [Computer Science A Programmers Perspective
- CSAPP](http://www.amazon.com/Computer-Systems-A-Programmers-Perspective/dp/013034074X)
book and came across an exercise for mirroring the bit representation
for a given integer.

<more/>

Here goes my solution for it

    def mirror(input):
        mirror = 0
        for _ in range(sys.getsizeof(input)):
            mirror = (mirror << 1) | (input & 0x1)
            input = input >> 1
        return mirror

On a high level the the above algorithm achieve its task by copying bit by bit
the input from right on each iteration and places it on the left of a new
variable.

###The devil is in the details:

1. (input & 0x1): Copy the least significant bit from the input.

2. (mirrored << 1): Left shift the bits in the mirror variable by 1 position to
the left. This will have no effect on the first iteration as the mirror
variable is set to 0. However from the second iteration onwards this operation
will move the previously copied bit 1 position to the left moving it towords
it's final destination.

3. OR (|): This operation copies the bit extracted from first operation to the
least signification position of the mirror variable.

Performing the above steps for each bit will result in a mirror represantation
of the input.

In addition to integers, characters can be passed as well by obtaining their
respective ascii value.

Happy hacking... :)
