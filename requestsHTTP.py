# Http requests
import requests as req
import json

url = "http://localhost:3000/api/NewBuggy/"
headers = {'content-type': 'application/json'}


def getAll():
    r = req.get(url)
    return r.status_code


def postData(Data):
    r = req.post(url, data=json.dumps(Data), headers=headers)
    return r.status_code

'''  To do 
def updateData(id):
    
def deleteData(id):
'''
