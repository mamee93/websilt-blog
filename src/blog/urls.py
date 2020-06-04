from django.urls import path
from  . import views
name_app = 'blog'
app_name='blog'
urlpatterns = [
    path(r'', views.post_list, name='all_blog'),
    path('<str:slug>', views.post_detail, name ='detail'),

]
