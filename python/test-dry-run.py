#!/usr/bin/python


import sys


def run(run=False):
    if run:
        print "Actual run. About to commit changes!"
    else:
        print "This is a dry run. Please stay calm!"


if __name__ == '__main__':
    run('--run' in sys.argv)
