#!/usr/bin/env python
# encoding: utf-8
import Queue

if __name__ == '__main__':

    a = Queue.Queue()
    a.put((1,2))
    a.put((2,3))

    print a.empty()
