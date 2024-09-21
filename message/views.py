from django.shortcuts import render
from wsgiref.util import FileWrapper
from Portfolio import settings
from django.http import FileResponse,HttpResponse, Http404,JsonResponse
import os
import json

# import urllib
import requests
# Create your views here.

def send_data(url):
    try:
        # url1 = 'https://leetcode-stats-api.herokuapp.com/Shashank_1203'
        response = requests.get(url)
        if response.status_code!=200:
            print("Request failed")
        data = response.json()
        return data
    except:
        return 

def show(request):
    data1 = send_data('https://leetcode-stats-api.herokuapp.com/Shashank_1203')
    leetcode_data = {
            'totalSolved' : data1.get('totalSolved'),
            'easySolved': data1.get('easySolved'), 
            'mediumSolved': data1.get('mediumSolved'),
            'hardSolved': data1.get('hardSolved'), 
            'acceptanceRate': data1.get('acceptanceRate'), 
            'ranking': data1.get('ranking'), 
            'reputation': data1.get('reputation'),
        }
    # print(leetcode_data)
    data2 = send_data("https://api.github.com/users/Shashank12-03")
    github_data = {
                'public_repos': data2.get('public_repos'),
                'public_gists': data2.get('public_gists'),
                'followers': data2.get('followers'),
                'following': data2.get('following'),
            }
    # print(github_data)
    return render(request, 'index.html',{'leetcode_data':leetcode_data,'github_data':github_data})

def dashboard(request):
    data1 = send_data('https://leetcode-stats-api.herokuapp.com/Shashank_1203')
    leetcode_data = {
            'totalSolved' : data1.get('totalSolved'),
            'easySolved': data1.get('easySolved'), 
            'mediumSolved': data1.get('mediumSolved'),
            'hardSolved': data1.get('hardSolved'), 
            'acceptanceRate': data1.get('acceptanceRate'), 
            'ranking': data1.get('ranking'), 
            'reputation': data1.get('reputation'),
        }
    print(leetcode_data)
    data2 = send_data("https://api.github.com/users/Shashank12-03")
    github_data = {
                'public_repos': data2.get('public_repos'),
                'public_gists': data2.get('public_gists'),
                'followers': data2.get('followers'),
                'following': data2.get('following'),
            }
    print(github_data)
    return JsonResponse({'leetcode_data':leetcode_data,'github_data':github_data})

def portfolio_1(request):
    return render(request,'portfolio-details1.html')

def portfolio_2(request):
    return render(request,'portfolio-details2.html')

def view_pdf(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'media', 'Shashank_Joshi_resume.pdf')
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')  # Use content_type instead of mimetype
        response['Content-Disposition'] = 'inline; filename="Shashank_Joshi_resume.pdf"'  # Specify filename in quotes
        return response
    # try:
    #     return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
    # except FileNotFoundError:
    #     raise Http404()
    
