from django.urls import path
from  . import views

app_name='blog'
urlpatterns = [
    path(r'', views.post_list, name='all_notes'),
    path('<int:id>', views.post_detail, name ='detail'),

]
