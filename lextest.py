import sys
import ply.lex as lex
import toml


tokens = (
    #'LPAREN',
    'OBJECT',
    #'RPAREN',
    'KEY',
    'STRING',
    'COMMENT',
    'NUM',
    'IP',
    'DATE',
    'TIME',
    'BOOLEAN'
)

literals = '-:.",[]'

t_ignore = ' \t\n=,[]'

def t_BOOLEAN(t): r'TRUE|FALSE|true|false'; return t
def t_IP(t): r'\"\d+\.\d+\.\d+\.\d+\"'; return t
def t_DATE(t): r'\d+\-\d+\-\d+'; return t
def t_TIME(t): r'\d+\:\d+\:\d+'; return t
def t_NUM(t): r'\d+'; return t
def t_COMMENT(t): r'\#\s.*'; return t
def t_KEY(t): r'[a-z]+\D?[a-z]+\s'; return t
#def t_LPAREN(t): r'\[' ; return t
def t_STRING(t): r'\".+\"'; return t
def t_OBJECT(t): r'[a-z]*\.?[a-z]+'; return t
#def t_RPAREN(t): r'\]' ; return t



def t_error(t):
    print("Erro: " + t.value[0], file=sys.stderr)
    t.lexer.skip(1)

lexer = lex.lex()


with open("exemplo1.toml",'r') as file:
    texto = file.read()

    lexer.input(texto)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)