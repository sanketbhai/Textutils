# i created this file -sanket 

from django.http import HttpResponse

def index(request):
    f=open('1.txt','r')
    
    return HttpResponse(f.read())
    
def about(request):
    return HttpResponse('''<h1> this is about page </h1><br> <a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'> code with harry django play list</a> <br> <button><a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>same link but in button</a></button>''')