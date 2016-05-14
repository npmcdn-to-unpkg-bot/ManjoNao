'''
Created on 17/04/2016

@author: Arihane.Mariano
'''

from gluon.contrib.memdb import Query

def insertNew(wVars):
    ret = ''
    
    query = """INSERT INTO MANJA (email, nick_name, text_manja)VALUES ('{0}','{1}','{2}')""".format(wVars.email,wVars.nick,wVars.text)
    
    try:
        db.executesql(query)
    
    except Exception as wE:
        ret = "error Deu ruim"
    
    return ret