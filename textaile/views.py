# i created this file -sanket 

from django.http import HttpResponse
# code of video 6 exersise personal navigator
#def index(request):
    #f=open('1.txt','r')
    
    #return HttpResponse(f.read())
    
#def about(request):
   # return HttpResponse('''<h1> this is about page </h1><br> <a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'> code with harry django play list</a> <br> <button><a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>same link but in button</a></button>''')
    
    
    
  # code of video 6 exersise display text file content in html 
#def index(request):
    #f=open('1.txt','r')
    
   # return HttpResponse(f.read())
   
#def about(request):
    #return HttpResponse('''<h1> this is about page </h1><br> <a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'> code with harry django play list</a> <br> <button><a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>same link but in button</a></button>''')
    
    
    
    
def index(request):
    
    return HttpResponse('''home<br> <ol> <li><a href='/removepunk'>removepunk</a></li> <li><a href='/capitalizefirst'>capitalizefirst</a></li> <li><a href='/newlinermv'>newlinermv</a></li></ol>''')
   
def removepunk(request):
    
    return HttpResponse('''removepunk <a href='/'> </a> ''')
   
def capitalizefirst(request):
    
    return HttpResponse('''<h1>capitalizefirst <a href='/'> back</a> </h1>''')
   
def newlinermv(request):
    
    return HttpResponse('''<h1>newlinermv <a href='/'> back</a> </h1>''')
   
def spacermv(request):
    
    return HttpResponse('''spacermv <a href='/'> back</a>''')

def charcount(request):
    
    return HttpResponse('''charcount <a href='/'>back</a>''')
   
   
