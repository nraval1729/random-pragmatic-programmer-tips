Just read The Pragmatic Programmer: From Journeyman to Master? Read it a long time ago?
Need inspiration from the "tips" given in the book?

Look no further! I built this set of simple scripts to help engineers stay motivated and mindful of the best software engineering
advice that exists. 

The Pragmatic Programmer: From Journeyman to Master is, IMHO the best software engineering book ever. I have just started reading it, and
I absolutely love the little tips mentioned in the book. I feel like it would be more productive if one could regularly read these tips.
Since you would have already read the book, just reading the tips would refresh your memory and remind you of the key concepts as presented
in the book. Enjoy!

Glossary

pragmatic_tips.txt --> A text file containing all the tips + their short descriptions. Courtesy of the pragmatic programmer website.

pickle_tips.py --> This script stores all the tips and their corresponding descriptions in a dict. Then pickles it.

pragmatic_tips.p --> This is the pickled file.

tip_gen.py --> This script accepts a command line arg: the absolute path to the above pickled file. Then it unpickles it, and randomly prints out
a tip alongwith its description. Run it like python tip_gen.py /path/to/pragmatic_tips.p

I put the tip_gen.py in my bashrc file (along with the absolute path to the .p file, so that everytime you start a new terminal instance, you get a tip + description. You are welcome!
