#!/usr/bin/env python

"""
Cacheability checking function. Called on complete responses by RedFetcher.
"""

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2008-2012 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import redbot.message_check.cache
import redbot.message_check.headers
import redbot.message_check.status

class MessageChecker(object):
    """
    Checks HTTP messages to make sure they're syntactically correct, as well
    as commenting upon their semantics. Does not perform any requests.

    If the message_type is known, it should be stated in message_type; "req"
    or "res". If left as None, we'll guess.

    If headers_only is true, it's assumed that the message will be complete, 
    and therefore we'll be checking the entire message; otherwise, we expect
    it to be syntactically complete.
    """
    def __init__(self, state):
        headers.process_headers(state)
        status.ResponseStatusChecker(state)
        cache.checkCaching(state)