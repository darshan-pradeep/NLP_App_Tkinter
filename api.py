import paralleldots
import os

api_key=os.environ['API_KEY']

class api_functions:
    def __init__(self):
        paralleldots.set_api_key(api_key)
    
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        # print(response)
        print_response=''
        for i in response['sentiment']:
            print_response=i+' : '+str(response['sentiment'][i])+'\n'+print_response
        return print_response
    
    def emotion_analysis(self,text):
        response=paralleldots.emotion(text)
        # print(response)
        print_response=''
        for i in response['emotion']:
            print_response=i+' : '+str(response['emotion'][i])+'\n'+print_response
        return print_response
    
    def ner(self,text):
        response=paralleldots.ner(text)
        # print(response)
        print_response=''
        for i in response['entities']:
            print_response='Name : '+i['name']+'  '+'Category : '+i['category']+'\n\n'+print_response
        return print_response