from django.urls import path,include
from . import views
urlpatterns = [
	path('',views.homepage,name='home'),
	path('colleges/',views.college_list,name='colleges'),
	path('college/<str:pk>/',views.college_branch,name='college_branch'),
]