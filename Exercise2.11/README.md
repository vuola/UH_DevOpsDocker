QUICK START:

This is a server version of a Markov algorithm generating "nonesense" literature by mashing together content from Dickens, Shakespeare and Hemingway novels.

Build and run the server with commands

	$> cd markov
	$> docker-compose up

and connect to the service with your browser at address:

	http://localhost:5000

Each browser refresh will create a fresh sample text. Enjoy the absurd literature !

DEVELOPER'S NOTES

The code of this algorithm is created with python and served by a python library web server from the "flask" package. Markov algorithm resides in file "markov_server.py" and the server code in "server.py".

A handy feature is automated re-booting of the service triggered by saving of code changes. This is achieved by mounting the folder of localhost into the container and sharing one codebase while the container is running. 

FULL DESCRIPTION OF THE ALGORITHM:

If you choose words from the book at random, you can get a sense of the vocabulary, but you probably won’t get a sentence:

    this the small regard harriet which knightley's it most things

A series of random words seldom makes sense because there is no relationship between successive words. For example, in a real sentence you would expect 
an article like “the” to be followed by an adjective or a noun, and probably not a verb or adverb.

One way to measure these kinds of relationships is Markov analysis, which characterizes, for a given sequence of words, the probability of the words 
that might come next. For example, the song Eric, the Half a Bee begins:

	Half a bee, philosophically, 
	Must, ipso facto, half not be. 
	But half the bee has got to be 
	Vis a vis, its entity. D’you see?

	But can a bee be said to be
	Or not to be an entire bee 
	When half the bee is not a bee 
	Due to some ancient injury?

In this text, the phrase “half the” is always followed by the word “bee”, but the phrase “the bee” might be followed by either “has” or “is”.

The result of Markov analysis is a mapping from each prefix (like “half the” and “the bee”) to all possible suffixes (like “has” and “is”).

Given this mapping, you can generate a random text by starting with any prefix and choosing at random from the possible suffixes. Next, you can 
combine the end of the prefix and the new suffix to form the next prefix, and repeat.

For example, if you start with the prefix “Half a”, then the next word has to be “bee”, because the prefix only appears once in the text. The next 
prefix is “a bee”, so the next suffix might be “philosophically”, “be” or “due”.

The program "markov.py" reads text from three literature sample files by Dickens, Shakespeare and Hemingway, and generates a mash-up story. 

First we create a dictionary that maps each prefix with a collection of possible suffix words.

The analysis is followed by generation of a random story with completed sentences. Each sentence ends when an ending character
(. ? !) is discovered to be the next suffix. Therefore, different random sentences can have very different word counts.

CALL SYNTAX FROM A SHELL PROMPT

	> python3 markov.py 6 2

Prints out a random story with 6 sentences using a Markov analysis with prefix length 2

