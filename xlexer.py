from sly import Lexer

class XLexer(Lexer):
  tokens = {ID, INT, FLOAT}
  
  literals = { '=', '+', '-', '*', '/', '(', ')' }
  
  ignore = ' \t'
  
  # TOKENS
  ID = r'[a-zA-Z][a-zA-Z0-9_]*'
  
  
  @_(r'[0-9]+\.[0-9]+')
  def FLOAT(self, t):
    t.value = float(t.value)
    return t
  
  @_(r'\d+')
  def INT(self, t):
      t.value = int(t.value)
      return t
  
  
  # Special functions for newline so as to increase the line number after encountering any newline....
  @_(r'\n+')
  def newline(self, t):
    self.lineno += t.value.count('\n')
    
  # This handles happens whenever it finds mystery characters
  
  # Instead of crashing it should just print an error
  
  def error(self, t):
    print(f"Illegal character {t.value!r} at line {self.lineno}")
    self.index += 1
    
    