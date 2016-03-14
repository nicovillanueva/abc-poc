# Architecture PoC

And also an example on how to use ABC's to enforce API contracts in classes, and 'statically' analyzing Python files to look for subclasses of a given base class (in a really crude, inefficient and shitty way; but not loading them, which is nice)

## Requires
- Python 3.5
- Go (for no real reason, as the Go binary examples just print shit)

## TODO
- Actually use the Go binaries

## Purpose
The purpose of the thing is to be extensible. To be able to write new "attacks", which must comply with a given API, and to just throw them into a folder to be picked up by the application's main() method.

Sorta imitating Java-like 'interfaces', this compliance is enforced via ABC's (Abstract Base Classes).

Then, in the main() method, we look for BaseClass-extending classes by simply recursively scanning the folder where the attacks are dumped, looking through the file and looking for a given text using a regex. Dirt simple, but functional (and can be much better using threads). A sturdier solution was looked for, but nothing suitable was found. Everything either went over the top and implemented a whole bunch of useless stuff (useless for me, at least), or didn't give me the necessary information, or simply didn't work.

Using the module importlib, we just import the module. Then, with the getattr builtin, we look for the class, give it it's parameters, instantiate it, and return it for the user to have fun.

It's not the most beautiful piece of code I've ever laid my eyes on, or I've ever poured off my fingertips, but hey, it works

## Running
Simply do `python3.5 main.py`. What did you expect?
