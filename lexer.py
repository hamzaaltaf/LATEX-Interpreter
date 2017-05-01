# TOKENS
t_ignore                = ' \t\v\r\b' # shortcut for whitespace

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1
        pass

tokens = (
	'SLASH',			# \
	'DOCUMENTCLASS',	# documentclass  
	'BEGIN',			# begin
	'END',				# end
	'ARTICLE',			# article
	'DOCUMENT',			# document
	'TITLE',			# title
	'AUTHOR',			# author
	'DATE',				# date
	# 'MAKETITLE'			# maketitle
	'SECTION',			# section
	'SUBSECTION',		# subsection
	'USECTION',
	'BOLD',				# bold
	'ITALIC',			# italic
	'UNDERLINE',		# underline
	'ITEMIZE',			# itemize
	'ITEM',				# item
	# 'FIGURE',			# figure
	# 'INCLUDEGRAPHICS',	# includegraphics
	# 'WORD',				# apple
	'LBRACE',			# {
	'RBRACE',			# }
	# 'ASTERISK',			# *
	# 'TWOCOLUMN',		# twocolumn
	# 'LSBRACE',			# [
	# 'RSBRACE',			# ]
	'TEXT'
	)


t_SLASH			= r'\\ '
t_DOCUMENTCLASS	= r'\\documentclass'
t_BEGIN			= r'begin'
#t_END			= r'end'
t_ARTICLE		= r'article'
t_DOCUMENT		= r'document'
t_TITLE			= r'\\title'
t_AUTHOR		= r'\\author'
t_DATE			= r'\\date'

#t_DATE_TEXT     = r'(\d+-\d+-\d+)'
# t_MAKETITLE		= r'maketitle'
t_SECTION			= r'\\section'
t_USECTION          = r'\\section*'
t_SUBSECTION		= r'\\subsection'
t_BOLD			= r'textbf'
t_ITALIC			= r'textit'
t_UNDERLINE		= r'underline'
t_ITEMIZE			= r'itemize'
t_ITEM			= r'item'
# t_FIGURE			= r'figure'
# t_INCLUDEGRAPHICS	= r'includegraphics'
# t_WORD			= r'[a-zA-Z_][a-zA-Z_0-9]*'
t_LBRACE			= r'\{'
t_RBRACE			= r'\}'
# t_ASTERISK		= r'\*'
# t_TWOCOLUMN		= r'twocolumn'
# t_LSBRACE			= r'\['
# t_RSBRACE			= r'\]'
t_TEXT          = r'\w+'

def t_END(t):
    r'end'
    return t

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)