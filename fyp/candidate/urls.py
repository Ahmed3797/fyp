
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.Candidate.as_view(),name="candidate"),
    path("search",views.Search.as_view(),name="search"),
    path('initial_data/', views.initial_data, name='initial_data'),
    path('add_skill/', views.add_skill_view, name='add_skill'),
    path('add_education/', views.add_education_view, name='add_education'),
    path('save_image/', views.save_image, name='save_cand_image'),
    path("save_desc",views.save_company_name,name="save_cand_desc"),
    path("save_bio/",views.save_bio,name="save_cand_bio"),
    path('/interview/',include("interview.urls"),)
    
    
]

