import sys
import ply.lex as lex
import toml
import re

tokens = (
    'STRING',
    'COMMENT',
    'NUMBER',
    'IP',
    'DATE',
    'TIME',
    'BOOLEAN',
    #'IDENTIFIER',
    'KEY',
    'OBJECT',
    'SUBOBJECT',
    'LBRACKET',
    'RBRACKET',
    'EQUALS',
    'COMMA',
)

literals = '-:.",=[]'

t_ignore = ' \t\n'

def t_BOOLEAN(t): 
    r'TRUE|FALSE|true|false'
    t.value = True if t.value == 'true' else False 
    return t

def t_IP(t): 
    r'\"\d+\.\d+\.\d+\.\d+\"'
    t.value = t.value[1:-1]  # Remove aspas
    return t

def t_DATE(t): 
    r'\d+\-\d+\-\d+'
    return t

def t_TIME(t): 
    r'\d+\:\d+\:\d+'
    return t

def t_NUMBER(t): 
    r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

def t_COMMENT(t):
    r'(\#\s.*)'
    return t

def t_STRING(t): 
    r'("[^"]*" | \'[^\']*\' | """[^"]*""" | \'\'\'[^\']*\'\'\')'
    t.value = t.value[1:-1]  # Remove aspas
    return t

#def t_IDENTIFIER(t): 
#    r'[a-zA-Z_][a-zA-Z0-9_]*'
#    return t

def t_KEY(t): r'[a-z]+\D?[a-z]+\s'; return t

def t_SUBOBJECT(t): 
    r'[a-z]*\.[a-z]+'
    match = re.match(r'([a-z]*)\.([a-z]+)', t.value)
    if match:
        t.value = match.group(2)
    return t

def t_OBJECT(t): 
    r'[a-z]+'
    return t

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'='
t_COMMA = r','


def t_error(t):
    print("Erro: " + t.value[0], file=sys.stderr)
    t.lexer.skip(1)

lexer = lex.lex()


with open("exemplo2.toml",'r') as file:
    texto = file.read()

    lexer.input(texto)

    while True:
        tok = lexer.token()
        if not tok:
            break
        #print(tok)