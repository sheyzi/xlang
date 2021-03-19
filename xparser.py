from sly import Parser
from xlexer import *

class XParser(Parser):
    tokens = XLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', UMINUS),
        )

    def __init__(self):
        self.ids = { }

    @_('ID "=" expr')
    def statement(self, p):
        self.ids[p.ID] = p.expr
     

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('INT')
    def expr(self, p):
        return p.INT
        
    @_('FLOAT')
    def expr(self, p):
        return p.FLOAT

    @_('ID')
    def expr(self, p):
        try:
            return self.ids[p.ID]
        except LookupError:
            print("Undefined name '%s'" % p.ID)
            return 0
