from django.shortcuts import render
from . models import MovieInformation
from . forms import MovieForm

# Create your views here.
def create(request):
    frm=MovieForm()
    if request.POST:
       frm=MovieForm(request.POST)
       if frm.is_valid:
           frm.save()
    else:
           frm=MovieForm()   

    return render(request,'create.html',{'frm':frm})

def list(request):
     movie_set=MovieInformation.objects.all()
     print(movie_set)
     return render(request,'list.html',{'movies':movie_set}) ## values are passed by using dictionary


def edit(request):
    return render(request,'edit.html')
