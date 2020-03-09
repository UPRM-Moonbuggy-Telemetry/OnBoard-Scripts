import requests as req
import json
import time as t
import queue

# import dataloss_prev from dataloss

def post_data(json_data, buggy_flag):

        # url = "http://localhost:3000/api/NewBuggy/"
        url = "http://localhost:3000/api/"
        headers = {'content-type': 'application/json'} 

        q = queue.Queue()

        ''' Receive json object '''
        ''' Receive New/Old Buggy flag'''

        # flag = 0        # whichever flag type is received
        buggy = 'NewBuggy'
        if buggy_flag:
                buggy = 'OldBuggy'

        url = url + buggy + '/'

        data_dict = json.loads(json_data)

        try:
                r = req.getAll()  
                if not q.empty():  
                        for i in range(q.qsize()):
                                d = q.get()  
                                req.post(url, data=d, headers=headers)
                else:
                        req.post(url, data=data_dict, headers=headers) 
                        t.sleep(3)
        except Exception:
                print("No connection! Queueing data...")
                q.put(data_dict)
                t.sleep(3)

''' ToDo: 
          -change script to data obj (instead of json)
          -add Everson's implementation
'''

# try:
#         resp = req.post(url, data=data_dict, headers=headers)
#         print(resp.status_code)
# except:
#         print(resp)

#         # Do something (data-loss algorithm?)
#         # dataloss_prev(data_dict, url, headers)