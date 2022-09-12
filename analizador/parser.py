from ply.yacc import yacc
from analizador import lexer

tokens = lexer.tokens

# expresion : expresion MAS expresion
#            | expresion MENOS expresion
#            | expresion MULTI expresion
#            | expresion DIV expresion
#            | MENOS expresion
#            | NUMERO


# precedencia

precedence = (
    ('left', 'MENOS', 'MAS'),
    ('left', 'MULTI', 'DIV'),
    ('right', 'UNARIO'),
)

def p_expresion_op_binaria(p):
    """
    expresion : expresion MAS expresion
               | expresion MENOS expresion
               | expresion MULTI expresion
               | expresion DIV expresion
    """
    # p contiene los elementos de la gramatica
    #
    # expresion : term MAS term
    #   p[0]     : p[1] p[2] p[3]
    #
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '/':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] - p[3]

def p_expresion_unaria(p):
    """
    expresion : MENOS expresion %prec UNARIO
    """
    p[0] = - p[2]

def p_expresion_parentesis(p):
    """
    expresion : PARA expresion PARC
    """
    p[0] = p[2]

def p_expresion_numero(p):
    """
    expresion : NUMERO
    """
    p[0] = p[1]



# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r} en la linea {p.lineno}')


# Build the parser
parser = yacc()

