# -*- coding: utf-8 -*-
import geolite2
from geolite2 import geolite2
import subprocess, sys, os
from subprocess import PIPE, DEVNULL
import traceback
#import IPQUERY

try:
    print('X' * 50)
    print('X' * 50)
    print()
    uinput = '76.172.85.231'
    print(uinput)
    print(type(uinput))



    result = subprocess.run(
        [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py"], stdout=PIPE, stderr=PIPE, shell=False, check=True, text=True, input=f'{uinput}')  # , stdin=input))

    print(result)

    # output_pipe = subprocess.run(
    #     [sys.executable, '-c', r"//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py",
    #      str(uinput)], stdout=PIPE, stderr=PIPE, shell=False, check=True, text=True)
    # print(output_pipe)
    #
    #
    # # p = subprocess.Popen(
    # #     ['python3', "/Users/adelal-aali/Documents/CS/PROJECT/django_pythonScripts01/blog/IPQUERY.py", uinput], stdin=PIPE, stderr=PIPE, stdout=PIPE,
    # #     shell=False, text=True)  # .decode('utf-8')
    # # print(p)
    #
    # # output_capture = subprocess.run(
    # #     [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py",
    # #      uinput], capture_output=True, shell=True, text=True)
    # #
    # # print(output_capture)
    # # print('X' * 50)
    # # print('X' * 50)
    # # print()
    #
    #     ## works best
    # output_pipe = subprocess.run(
    #     [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py",
    #      uinput], stdout=PIPE, stderr=PIPE, shell=False, check=True, text=True)  # , stdin=input)
    # print(output_pipe)
    #
    #
    #
    # output_devnull = subprocess.run(
    #     [sys.executable, "//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py",
    #      uinput], shell=False, check=True, text=True, stdout=DEVNULL, stderr=DEVNULL)  # , stdin=input)
    #
    # print(output_devnull)
    # print('X' * 50)
    # print('X' * 50)
    # print()
    #
    # proc = subprocess.run(
    #     ["//Users//adelal-aali//Documents//CS/PROJECT//django_pythonScripts01//blog//IPQUERY.py", uinput],
    #     stdin=PIPE, stdout=PIPE, stderr=PIPE, check=True)
    # stdout_v, stderr_v, = proc.stdout, proc.stderr
    # # return_code = proc.return_code
    # print(stdout_v)
    # print(stderr_v)
    # print(return_code)
    # print('X' * 50)
    # print('X' * 50)


except subprocess.CalledProcessError as e:
    traceback.print_exc()
    raise RuntimeError("[command '{}' return with error (code {}): {}]".format(e.cmd, e.returncode, e.output))

except Exception as E:
    traceback.print_exc()
    print(str(E))

