from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    context: dict[str, str] = {
        "title": "Main page",
        "content": "Main page content",
        "list": [1, 2, 3, 4, 5],
        "dict": {"name": "John", "age": 30},
        'is_authenticated': True
        
    }
    
    return render(request, 'main/index.html', context)
  
  
def about(request):
    return HttpResponse("About page")
