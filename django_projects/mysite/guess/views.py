from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.utils.html import escape

# def dump_data(place, data) :
#     retval = ""
#     if len(data) > 0 :
#         retval += '<p>Incoming '+place+' data:<br/>\n'
#         for key, value in data.items():
#             retval += escape(key) + '=' + escape(value) + '</br>\n'
#         retval += '</p>\n'
#     return retval


def check_guess(guess) :
    message = False
    if guess is not None:
        try:
            if int(guess) < 24 :
                message = 'Too low'
            elif int(guess) > 24 :
                message = 'Too high'
            else:
                message = 'Just Right'
        except:
            message = 'Bad format for guess:' + escape(guess)
    return message

def index(request):
    return render(request, 'guess/index.html')

def guess(request, guessvalue):
    message = check_guess(guessvalue)
    return render(request, 'guess/mainpage.html', { 'message' : message })
