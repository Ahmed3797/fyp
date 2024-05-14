
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Home.as_view(),name="Home"),
    path('signup',views.signup.as_view(),name="signup"),
    path("login",views.Login.as_view(),name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("goto/",views.goto,name="goto"),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('candidate',include("candidate.urls")),
    path('company',include("company.urls")),
    
    
]

    

