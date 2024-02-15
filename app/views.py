from django.shortcuts import render

# Create your views here.
from app.models import user

from django.http import HttpResponse


from django.views.generic import ListView,DetailView,DeleteView

def lisst(request):
    UO  =  user.objects.all()
    return render(request,'show.html',{'UO':UO})





def users(request,pk):


    UO = user.objects.get(pk = pk)
    print(UO)

    return HttpResponse(UO)


def ids(request,value):

    return HttpResponse(value)


class StudentDetails(ListView):
    template_name='cbv_show.html'
    model = user
    context_object_name = 'UO'





class UserDetails(DetailView):

    template_name ='detailview.html'
    model = user
    context_object_name = 'UO'

def succcess(request):

    return render(request,'success.html')


class user_delete(DeleteView):
    template_name = 'user_delete.html'
    model = user
    success_url = '/succcess/'





