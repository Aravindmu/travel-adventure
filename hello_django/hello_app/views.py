from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):

    movie_data ={'movies': [{
        'title':'Godfather',
        'year':1990,
        'sucess':False,
    },
    {
        'title':'God',
        'year':1999,
        'summary':'story of an underworld king',
        'sucess':False,
    },
    {
        'title':'father',
        'year':1998,
        'summary':'story of an underworld king',
        'sucess':False,
    },
    ]
    }
    return render(request,'hello.html',movie_data)
