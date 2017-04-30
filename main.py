#===============================================================================
# => Latex to pdf compiler
#===============================================================================

import sys
from lexer import *
from parser import *
import ply.lex as lex
import ply.yacc as yacc

# DEBUGGING
# from test import *
# from pprint import pprint

sys.path.insert(0, "../../")

lexer = lex.lex()
parser = yacc.yacc()


def makepdf(parseTree):
    """ Using the parseTree write the pdf file.

    :parseTree: parse tree of yacc parse
    :returns: result msg as string

    """
    pass

def main(*args, **kwargs):
    args = args[0]
    if (len(args) == 0):
        print "enter latex file to read"
    elif len(args) == 1:
        f = open(args[0])
        latexCode = ''.join([l for l in f.readlines()]).split('\n')
        print latexCode
        # print lex.lex(latexCode)
        print lexer.input(''.join(latexCode))
        
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)
        print('TOKENS ENDED')
        try:
            res = parser.parse(''.join(latexCode))
            print res
            print "pdf made sucessfully as " + args[0] + ".pdf"
        except Exception as e:
            print(e)
    else:
        print "invalid number of args given"

if __name__ == "__main__":
    main(sys.argv[1:])
