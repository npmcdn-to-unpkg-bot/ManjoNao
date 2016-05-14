'''
Created on 18/04/2016

@author: Arihane.Mariano
'''

import processor

processor.db = db
def saveThat():
    if request.args[0] == 'insert':
        #ret = processor.insertNew(request.vars);
        query = """INSERT INTO MANJA (email, nick_name, text_manja)
        VALUES ('{0}','{1}','{2}')""".format(request.vars.email,request.vars.nick,request.vars.descript)
        ret = ''
        try:
            db.executesql(query)
            values = db.executesql('select * from manja',as_dict=True)
    
        except Exception as wE:
            ret = "error Deu ruim"
    if request.args[0] == 'update':
        #ret = processor.insertNew(request.vars);
        query = """UPDATE MANJA SET email='{0}', nick_name='{1}', text_manja='{2}'
        WHERE id={3} """.format(request.vars.email,request.vars.nick,request.vars.descript,request.vars.id)
        ret = ''
        try:
            db.executesql(query)
            values = db.executesql('select * from manja',as_dict=True)
    
        except Exception as wE:
            ret = "error Deu ruim"        
        

        return XML(response.json({'info':ret, 'values':values}))


def delThat():
    
    if request.vars.id != None:
        try:
            db.executesql('delete from manja where id='+str(request.vars.id))
            ret = 'deu'
            values = db.executesql('select * from manja',as_dict=True)
        
        except Exception as wE:
            ret =  wE
            
        return XML(response.json({'info':ret, 'values':values}))
        
        
def getAll():
    values = db.executesql('select id, nick_name as nick, text_manja as descript, email from manja',as_dict=True)
    return XML(response.json(values))