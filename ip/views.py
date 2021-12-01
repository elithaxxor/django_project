#from . import IPCHECKER as IPx
import subprocess, traceback, os, time
from . import IPQUERY as IPq
from django.shortcuts import render
from django.http import HttpResponse
import sys, requests
from subprocess import PIPE, Popen, STDOUT, CalledProcessError
#from IPCHECKER import *
#from blog import IPCHECKER
from django.shortcuts import render
# from IPx import *
# Create your views here.


def IPhome(request):
    # context = {
    #     "title": "[Trigger Python Logic]"
    # }
    return render(request, "ip/home.html")

def IPabout(request):
    return render(request, "ip/about.html")

def IPsimple_function(request):
    print(),print()
    print('**[SAMPLE  FUNCTION (IP-PAGE)]**')
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

    return render(request, "ip/external.html", context)

def IPexternal(request):
    global e
    print('X' * 50)
    print('**[REQUEST]**')
    input = request.POST.get('param') ## grab the data 'param'
    print('[INPUT]', input)
    print(type(input))
    print('X' * 50)
    print(), print
    output = subprocess.run(
        [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py",
         input], shell=False, stdout=PIPE, text=True, check=True).stdout.decode()   # stdout=PIPE)
    print('X' * 50)
    print('[INPUT]', input)
    print('[OUTPUT]** ', output)
    IPcontext = {
        #"[F-Writer]": f,
        "[input]":input,
        "[output]":output,
        #"[lines]":lines
    }
    print()
    print('X' * 50)
    print('[CONTEXT]', IPcontext)
    return render(request, "ip/external.html",  IPcontext)



    #
    # try:
    #     with open('output.txt', 'a') as f:
    #         #output = subprocess.run([sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py", input], shell=False, stdin=f, capture_output=True, text=True, check=True)# stdout=PIPE)
    #        # output = subprocess.run([sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py", input],shell=True, stdin=f, stderr=STDOUT, text=True, check=True, stdout=PIPE)# stdout=PIPE)
    #         output = subprocess.run([sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py", input],shell=True, stdin=f, stderr=f, text=True, check=True, stdout=f)# stdout=PIPE)
    #         #output = subprocess.run([sys.executable, "/Users/adelal-aali/Documents/CS/PROJECT/django_pythonScripts01/blog/IPQUERY.py", input], shell=False, stdin=f, stderr=STDOUT, text=True, check=True, stdout=PIPE)
    #         f.writelines(str(output))
    #         print(), print()
    #         print('X' * 50)
    #         print('[OUTPUT]** ', output)
    #         print('[F]** ', f)
    #         print(), print()
    #
    #     print(), print()
    #     print('X' * 50)
    #     print('[INPUT]', input)
    #     print(type(input))
    #     print()
    #     print('[OUTPUT]: \n', output)
    #     print(type(output))
    #     print()
    #     print('[F-Writer] \n', f)
    #     print('X' * 50)
    #     print(), print()
    #     f.close()
    #
    #     with open('output.txt', 'r') as r:
    #         lines = r.readlines()
    #         print(lines)
    #         r.close()
    #     context = {
    #         "[F-Writer]": f,
    #         "[input]":input,
    #         "[output]":output,
    #         "[lines]":lines
    #     }
    # context = {
    #     #"[F-Writer]": f,
    #     "[input]":input,
    #     "[output]":output,
    #     #"[lines]":lines
    # }
    # print()
    # print('X' * 50)
    # print('[CONTEXT]', context)
    # return render(request, "blog/home.html", {'ip_data1':output}, context)

    # except subprocess.CalledProcessError as e:
    #     traceback.print_exc()
    #     raise RuntimeError("[command '{}' return with error (code {}): {}]".format(e.cmd, e.returncode, e.output))

    #return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") ## sennds user back to homepage
   # return HttpResponse(IPq) ## sennds user back to homepage
    #return HttpResponse(IPq) ## sennds user back to homepage
    #return HttpResponse(IPq) ## sennds user back to homepage



    # return render(request, "home/home.html", context)
