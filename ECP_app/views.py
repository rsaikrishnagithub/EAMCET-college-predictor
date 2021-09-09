from django.shortcuts import render

# Create your views here.
def homepage(request):
	if request.method == 'POST':
		rank=request.POST.get('rank')
		gender=request.POST.get('gender')
		caste=request.POST.get('caste')
		branch=request.POST.get('branch')
		
	return render(request,'homepagee.html')