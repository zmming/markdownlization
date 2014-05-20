# -*- coding: utf-8 -*-

'''
1 make markdown formate file 
2 change to html
'''

__author__='zmming'

import markdown

class markdownlization:
    def convert2html(self,text):
        html = markdown.markdown(text)
        return html
    


if __name__=='__main__':
    md=markdownlization()
    text='#test'
    html=md.convert2html(text)
    print html
