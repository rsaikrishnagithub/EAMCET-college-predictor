from django.shortcuts import render
from .demo import *
import numpy
# import pandas as pd

# df=pd.read_csv('tseamcet.csv')
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def homepage(request):
	if request.method == 'POST':
		rank=int(request.POST.get('rank'))
		gender=str(request.POST.get('gender')) 
		caste=str(request.POST.get('caste'))
		branch=str(request.POST.get('branch'))

		print(rank,gender,caste,branch)
		val=predict(rank,gender,caste,branch)
		
		vals=val.to_numpy().tolist()
		# print(vals)
		context ={'values':vals}
		return render(request,'results.html',context=context)

	return render(request,'homepagee.html')

def college_list(request):
	res=list_of_colleges()
	context={'colleges':res}
	return render(request,'colleges_list.html',context)

def college_branch(request,pk):
	branch=branch_list(pk)
	fee=fees(pk)
	context={'branches':branch,'Name':pk,'fee':fee}
	return render(request,'college.html',context)