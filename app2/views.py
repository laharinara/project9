from django.shortcuts import render

# Create your views here.
def page2(request):
    return render(request,'page2.html')
def page3(request):
    return render(request,'page3.html')