import requests as req
import json
import time as t
import queue

def post_data(json_data, buggy_flag: str, data_queue):

        url = "http://localhost:3000/api/"
        headers = {'content-type': 'application/json'} 

        url = url + buggy_flag + '/'

        data_dict = json.loads(json_data)

        try:
                r = req.getAll()  
                if not data_queue.empty():  
                        for i in range(data_queue.qsize()):
                                d = data_queue.get()  
                                req.post(url, data=d, headers=headers)
                else:
                        req.post(url, data=data_dict, headers=headers) 
                        t.sleep(3)
        except Exception:
                print("No connection! Queueing data...")
                data_queue.put(data_dict)
                t.sleep(3)
