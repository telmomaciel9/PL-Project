import sys
import json
import toml
from lex import tokens, texto
import ply.yacc as yacc


# P1  : FT : Section_list 
# P2  : Section_list : Section section_list
# P3  : Section_list : Section
# P4  : Section : '[' Section_name ']' Section_content 
# P5  :         | '[' Section_name ']' Subsection
# P6  :         | Content
# P7  : Subsection : '[' Subsection_name ']' Section_content Subsection
# P8  : Subsection : '[' Subsection_name ']' Section_content 
# P9  : Section_name : OBJECT
# P10 : Subsection_name : SUBOBJECT
# P11 : Section_content : Content Section_content
# P12 :                 | Content
# P13 :                 | COMMENT
# P14 : Content : Key '=' Value
# P15 : Key : KEY
# P16 : Value : STRING
# P17 :       | NUMBER
# P18 :       | IP
# P19 :       | DATE
# P20 :       | TIME
# P21 :       | BOOLEAN
# P22 :       | Array
# P23 : Array : '[' Value_list ']'
# P24 : Value_list : Value ',' Value_list
# P25 :            | Value

def p_FT(p):
    "FT : Section_list"
    p[0] = p[1]

def p_Section_list1(p):
    "Section_list : Section Section_list"
    p[0] = {**p[1], **p[2]}

def p_Section_list2(p):
    "Section_list : Section"
    p[0] = p[1]

def p_Section1(p):
    "Section  : LBRACKET Section_name RBRACKET Section_content"
    p[0] = { p[2]: p[4] }

def p_Section2(p):
    "Section  : LBRACKET Section_name RBRACKET Subsection"
    p[0] = { p[2]: p[4] }

def p_Section3(p):
    "Section  : Content"
    p[0] = p[1]

def p_Subsection1(p):
    "Subsection : LBRACKET Subsection_name RBRACKET Section_content Subsection"
    p[0] = {p[2]: p[4]}
    p[0].update(p[5])

def p_Subsection2(p):
    "Subsection : LBRACKET Subsection_name RBRACKET Section_content"
    p[0] = { p[2]: p[4] }  

def p_Section_name(p):
    "Section_name : OBJECT"
    p[0] = p[1]

def p_Subsection_name(p):
    "Subsection_name : SUBOBJECT"
    p[0] = p[1]

def p_Section_content1(p):
    "Section_content : Content Section_content"
    p[0] = {**p[1], **p[2]}

def p_Section_content2(p):
    "Section_content : Content"
    p[0] = p[1]

def p_Section_content3(p):
    "Section_content : COMMENT"
    p[0] = p[1]

def p_Content(p):
    "Content : Key EQUALS Value"
    p[0] = { p[1] : p[3] }

def p_Key(p):
    "Key : KEY"
    p[0] = p[1]

def p_Value(p):
    '''Value : STRING
             | NUMBER
             | IP
             | DATE
             | TIME
             | BOOLEAN
             | Array
            '''
    p[0] = p[1]

def p_Array(p):
    "Array : LBRACKET Value_list RBRACKET "
    p[0] = p[2]

def p_Value_list(p):
    '''Value_list : Value COMMA Value_list
                  | Value'''
    if len(p) > 2:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_error(p):
    parser.success = False
    print(f"Sintax error: {p.value}")


parser = yacc.yacc()
parser.success = True


# Função para transformar o dicionário TOML em uma string JSON
def to_json(toml_dict):
   return json.dumps(toml_dict, indent=2)


#parser.parse(texto)
parsed_dict = parser.parse(texto)
print(parsed_dict)
json_string = to_json(parsed_dict)
print(json_string)

with open("out.json", "w") as f:
    json.dump(parsed_dict, f, ensure_ascii=False)