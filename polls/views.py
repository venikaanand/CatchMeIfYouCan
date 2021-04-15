
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
	list_Sq = SquirrelModel.objects.all()[:100]
	context = {'squirrels': list_Sq}
	return render(request, 'polls/map.html', context)
	
def website_homepage(request):
    return render(request,'polls/homepagee.html')
	
def squirrel_modify(request, squirrel_id):
	squirrel = get_object_or_404(SquirrelModel, Unique_Squirrel_ID=squirrel_id)
	if request.method=='POST':
		form = SquirrelUpdateForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelUpdateForm(instance=squirrel)
	context ={
		'form':form
			}
	return render(request, 'polls/edit.html', context)

def squirrel_details(request, squirrel_id):
	squirrel = get_object_or_404(SquirrelModel, Unique_Squirrel_ID=squirrel_id)
	if request.method=='POST':
		form = SquirrelAllForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelAllForm(instance=squirrel)
	context ={
		'form':form
			}
	return render(request, 'polls/details.html', context)
	
def squirrel_add(request):
	if request.method=='POST':
		form = SquirrelAddForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/')
	else:
		form = SquirrelAddForm()
	context ={
		'form':form
			}
	return render(request, 'polls/add_squirrel.html', context)

def squirrel_stats(request):
	list_Sq = SquirrelModel.objects.all()
	total_Sq = len(list_Sq)
	
	Sq_fur_color =list(list_Sq.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
	Sq_hectare =list(list_Sq.values_list('Hectare_Squirrel_Number').annotate(Count('Hectare_Squirrel_Number')))	
	Sq_loc = list(list_Sq.values_list('Location').annotate(Count('Location')))
	Sq_time = list(list_Sq.values_list('Shift').annotate(Count('Shift')))
	Sq_Agegroup = list(list_Sq.values_list('Age').annotate(Count('Age')))
	
	context = {'total_Sq': total_Sq,
		'Sq_fur_color': Sq_fur_color,
		'Sq_hectare': Sq_hectare,
		'Sq_loc': Sq_loc,
		'Sq_time': Sq_time,
		'Sq_Agegroup': Sq_Agegroup,
		}
	return render(request, 'polls/stats.html', context)