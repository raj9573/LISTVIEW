from django.shortcuts import render

# Create your views here.
from app.models import user


from django.views.generic import ListView





def lisst(request):
    UO  =  user.objects.all()
    return render(request,'show.html',{'UO':UO})



class StudentDetails(ListView):
    template_name='cbv_show.html'
    model = user
    context_object_name = 'UO'


