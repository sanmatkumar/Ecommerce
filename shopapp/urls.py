from django.urls import path
from shopapp import views

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login1,name='login'),
    path('logout/',views.hlogout,name='hlogout'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    
] 