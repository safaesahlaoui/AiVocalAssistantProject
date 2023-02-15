import  requests
from apiKey import *

api_adress ='https://newsapi.org/v2/everything?q=Apple&from=2023-02-06&sortBy=popularity&apiKey='+key
api_adress2 ='http://newsapi.org/v2/top-headlines?country=us&apikey='+key
json_data=requests.get(api_adress2).json()
ar=[]
def news():
    for i in range(3):
        ar.append('Number '+str(i+1)+json_data['articles'][i]['title']+".")
        return ar



#arr=news()
#print(arr[i])