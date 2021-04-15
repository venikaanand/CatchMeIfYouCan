<<<<<<< HEAD

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count

from .models import SquirrelModel
from .forms import SquirrelUpdateForm, SquirrelAddForm,SquirrelAllForm


# Create your views here.

	
def website_homepage(request):
    return render(request,'polls/homepagee.html')
=======

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count

from .models import SquirrelModel
from .forms import SquirrelUpdateForm, SquirrelAddForm,SquirrelAllForm


# Create your views here.

def website_homepage(request):
    return render(request,'polls/homepagee.html')
	
>>>>>>> d4b35acf0fc875078ef573a2c8764e055609208a
