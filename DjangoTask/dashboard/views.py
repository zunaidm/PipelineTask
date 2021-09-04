from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.db.models import Count
from .models import *
# Create your views here.


def home(request):
    last_ten_log = Log.objects.all().order_by('-id')[:10]
    category_wise_count = Log.objects.values('category').annotate(Count('category'))   
    date_time_count = Log.objects.values('date_time').annotate(Count('id'))
    date_count = {}
    for dt in date_time_count:
        date_count[dt['date_time'][:6]] = 0
    for dt in date_time_count:
        date_count[dt['date_time'][:6]] = date_count[dt['date_time'][:6]]+dt['id__count']
        #print(date_count)
    date_count_list = list(date_count.items())
    date_count_list.sort() 

    context= {
        'last_ten_log':last_ten_log,
        'category_wise_count':category_wise_count,
        'date_count_list':date_count_list
    }
    return render(request,'dashboard/dashboard.html',context)


