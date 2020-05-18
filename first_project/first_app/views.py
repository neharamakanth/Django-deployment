from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AcessRecord

# Create your views here.
def index(request):
#     my_dict={'insert_me':"I am from views.py and from first_App intex.html"}
     webpages_list=AcessRecord.objects.order_by('date')
     access_list={'access_records':webpages_list}
#     return render(request,'first_app/index.html',context=my_dict)
     return render(request,'first_app/index.html',context=access_list)
