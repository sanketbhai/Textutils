# i created this file -sanket 

from django.http import HttpResponse

def index(request):
    f=open('1.txt','r')
    
    return HttpResponse(f.read())
    
def about(request):
    return HttpResponse('<h1> this is about page </h1>')