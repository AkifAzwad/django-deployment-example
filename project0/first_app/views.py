from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import AccessRecord
# from first_app.models import AccessRecord,Webpage,Topic
# Create your views here.



def index(request):

    acc_rec=AccessRecord.objects.order_by("date")
    
    my_dict={
        "access_records" : acc_rec, 
    }

    return render(request,"first_app/index.html",context=my_dict)


