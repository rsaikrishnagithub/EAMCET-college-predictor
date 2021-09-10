from django.urls import path,include
from . import views
urlpatterns = [
	path('',views.homepage,name='home'),
	path('colleges/',views.college_list,name='colleges'),
]