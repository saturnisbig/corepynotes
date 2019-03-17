#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from time import time


def logged(when):
    def log(f, *args, **kwargs):
        print '''Called:
        function: %s
        args: %r
        kwargs: %r''' % (f, args, kwargs)

    def pre_logged(f, *args, **kwargs):
        def wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper

    def post_logged(f, *args, **kwargs):
        def wrapper(*args, **kwargs):
            start = time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print "time delta: %s" % (time() - start)
        return wrapper
    try:
        return {'pre': pre_logged,
                'post': post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@logged("post")
def hello(name):
    print "Hello, ", name

hello("World!")
