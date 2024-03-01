from django.shortcuts import render, HttpResponse
from wsgiref.util import FileWrapper
from Portfolio import settings
import os
# Create your views here.
def show(request):
    return render(request,'index.html')

def portfolio_1(request):
    return render(request,'portfolio-details1.html')

def portfolio_2(request):
    return render(request,'portfolio-details2.html')

def download_pdf(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'media', 'Shashank_Joshi_resume.pdf')
    with open(file_path, 'rb') as file:
        content = FileWrapper(file)
        response = HttpResponse(content, content_type='application/pdf')
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'Shashank_Joshi_resume.pdf'
        return response