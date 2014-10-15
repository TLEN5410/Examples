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
    on 15.10.2014 14:38:05 MDT
"""
import sys
import netsnmp

def main():
    """
    """
    session = netsnmp.Session(Version=1, Community='supersecretpassword',
                              DestHost='198.51.100.1')

    syscontact = netsnmp.Varbind('.1.3.6.1.2.1.1.4.0')
    varlist = netsnmp.VarList(syscontact)

    print syscontact.tag
    session.get(varlist)
    print syscontact.val


    return 0

if __name__ == '__main__':
    sys.exit(main())

