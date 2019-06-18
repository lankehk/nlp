# -*- coding: utf-8 -*-
"""This module contains a template Workbench application"""
from mindmeld import Application
from mindmeld.components import QuestionAnswerer
import os
import sys
app = Application(__name__)

__all__ = ['app']


@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('Hello there!')
    responder.listen()

@app.handle(intent ='greet')
def greeting(request,responder):
    a = os.environ['HOME'].split('/')
    name = a[-1]
    r = "hi " + name + " This is a Greeting Message"
    responder.reply(r)
    responder.listen()

@app.handle(intent ='unspported')
def warningCust(request,responder):
    r = 'Please ask a valid question'
    responder.reply(r)
    responder.listen()

@app.handle(intent='get_companies')
def listcompanies(request,responder):
    r = 'The Companies which came are ' 
        
    companies = app.question_answerer.get(index = 'companies')
    names = []
    for i in companies:
        names.append(i['company_name'])
    r = r + ",".join(names)

    responder.reply(r)

@app.handle(intent = 'get_year')
def giveyear(request,responder):
    companies = app.question_answerer.get(index='companies')
    names = []
    for i in companies:
        names.append(i['company_name'])
    tokens = request.text.split()
    #print(tokens)
    #print(names)
    flag = 0
    for i in names:
        if flag ==1:
            break
        for j in tokens:
            if i.lower() == j.lower():
                ans = i
                flag = 1
                break
    if flag == 0: 
        responder.reply('Sorry,Not Found')
        return 
    for i in companies:
        if i['company_name'] == ans:
           year = i['year']
           sal = i['salary']
           break
    r = 'The year in which %s came is %s with salary of %s' %(ans, year,sal) 
    responder.reply(r)
 
@app.handle(intent = 'get_sal')
def getsal(request,responder):
    y = app.question_answerer.get(index = 'salary')
    #print(type(y))
    #for i in y:
    #    print(type(i['yearsal']))
    #    print(i)
    tokens = request.text.split()
    names = []
    for i in y:
        names.append(i['company_name'])
    flag = 0
    #print(request)
    company = request.entities[0]['value'][0]['cname']
    #print(company,"****")
    tokens.append(company)
    #print(names)
    for i in tokens:
        if flag == 1:
            break
        for j in names:
            if i.lower() == j.lower():
                ans = i
                flag = 1
                break
    


    if flag == 0:
        responder.reply("Sorry Can't Understand")
    else:
        sal = []
        year = []
        
        for i in y:
            if i['company_name'] == ans:
                a = i['years'].split()
                b = i['sals'].split()
                for j in range(len(a)):
                    responder.reply(i['company_name']+" gave a salary of "+b[j]+" in the year "+a[j]+".")
                    
                     
       









@app.handle(intent='exit')
def Exitmessage(request,responder):
    a = os.environ['HOME'].split('/')
    r = "Bye " + a[-1] 
    responder.reply(r)
    exit
