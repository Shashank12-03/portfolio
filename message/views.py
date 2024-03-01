from django.shortcuts import render, HttpResponse
from wsgiref.util import FileWrapper
from Portfolio import settings
from django.http import FileResponse, Http404
import os
# Create your views here.
def show(request):
    return render(request,'index.html')

def portfolio_1(request):
    return render(request,'portfolio-details1.html')

def portfolio_2(request):
    return render(request,'portfolio-details2.html')

def view_pdf(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'media', 'Shashank_Joshi_resume.pdf')
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')  # Use content_type instead of mimetype
        response['Content-Disposition'] = 'inline; filename="Shashank_Joshi_resume.pdf"'  # Specify filename in quotes
        return response
    # try:
    #     return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
    # except FileNotFoundError:
    #     raise Http404()