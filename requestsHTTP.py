# Http requests
import requests as req
import json

url = "http://localhost:3000/api/NewBuggy/"
headers = {'content-type': 'application/json'}


def getAll():
    req.get(url)


def postData(Data):
    req.post(url, data=json.dumps(Data), headers=headers)

'''  To do 
def updateData(id):
    
def deleteData(id):
'''
