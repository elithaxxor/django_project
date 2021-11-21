import requests
from django.shortcuts import render
from django.http import HttpResponse
from . import IPQUERY as IPq


def home(request):
    print('[HOME-PAGE-REQUEST ]')
    return HttpResponse('<h1>Homepage</h1>')



def simple_function(request, *args, **kwargs):
    print(),print()
    print('**[SAMPLE  FUNCTION (MAIN-PAGE)]**')
    print('X' * 50)
    ip_data = IPq.INFO ## save the IPq info in var, then parse to
    print(ip_data)
    print(IPq)
    print(type(IPq))
    print('X' * 50)
    print(),print()

    context = {
        'BLOG-IP':'[IP OUTPUT]\n',
        'IP-DATA':ip_data,
        'IPq-DATA':IPq
    }

    return render(request, "ip/external.html", {'ip_main':IPq})



# def home(request):
#     context = {
#         "title": "[Trigger Python Logic]"
#     }
#     return render(request, "home/home.html", context)

# def simple_function(request):
#     print('[SAMPLE FUNCTION]')
#     return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

# data = requests.get("https://regres.in/api/user")
# data = requests.get("https://regres.in/api/users")
# print(f'{data.status_code}')
# print(data.text)
