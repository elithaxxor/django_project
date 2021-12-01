#from . import IPCHECKER as IPx
import subprocess, traceback, os, time
from . import IPQUERY as IPq
from django.shortcuts import render
from django.http import HttpResponse
import sys, requests
from subprocess import PIPE, Popen, STDOUT, CalledProcessError

#from IPCHECKER import *
#from blog import IPCHECKER



# from IPx import *

# Create your views here.
def home(request, *args, **kwargs):
    # context = {
    #     "title": "[Trigger Python Logic]"
    # }
    return render(request, "blog/home.html")

def button(request, *args, **kwargs):
    # context = {
    #     "title": "[Trigger Python Logic]"
    # }
    return render(request, "blog/home.html")

def about(request, *args, **kwargs):
    return render(request, "blog/about.html")

def simple_function(request, *args, **kwargs):
    print(),print()
    print('**[SAMPLE  FUNCTION -- MAIN-PAGE]**')
    print('X' * 50)
    ip_data = IPq.INFO ## save the IPq info in var, then parse to
    print(ip_data)
    print(IPq)
    print(type(IPq))
    print('X' * 50)
    print(),print()
    return render(request, "blog/home.html", {'ip_data':ip_data})

def external(request, *args, **kwargs):
    try:
        global e
        print('X' * 50)
        print('**[REQUEST-BLOG]**')
        uinput = request.POST.get('param') ## grab the data 'param'
        print('[INPUT-BLOG]', uinput)
        print(type(uinput))
        print('X' * 50)
        print(), print
        ## works best
        output_pipe = subprocess.run(
            [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py"],
            stdout=PIPE, stderr=PIPE, shell=False, check=True, text=True, input=f'{uinput}')  # , stdin=input))

        print(output_pipe)

        print('X' * 50)
        print('[INPUT-BLOG]', uinput)
        print('[OUTPUT-BLOG]** ', output_pipe)

        context = {
            #"[F-Writer]": f,
            "[input]":uinput,
            "ip_data1":output_pipe,
            #"[lines]":lines
        }
        print()
        print('X' * 50)
        print('[CONTEXT]', context)
        return render(request, "blog/home.html", {'ip_data1':output_pipe})

    except subprocess.CalledProcessError as e:
        traceback.print_exc()
        raise RuntimeError("[command '{}' return with error (code {}): {}]".format(e.cmd, e.returncode, e.output))
    except Exception as E:
        traceback.print_exc()
        print(str(E))




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
