import sys
import ply.lex as lex


tokens = (
    'LPAREN',
    'OBJECT',
    'RPAREN',
    'KEY',
    'STRING',
    'COMMENT',
    'NUM',
    'IP',
    'DATE',
    'TIME',
    'BOOLEAN'
)

literals = '-:.",'

t_ignore = ' \t\n=,'

def t_BOOLEAN(t): r'TRUE|FALSE|true|false'; return t
def t_IP(t): r'\"\d+\.\d+\.\d+\.\d+\"'; return t
def t_DATE(t): r'\d+\-\d+\-\d+'; return t
def t_TIME(t): r'\d+\:\d+\:\d+'; return t
def t_NUM(t): r'\d+'; return t
def t_COMMENT(t): r'\#\s.*'; return t
def t_KEY(t): r'[a-z]+\D?[a-z]+\s'; return t
def t_LPAREN(t): r'\[' ; return t
def t_STRING(t): r'\".+\"'; return t
def t_OBJECT(t): r'[a-z]*\.?[a-z]+'; return t
def t_RPAREN(t): r'\]' ; return t



def t_error(t):
    print("Erro: " + t.value[0], file=sys.stderr)
    t.lexer.skip(1)

lexer = lex.lex()

texto= '''

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
date = 2010-04-23
time = 21:30:00

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]
[servers.alpha]
ip = "10.0.0.1"
dc = "eqdc10"

[servers.beta]
ip = "10.0.0.2"
dc = "eqdc10"

# Line breaks are OK when inside arrays
hosts = [
"alpha",
"omega"
]

'''

lexer.input(texto)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)