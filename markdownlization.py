# -*- coding: utf-8 -*-

'''
1 make markdown formate file 
2 change to html
'''

__author__='zmming'

import markdown

def convert2html(text):
    html = markdown.markdown(text)
    return html

def title(text, n):
    pre='#'*n
    tail='\n'
    return pre+text+tail
    
def num(text):
    pre='1. '
    tail='\n'
    return pre+text+tail
    
def noNum(text):
    pre='- '
    tail='\n'
    return pre+text+tail
    
def italic(text):
    pre='*'
    tail='*\n'
    return pre+text+tail
    
def bold(text):
    pre='**'
    tail='**\n'
    return pre+text+tail
    
def italicBold(text):
    pre='***'
    tail='***\n'
    return pre+text+tail

def quote(text):
    pre='>'
    tail='\n'
    return pre+text+tail

def pic(picName, description):
    pre='!['+description+']'
    tail='('+picName+')\n'
    return pre+tail

def tab(title, body):
    pre='|'+'|'.join(title)+'|'+'\n'+('|---------:|'*len(title))+'\n'
    con=''
    for line in body:
        con+=('|'+'|'.join(line)+'|\n')
    return pre+con    


if __name__=='__main__':
    text=title('test', 3)
    text+=italicBold('context')
    t=['tab1','tab2','tab3']
    b=[['n1','n2','n3'],['m1','m2','m3']]
    text+=tab(t,b)
    html=convert2html(text)
    print html
