#!/usr/bin/env python
'''
Created by Seria at 02/11/2018 3:57 PM
Email: zzqsummerai@yeah.net

                    _ooOoo_
                  o888888888o
                 o88`_ . _`88o
                 (|  0   0  |)
                 O \   。   / O
              _____/`-----‘\_____
            .’   \||  _ _  ||/   `.
            |  _ |||   |   ||| _  |
            |  |  \\       //  |  |
            |  |    \-----/    |  |
             \ .\ ___/- -\___ /. /
         ,--- /   ___\<|>/___   \ ---,
         | |:    \    \ /    /    :| |
         `\--\_    -. ___ .-    _/--/‘
   ===========  \__  NOBUG  __/  ===========
   
'''
# -*- coding:utf-8 -*-

import time

def Timer(func):
    def _timerWrapper(*args, **kwargs):
        t_ = time.time()
        ret = func(*args, **kwargs)
        _t = time.time()
        if not isinstance(ret, tuple):
            ret = (ret,)
        return (_t - t_,) + ret

    return _timerWrapper
