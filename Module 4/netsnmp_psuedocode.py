#!/usr/bin/env python
"""
    Provide details regarding your python module here, e.g what it
    does, how to use it, etc.  If you are looking for some example
    doc string syntax you can see examples of Google's format at:

    http://goo.gl/BbPGfb

    To change this template, simply edit the file located at:
    ~/.config/geany/templates/filetype.python

    untitled.py
    Created by Set your name in Edit > Preferences > Templates
    on 22.10.2014 12:43:18 MDT
"""
import sys

class Session():
    def __init__(self, DestHost="", Version="", Community=""):
        self.desthost = DestHost
        self.version = Version
        self.community = Community

    def get(self, avarlistobject):
        for item in avarlistobject.internal_list:
            item.tag
            # pretend code is here to get something from the router using item.tag
            item.val

class Varbind():
    def __init__(self, oid):
        self.tag = oid
        self.val = None
        self.iid = None

class VarList():
    def __init__(self, varbind):
        self.internal_list = list()
        self.internal_list.append(varbind)

    def append(self, varbind):
        self.internal_list.append(varbind)

def main():
    """
    """
    return 0

if __name__ == '__main__':
    sys.exit(main())

