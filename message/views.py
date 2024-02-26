from django.shortcuts import render, HttpResponse
from wsgiref.util import FileWrapper
import os
# Create your views here.
def show(request):
    return render(request,'index.html')

def portfolio_1(request):
    return render(request,'portfolio-details1.html')

def portfolio_2(request):
    return render(request,'portfolio-details2.html')

def download_pdf(request):
    filename = 'D:\shashank\documents\Shashank_Joshi_resume.pdf'
    # Open the file in binary mode
    with open(filename, 'rb') as file:
        content = FileWrapper(file)
        response = HttpResponse(content, content_type='application/pdf')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'Shashank_Joshi_resume.pdf'
        return response