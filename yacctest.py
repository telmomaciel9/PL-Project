

# T   : {'=', '[', ']', ',', KEY, OBJECT, STRING, BOOLEAN, IP, 
#        NUM, DATE, TIME, COMMENT}
# NT  : {FT, Linha, Atributo, Objeto, Valor, List, LCont, Conteudo, Cont2}

# P1  : FT : Linha FT 
# P2  :    | Linha
# P3  : Linha : Atributo Linha
# P4  :       | Objeto 
# P5  :       | 
# P6  : Atributo : KEY '=' Valor
# P7  : Objeto : '[' OBJECT ']' Linha
# P8  : Valor : STRING
# P9  :       | BOOLEAN
# P10 :       | IP
# P11 :       | NUM
# P12 :       | DATE
# P13 :       | TIME
# P14 :       | List
# P15 :       | COMMENT
# P16 : List : '[' LCont
# P17 : LCont : ']'
# P18 :       | Conteudo ']'
# P19 : Conteudo : Valor Cont2
# P20 : Cont2 : ',' Conteudo
# P21 :       |


def p_FT1(t):
    "FT : Linha FT "

def p_FT2(t):
    "FT : Linha"

def p_Linha1(t):
    "Linha : Atributo Linha"

def p_Linha2(t):
    "Linha : Objeto"

def p_Linha3(t):
    "Linha : "

def p_Atributo(t):
    "Atributo : KEY '=' Valor"

def p_Objeto(t):
    "Objeto : '[' OBJECT ']' Linha"

def p_Valor1(t):
    "Valor : STRING"

def p_Valor2(t):
    "Valor : BOOLEAN"

def p_Valor3(t):
    "Valor : IP"

def p_Valor4(t):
    "Valor : NUM"

def p_Valor5(t):
    "Valor : DATE"

def p_Valor6(t):
    "Valor : TIME"

def p_Valor7(t):
    "Valor : LIST"  

def p_Valor8(t):
    "Valor : COMMENT"                      

def p_List(t):
    "List : '[' LCont"

def p_LCont1(t):
    "LCont : ']'"

def p_LCont2(t):
    "LCont : Conteudo ']'"

def p_Conteudo(t):
    "Conteudo : Valor Cont2"

def p_Cont2_1(t):
    "Cont2 : ',' Conteudo"

def p_Cont2_2(t):
    "Cont2 : "