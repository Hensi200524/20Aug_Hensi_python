from django.shortcuts import render

count = 0
# Create your views here.
def index(request):
    global count
    count+=1
    return render(request,'index.html',{'cnt':count})
