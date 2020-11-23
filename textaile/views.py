# i created this file -sanket 

from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    
    return render(request,'index.html')
    
 
     
   
def filter(request):
    
    length=''
    djtext=request.POST.get('text','default')
    
    capitalize=request.POST.get('capitalize','off')
    rmvpunctuation=request.POST.get('rmvpunctuation','off')
    newlineremove=request.POST.get('newlineremove','off')
    charcount=request.POST.get('charcount','off')
    spacermv=request.POST.get('spacermv','off')
    
    if capitalize=='on':
        c=''
        for char in djtext:
            c=c+char.upper()
        djtext=c
        
    if rmvpunctuation=='on':
        c=''
        pun=',/;:!-_@#$&\<>][}{~`|\><'
        for char  in djtext:
            if char not in pun:
                c=c+char
        djtext=c
    
    if newlineremove=='on':
        c=''
        for char in djtext:
            if char!='\n' and char!='\r':
                c+=char
        djtext=c
        
    if charcount=='on':
        length=str(len(djtext))
    
        
    if spacermv=='on':
        c=''
        for index ,char in enumerate(djtext):
            
            if not(djtext[index]==' ' and djtext[index+1]==" "):
                
                c+=char
            
        
        djtext=c
                
    dic ={'analizedtext':djtext,
            'length':length}
            
        
    return render(request,'analized.html',dic)
