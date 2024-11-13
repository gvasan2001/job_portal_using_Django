from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page URL
    path('company-login/', views.company_login, name='company_login'),
    path('company-register/' ,views.company_register, name='company_register')
,    path('user-login/', views.user_login, name='user_login'),
    path('user-register/' ,views.user_register, name='user_register'),
    path('admin-home', views.company_home,name='company_home'),
    path('company-add-job', views.add_job,name='add_job'),
    path('user-home', views.user_home,name='user_home'),
    path('view-job',views.view_job,name='view_job'),
    path('apply-job',views.apply_job,name='apply_job'),
     path('view-application', views.view_application, name='view_application'),
    path('schedule', views.shedule, name='shedule'),  # Ensure to include a trailing slash
    path('view-status', views.view_status, name='view_status')]
