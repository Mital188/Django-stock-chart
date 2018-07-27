from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import requests
# from stocks.utils import StockUtil
from django.views.decorators.csrf import csrf_exempt
from stockApp.settings import STOCKS_API_KEY,STOCKS_API_URL
import json


@csrf_exempt
def index(request):
    usr_msg = dict(success=False,
                   message='Send something from view')
    if request.method == 'POST':
        ajax_data = request.body.decode('utf-8')
        company = ajax_data.split('=')[1]
        print("ajax_data", ajax_data.split('=')[1])
        response = requests.get(STOCKS_API_URL+company+'.csv?api_key='+STOCKS_API_KEY)
        result = response.content #.decode('utf-8')
       
        with open('stocks/static/csvfile.csv','wb') as file:
            file.write(result)
        user_msg = dict(success = True, message=ajax_data)

        return JsonResponse(user_msg)
      
        
    if request.method == 'GET':
        response = requests.get(STOCKS_API_URL+'AAPL.csv?api_key='+STOCKS_API_KEY)
        result = response.content #.decode('utf-8')
        with open('stocks/static/csvfile.csv','wb') as file:
            file.write(result)
                # file.write('\n')

        return render(request,'stocks.html',{'stock_data' : result})
    return JsonResponse(usr_msg)