from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello,name="hello"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('info/<mname>',views.info,name="info"),
    path('homedashboard',views.homedashboard,name="homedashboard"),
    path('about',views.about,name="about"),
    path('refund',views.refund,name="refund"),
    path('terms',views.terms,name="terms"),
    path('privacy',views.privacy,name="privacy"),
    path('showidpass',views.showidpass,name="showidpass"),
    path('profile',views.profile,name="profile"),
    path('register',views.register,name="register"),
    path('login',views.loginpage,name="login"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('regmatches',views.regmatches,name="regmatches"),
    path('registermatch/<mname>',views.register_match,name="registermatch"),
    path('contactus',views.contactus,name='contactus' ),
    path('success/<mname>' , views.success , name='success')
]