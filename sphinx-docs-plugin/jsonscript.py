# -*- coding: utf-8 -*-
"""
    pygments.lexers.jsonscript
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for JsonScript.

    :copyright: Copyright 2016 by NaviCore team, Mapbar Inc.
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
            (words(('enum', 'if'), suffix=r'\b'), Keyword),
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
