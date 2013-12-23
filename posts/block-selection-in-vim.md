Title: Block selection in VIM
Published: 15-08-2011
Tags: Vim

I have been wanting to try out VIM for a while and a few months back I decided
to abandon Netbeans and use VIM for all my editing needs.

The initial days were challenging but once I got used to the modes and
internalized some of the shortcuts and commands it started getting fun. Now I
use VIM full-time and it's been a joyful experience so far, hands down!

One of the features that has impressed me from the outset is the block
selection. You can select a column of text vertically and delete or substitue
them. I knew on how to delete the selected column but did not figure out on how
to substitute the selection.

[:more:]

![Block selection](/static/bffd5-screenshot-scaled1000.png)

Typically I would highlight the column, delete them and record a macro for the
first line and repeat the macro on the rest of the lines, or better yet I would
perform a search and replace operation. None of these options are efficient.

Today I bumped across
[this article](http://mohtasham.info/article/block-selecting-killer-feature-vim/)
which explains on how to simultaneously edit
the entire column. Select the block by pressing Ctrl+v in normal mode.
Thereafter press s to substitue, the entire selection will vanish. Pressing s
would automatically alters the mode to Insert, and the cursor will be
positioned at the start of the selection. Enter the new text in the first line
and press ESC. Watch the magic unfold... After a short pause you would see that
the newly entered text in the first line has been magically replicated in the
rest of the lines below. Such is the power and beauty of VIM.

Strangely the replication occurs only if you perform an operation in the insert
mode and then switch to normal mode. Sadly yanking does not work.

Hey, stranger if you have never used VIM, I urge you to give it a try or if you
are newbie learning VIM persist and you shall be enlightened ;).
