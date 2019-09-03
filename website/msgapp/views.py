#coding=utf-8   
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def msgproc(request):
    datalist = []
    if request.method == "POST":
        name = request.POST.get("name", None)
        phone = request.POST.get("phone", None)
        major = request.POST.get("major", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(name, phone,\
                            major, time.strftime("%Y-%m-%d %H:%M:%S")))
        return render(request,'succeed.html')
    if request.method == "GET":
        return render(request, "MsgSingleWeb.html", {"data":datalist})
