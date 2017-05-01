# Parsing rules
# precedence = (('left', 'MINUS'),
#               ('right', 'UMINUS'))


# ###############################################################################
# => GRAMMAR RULES
# ###############################################################################


def p_rootstatement_terminal(p):
    '''rootstatement : DOCUMENTCLASS LBRACE ARTICLE RBRACE body'''
    if len(p) == 6:
        p[0] = ('documentclass_article', p[5])
    else:
        p[0] = ('documentclass_article', p[5])

def p_optionaltags_terminal(p):
    '''
    optionaltags : TITLE LBRACE oneormoretext RBRACE
                 | DATE LBRACE oneormoretext RBRACE
                 | AUTHOR LBRACE oneormoretext RBRACE
    '''
    if p[1] == '\\title':
        p[0] = ('title', p[3])
    elif p[1] == '\\date':
        p[0] = ('date', p[3])
    elif p[1] == '\\author':
        p[0] = ('author', p[3])

def p_body_terminal(p):
    '''body : optionaltags body
            | SLASH BEGIN LBRACE DOCUMENT RBRACE section SLASH END LBRACE DOCUMENT RBRACE
            | SLASH BEGIN LBRACE DOCUMENT RBRACE usection SLASH END LBRACE DOCUMENT RBRACE
            | SLASH BEGIN LBRACE DOCUMENT RBRACE oneormoretext SLASH END LBRACE DOCUMENT RBRACE'''
    if len(p) == 12:
        p[0] = ('begin_document', p[6])
    else:
        p[0] = (('tags', p[1]), p[2])

def p_usection_terminal(p):
    '''
    usection : USECTION LBRACE oneormoretext RBRACE subbody
    '''
    p[0] = ('usection', {'title': p[3], 'subbody': p[5]})


def p_section_terminal(p):
    '''
    section : SECTION LBRACE oneormoretext RBRACE subbody
    '''
    p[0] = ('section', {'title': p[3], 'subbody': p[5]})
    

def p_subsection_terminal(p):
    '''
    subsection : SUBSECTION LBRACE oneormoretext RBRACE subbody
    '''
    p[0] = ('subsection', {'title': p[3], 'subbody' : p[5]})


def p_subbody_terminal(p):
    '''
    subbody : section 
            | usection
            | subsection
            | oneormoretext subbody
            | oneormoretext
    '''
    if len(p) == 3:
        p[0] = (p[1], {'subbody': p[2]})
    else:
        p[0] = p[1]


# def p_oneormoresubsection_terminal(p):
#     '''oneormoresubsection : subsection oneormoresubsection 
#                           | subsection
#                           | oneormoretext'''
#     if len(p) == 3:
#         p[0] = ('listofsubsections', p[1], p[2]) 
#     else:
#         p[0] = p[1]
    
def p_ulist_termianl(p):
    '''
        
    '''
    pass

def p_oneormoretext_terminal(p):
    '''oneormoretext : oneormoretext TEXT 
                     | TEXT  '''
    if len(p) == 3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]
    

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p:
        print "Syntax error at '%s'" % p.value, p
    else:
        print "Syntax error at EOF"
    raise Exception('syntax error')
