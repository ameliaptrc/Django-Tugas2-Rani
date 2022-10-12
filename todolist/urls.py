from django.urls import path
from todolist.views import *


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change-status/<int:id>', status, name='status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('json/',show_json_todolist,name='show_json_todolist'),
    path('show/json/',show_todolist_ajax,name='show_todolist_ajax'),
    path('add/',todolist_add,name='todolist_add')
]