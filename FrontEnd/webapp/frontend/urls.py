from django.urls import path

from . import views
# Controladores
#from controllers import userController

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login_view, name = 'login_view'),
    # Administration
    path('user_new', views.add_user, name = 'user_new'),
    path('users', views.users, name = 'users'),
    path('setting', views.setting, name = 'setting'),
    path('resources', views.resources, name = 'resources'),
    path('resource_new', views.add_resource, name = 'resource_new'),
    path('categories', views.categories, name = 'categories'),
    path('category_new', views.add_category, name = 'category_new'),
    path('settings', views.settings, name = 'settings'),
    path('setting_new', views.add_setting, name = 'setting_new'),
    path('instances', views.instances, name = 'instances'),
    path('instance_new', views.add_instance, name = 'instance_new'),
    path('help', views.help, name = 'help'),
]