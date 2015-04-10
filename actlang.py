# import re
import re
import math
# 1. create token rules for each token and assign a regular expression to each token
  #- make sure that there's a carrot in each token
NUMBER = re.compile(r'^[0-9]+')
ADD = re.compile(r'^\+')
SUBTRACT = re.compile(r'^\-')
MULTIPLY = re.compile(r'^\*')
DIVIDE = re.compile(r'^\/')
LOG = re.compile(r'^log')
ROOT2 = re.compile(r'^root2')
ROOT3 = re.compile(r'^root3')
CARET = re.compile(r'^\^')
LPAREN = re.compile(r'^\(')
RPAREN = re.compile(r'^\)')
WHITESPACE = re.compile(r'^[ \n\t]+')

# 2. test tokenizer by assigning a source variable some expression you want to check
# source = '3+4^2+log(3)'
# print "source is: ", source

# 3. then while the length of your source is not zero, look for each token type in your source
#tokens = []
source = ''
tokens = []

def lexer():
    global source
    global tokens
    def tokstep(type, typename, source):
      a = type.findall(source)
      if len(a) != 0:
        # 4. if a token is found, we must reduce our source string by the length of the token found
        source = source[len(a[0]):]
        if typename != 'WHITESPACE':
          # 5. also, we must place the token type and the token itself in a list and put that list into a tokens variable
          # 6. to deal with whitespace, we can not include the whitespace token when it comes up in step 5
          tokens.append([typename, a[0]])
      return source

    while len(source) != 0:
      source = tokstep(NUMBER, 'NUMBER', source)
      source = tokstep(ADD, 'ADD', source)
      source = tokstep(SUBTRACT, 'SUBTRACT', source)
      source = tokstep(MULTIPLY, 'MULTIPLY', source)
      source = tokstep(DIVIDE, 'DIVIDE', source)
      source = tokstep(LOG, 'LOG', source)
      source = tokstep(ROOT2, 'ROOT2', source)
      source = tokstep(ROOT3, 'ROOT3', source)
      source = tokstep(CARET, 'CARET', source)
      source = tokstep(LPAREN, 'LPAREN', source)
      source = tokstep(RPAREN, 'RPAREN', source)
      source = tokstep(WHITESPACE, 'WHITESPACE', source)

#
# print "tokens: ", tokens

# tokens = [['NUMBER', '3'], ['ADD', '+'],['NUMBER', '2']]
#
#PARSER
# 1. Make utility functions for LL(1) grammar: lookahead which looks at the first element of your tokens list
def lookahead():
    if len(tokens):
        return tokens[0]
    else:
        return ['EOF', '']

# consume which truncates list by taking out the first element
def consume():
    global tokens
    tokens = tokens[1:]

# 2. create functions that either return another expression or appends the token to a list. Start each tree-able function with a new list to contain within. Work from most general to most specific.
def expr():
    return expr_add()

def expr_add():
    ret = []
    ret.append(expr_mul())

    look_value = lookahead()[0]
    look_token = lookahead()

    if look_value == 'ADD' or look_value == 'SUBTRACT':
        ret.append(look_token)
        consume()
        ret.append(expr_add())

    return ret


def expr_mul():
    ret = []
    ret.append(expr_atom())

    look_value = lookahead()[0]
    look_token = lookahead()

    if look_value == 'MULTIPLY' or look_value == 'DIVIDE' or look_value == 'CARET':
        ret.append(look_token)
        consume()
        ret.append(expr_mul())

    return ret


def expr_atom():
    ret = []
    look_value = lookahead()[0]
    look_token = lookahead()

    if look_value == 'NUMBER':
        ret.append(look_token)
        consume()
    elif look_value == 'LOG' or look_value == 'ROOT2' or look_value == 'ROOT3':
        ret.append(look_token)
        consume()
        #LPAREN
        ret.append(lookahead())
        consume()
        #expr
        ret.append(expr())
        #RPAREN
        ret.append(lookahead())
        consume()
    elif look_value == 'LPAREN':
        ret.append(look_token)
        consume()
        ret.append(expr())
        ret.append(lookahead())
        consume()
    else:
        print "error, atom type expected"

    return ret

# 3. return the highest level expression in your parser function.
def parser():
    return expr()

#p = parser()
# print "parser: "
# print p

#EVALUATOR
# 1. Start from most general expression to most specific. Extract tokens from tree and return the evaluated expression. Look at BNF to determine where it will be recursive and just put that expression evaluator in there.

def interpret_expr(p):
    return interpret_expr_add(p)

def interpret_expr_add(p):
    mul = interpret_expr_mul(p[0])
    if len(p) > 1:
        tokenname = p[1][0]
        if tokenname == 'ADD':
            add = interpret_expr_add(p[2])
            return mul+add
        elif tokenname == 'SUBTRACT':
            add = interpret_expr_add(p[2])
            return mul-add
    return mul

def interpret_expr_mul(p):
    atom = interpret_expr_atom(p[0])
    if len(p) > 1:
        tokenname = p[1][0]
        if tokenname == 'MULTIPLY':
            mul = interpret_expr_mul(p[2])
            return atom*mul
        elif tokenname == 'DIVIDE':
            mul = interpret_expr_mul(p[2])
            return atom/(mul*1.0)
        elif tokenname == 'CARET':
            mul = interpret_expr_mul(p[2])
            return atom**(mul)
    return atom

def interpret_expr_atom(p):
    tokenname = p[0][0]
    if tokenname == 'NUMBER':
        return int(p[0][1])
    elif tokenname == 'LOG':
        expr = interpret_expr(p[2])
        return math.log(expr)
    elif tokenname == 'ROOT2':
        expr = interpret_expr(p[2])
        return math.sqrt(expr)
    elif tokenname == 'ROOT3':
        expr = interpret_expr(p[2])
        return expr**(1/3.0)
    elif tokenname == 'LPAREN':
        expr = interpret_expr(p[1])
        return expr
    else:
        print "error in atom element"

def interpret(p):
    return interpret_expr(p)

# print "evaluated result:"
# print interpret(p)
while True:
    source = raw_input("Enter expression:")
    tokens = []
    lexer()
    p = parser()
    print interpret(p)
