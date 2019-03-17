#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def cleans_file(fn):
    """
    Functional Programming with map() . Write a program that
    takes a filename and “cleans” the file by removing all leading
    and trailing whitespace from each line. Read in the original
    file and write out a new one, either creating a new file or
    overwriting the existing one. Give your user the option to
    pick which of the two to perform. Convert your solution to
    using list comprehensions.
    """
    print 'Open file: %s' % fn
    with open(fn, 'r') as fd:
        choosen = raw_input('1: overwrite; 2: write to new file;"q" to quit\n')
        if choosen == '1':
            for i, line in enumerate(fd):
                fd[i] = line.strip(' \t')
        elif choosen == '2':
            new_fn = 'new_' + fn
            nfd = open(new_fn, 'w')
            for line in fd:
                nfd.write(line.strip(' \t'))
            nfd.close()
        else:
            return


if __name__ == "__main__":
    cleans_file('test.txt')
