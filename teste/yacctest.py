import sys
import json
import toml
from lextest import tokens, texto
import ply.yacc as yacc

# T   : {'=', '[', ']', ',', KEY, OBJECT, STRING, BOOLEAN, IP, 
#        NUM, DATE, TIME, COMMENT}
# NT  : {FT, Linha, Atributo, Objeto, Valor, List, LCont, Conteudo, Cont2}

# P1  : FT : Linha FT 
# P2  :    | 
# P3  : Linha : Atributo 
# P4  :       | Objeto 
# P5  :       | COMMENT 
# P6  : Atributo : KEY '=' Valor
# P7  : Objeto : '[' OBJECT ']' Linha
# P8  : Valor : STRING
# P9  :       | BOOLEAN
# P10 :       | IP
# P11 :       | NUM
# P12 :       | DATE
# P13 :       | TIME
# P14 :       | List
# P15 : List : '[' LCont
# P16 : LCont : ']'
# P17 :       | Conteudo ']'
# P18 : Conteudo : Valor Cont2
# P19 : Cont2 : ',' Conteudo
# P20 :       |

dic = {}

def p_FT1(p):
    "FT : Linha FT "
    #print("Reconheci uma linha:", p[1])
    p[0] = p[1] + "\n" + p[2]

def p_FT2(p):
    "FT : "
    p[0] = ""

def p_Linha1(p):
    "Linha : Atributo"
    #print(p[1])
    p[0] = p[1] 

def p_Linha2(p):
    "Linha : Objeto"
    #print(p[1])
    p[0] = p[1]

def p_Linha3(p):
    "Linha : COMMENT"
    #print("Reconheci um COMMENT:", p[1])
    p[0] = p[1]

def p_Atributo(p):
    "Atributo : KEY '=' Valor"
    #print("key:", p[1], ", valor:", p[3])
    p[0] = p[1] + ' : ' + p[3]
    #dic[p[1]]=p[3]

def p_Objeto(p):
    "Objeto : '[' OBJECT ']'"
    #print("Reconheci um object: ", p[2])
    p[0] = p[2] 

def p_Valor1(p):
    "Valor : STRING"
    #print("Reconheci uma string", p[1])
    p[0] = p[1]

def p_Valor2(p):
    "Valor : BOOLEAN"
    #print("Reconheci um bool", p[1])
    p[0] = p[1]

def p_Valor3(p):
    "Valor : IP"
    #print("Reconheci um IP", p[1])
    p[0] = p[1]

def p_Valor4(p):
    "Valor : NUM"
    #print("Reconheci um NUM", p[1])
    p[0] = p[1]

def p_Valor5(p):
    "Valor : DATE"
    #print("Reconheci uma DATA", p[1])
    p[0] = p[1] 

def p_Valor6(p):
    "Valor : TIME"
    #print("Reconheci TIME", p[1])
    p[0] = p[1]  

def p_Valor7(p):
    "Valor : List"
    #print("Reconheci a lista:", p[1])
    p[0] = p[1]                       

def p_List(p):
    "List : '[' LCont"
    p[0] = p[1] + p[2] 

def p_LCont1(p):
    "LCont : ']'"
    p[0] = p[1]

def p_LCont2(p):
    "LCont : Conteudo ']'"
    p[0] = p[1] + p[2] 

def p_Conteudo(p):
    "Conteudo : Valor Cont2"
    p[0] = p[1] + p[2]

def p_Cont2_1(p):
    "Cont2 : ',' Conteudo"
    p[0] = ',' + p[2] 

def p_Cont2_2(p):
    "Cont2 : "
    p[0] = ""

def p_error(p):
    parser.success = False
    print(f"Sintax error: {p.value}")


parser = yacc.yacc()
parser.success = True

print(parser.parse(texto))


with open("out.json", "w") as f:
    json.dump(dic, f, ensure_ascii=False)
