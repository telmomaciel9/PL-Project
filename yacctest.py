

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
# P15    :       | COMMENT
# P16 : List : '[' LCont
# P17 : LCont : ']'
# P18 :       | Conteudo ']'
# P19 : Conteudo : Valor Cont2
# P20 : Cont2 : ',' Conteudo
# P21 :       |
