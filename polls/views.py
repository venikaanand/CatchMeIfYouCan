
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count

from .models import SquirrelModel
from .forms import SquirrelUpdateForm, SquirrelAddForm,SquirrelAllForm


# Create your views here.

def squirrel_list(request):
	list_Sq = SquirrelModel.objects.all()
	context = {'squirrels': list_Sq}
	return render(request, 'polls/list_squirrel.html', context)


def squirrel_map(request):
	list_Sq = SquirrelModel.objects.all()
	context = {'squirrels': list_Sq}
	return render(request, 'polls/map.html', context)
	
def website_homepage(request):
    return render(request,'polls/homepagee.html')