from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json

# Create your views here.
def home(request):
    if 'sql' in request.GET:
        sql = request.GET['sql']
    elif 'sql' in request.POST:
        sql = request.POST['sql']
    else:
        sql = "SELECT 'HELLO RUNSQL!!'"
    rslt = _run_sql_(sql)
    jsonOBJ = json.dumps(rslt)
    
    return JsonResponse(jsonOBJ, safe=False)

def _run_sql_(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rslt = cursor.fetchall()
    return rslt