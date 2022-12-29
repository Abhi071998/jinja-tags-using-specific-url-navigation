from django.shortcuts import render

# Create your views here.
def abhi(request):
    d={'name':'Abhi'}
    return render(request,'abhi.html',d)