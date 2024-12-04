
import requests
import json

class Dictionary_API_Class:
    def __init__(self, word:str):
        self.base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"  
        self.word = word
    
    def get_proc(self):
        query_url = self.base_url + self.word
        resp = requests.get(url=query_url)
        if resp.status_code == 200:
            #print (resp.text)
            result_json = json.loads(resp.text)
            # print (result_json[0])
            pron_url = result_json[0]["phonetics"][0]["audio"]
            print (pron_url)

            