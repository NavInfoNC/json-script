# -*- coding: utf-8 -*-
"""
    pygments.lexers.jsonscript
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for JsonScript.

    :copyright: Copyright 2016 by NavInfo's NaviCore Department

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, using, \
    this, inherit, default, words
from pygments.util import get_bool_opt
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error

__all__ = ['JsonScriptLexer']

class JsonScriptLexer(RegexLexer):
    """
    For JsonScript source code
    """
    name = 'JsonScript'
    aliases = ['jss']
    filenames = ['*.jss', '*.JSS']
    priority = 0.1
    
    tokens = {
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text),  # line continuation
            (r'//(\n|(.|\n)*?[^\\]\n)', Comment.Single),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String),  # all other characters
            (r'\\\n', String),  # line continuation
            (r'\\', String),  # stray backslash
        ],
        'statements': [
            (r'<root>', Keyword),
            (r'L?"', String, 'string'),
            include('whitespace'),
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+[LlUu]*', Number.Float),
            (r'(\d+\.\d*|\.\d+|\d+[fF])[fF]?', Number.Float),
            (r'0[0-7]+', Number.Oct),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'\d+', Number.Integer),
            (words(('enum', 'if', 'optional', 'required'), suffix=r'\b'), Keyword),
            (r'[~!%^&*+=|?:<>/-]', Operator),
            (r'(bool|int|string|float)\b', Keyword.Type),
            (r'(true|false)\b', Name.Builtin),
            ('[a-zA-Z_]\w*', Name),
            (r'[()\[\],.]', Punctuation),
            ('[{}]', Punctuation),
            (';', Punctuation, '#pop'),
        ],
        'root': [
            default('statements'),
        ]
    }
