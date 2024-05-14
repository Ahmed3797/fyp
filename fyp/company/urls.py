from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
 path("",views.company.as_view(),name="company"),
 path("/create-interview",views.AddInterview.as_view(),name="create_interview"),
 path("/view/<id>",views.View_CVS.as_view(),name="cvs"),
 path('save_image/', views.save_image, name='save_image'),
 path("save_company_name/",views.save_company_name,name="save_company_name"),
 path("save_bio/",views.save_bio,name="save_bio"),
 path("/reports_view/<id>",views.Reports_view.as_view(),name="reports_view"),
 path("/reports/<id>",views.Reports.as_view(),name="reports")
    
]

