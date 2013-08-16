# (The MIT License)
#
# Copyright (c) 2013 Kura
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Blackhole is an email MTA that pipes all mail to /dev/null

Blackhole is just any other MTA out there except it does not
actual do any disk I/O with the mail it receives. It is simply
accept or rejected based on configuration and pretends it's
actually done something.
"""

__author__ = "Kura"
__copyright__ = "None"
__credits__ = ["Kura", ]
__license__ = "MIT"
__version__ = "1.9.0"
__maintainer__ = "Kura"
__email__ = "kura@kura.io"
__status__ = "Stable"

__pname__ = "blackhole"
__desc__ = "blackhole.io MTA"

__fullname__ = "%s %s" % (__pname__, __version__)
