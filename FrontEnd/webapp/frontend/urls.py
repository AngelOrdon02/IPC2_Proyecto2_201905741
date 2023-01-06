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
    path('users/<str:id>', views.del_user, name = 'user_del'),
    path('setting', views.setting, name = 'setting'),
    path('business', views.business, name = 'business'),
    path('business_new', views.add_business, name = 'business_new'),
    path('playlists', views.playlist, name = 'playlist'),
    path('songs', views.songs, name = 'songs'),
    # path('categories', views.categories, name = 'categories'),
    # path('category_new', views.add_category, name = 'category_new'),
    # path('settings', views.settings, name = 'settings'),
    # path('setting_new', views.add_setting, name = 'setting_new'),
    # path('instances', views.instances, name = 'instances'),
    # path('instance_new', views.add_instance, name = 'instance_new'),
    path('help', views.help, name = 'help'),
]