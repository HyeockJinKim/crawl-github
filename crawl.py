import json
import pickle
import ssl
import time
from urllib.request import Request, urlopen

topic_list = []
topic_dic = {}

def read_json(x):
    refer_head = 'http://www.google.com/'
    connection_head = 'keep-alive'
    user_head = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'
    head = 'application/vnd.github.mercy-preview+json'
    url = 'https://api.github.com/search/repositories?q=topic:'
    context = ssl._create_unverified_context()
    
    request = Request(url + x)
    request.add_header('User-Agent', user_head)
    request.add_header('referer', refer_head)
    request.add_header('Connection', connection_head)
    request.add_header('Accept', head)
    response = urlopen(request, context=context)
    topic_dic[x] = {}
    for data in json.load(response)['items']:
        for topic in data['topics']:
            is_in = False
            for top in topic_list:
                if topic in top:
                    is_in = True
            if not is_in:
                topic_list.append(topic)
            if topic not in topic_dic[x].keys():
                topic_dic[x][topic] = 1
            else:
                topic_dic[x][topic] = topic_dic[x][topic] + 1

    print(topic_dic[x])
    print('\n\n')


def crawl():
    for x in topic_list:
        time.sleep(6)
        print(x)
        try:
            read_json(x)
        except:
            pass


topic_list.append('tensorflow')

crawl()

with open('./crawl.bin', 'wb') as file:
    pickle.dump(topic_dic, file)
