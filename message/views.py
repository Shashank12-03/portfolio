from django.shortcuts import render, HttpResponse

# Create your views here.
def show(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio-details.html')