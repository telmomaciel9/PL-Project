import sys
import json
import toml
import yaml
import os
import xml.etree.ElementTree as ET
from lex import tokens, texto, linguagem
import ply.yacc as yacc


# P1  : FT              : Section_list 
# P2  : Section_list    : Section section_list
# P3  :                 | Section
# P4  : Section         : '[' Section_name ']' Section_content 
# P5  :                 | '[' Section_name ']' Subsection
# P6  :                 | Content
# P7  : Table           : LBRACKET LBRACKET Section_name RBRACKET RBRACKET Section_content Table
# P8  :                 | LBRACKET LBRACKET Section_name RBRACKET RBRACKET Section_content
# P9  : Subsection      : '[' Subsection_name ']' Section_content Subsection
# P10 :                 | '[' Subsection_name ']' Section_content 
# P11 : Section_name    : OBJECT
# P12 : Subsection_name : SUBOBJECT
# P13 : Section_content : Content Section_content
# P14 :                 | Content
# P15 :                 | COMMENT
# P16 : Content         : Key '=' Value
# P17 : Key             : KEY
# P18 : Value           : BASIC_STRING
#                       | LITERAL_STRING
#                       | STRING
# P19 :                 | NUMBER
# P20 :                 | IP
# P21 :                 | DATE
# P22 :                 | TIME
# P23 :                 | DATE_TIME
# P23 :                 | BOOLEAN
# P24 :                 | Array
# P25 : Array           : '[' Value_list ']'
# P26 : Value_list      : Value ',' Value_list
# P27 :                 | Value

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

def p_Section4(p):
    "Section  : Table"
    p[0] = p[1]

def p_Table1(p):
    "Table : LBRACKET LBRACKET Section_name RBRACKET RBRACKET Section_content Table"
    keys_list = list(p[7].keys())
    if p[3] == keys_list[0]:
        p[0] = {p[3]: [p[6]]+p[7][p[3]]}
    else:
        p[0] = {p[3]: [p[6]]}
        p[0].update(p[7])

def p_Table2(p):
    "Table : LBRACKET LBRACKET Section_name RBRACKET RBRACKET Section_content"
    p[0] = { p[3]: [p[6]] }

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
             | DATE_TIME
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

parsed_dict = parser.parse(texto)
parser.parse(texto)