## petgen.py
Generates species and attributes descriptions for fictional animals. Can be repurposed for any other randomizer which uses lists to generate results.

### Requirements
  - [Python 2.7](https://www.python.org/downloads/release/python-2710/)
  - [pip](https://pypi.org/project/pip/) 

### Basic setup
Download all included files. 

Open petgen.py in a text editor and update lines 16, 21, 26, 31 with the path to the .txt files.

To test run the generator, check out my upload on [replit](https://repl.it/@vuhlkantra/petgen).

### More info
This generator functions much the same way as the weather generator does. I've nerfed the datasets significantly for the github upload — the generator becomes more and more fun as you add more data.

You'll see that I've been very particular about the grammar in the concatenated string on line 40 of the petgen.py file. That's so the characteristics in special.txt can be varied and wild without having to be forced into a restrictive grammatical syntax.

If you look very closely, you might also notice how some of the text files have trailing whitespace on each line. This is because I am a fool and a masochist and hate dealing with whitespace in concatenated string formulas.
