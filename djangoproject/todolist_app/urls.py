from todolist_app import views
from django.urls import path, include

urlpatterns =[
    path('', views.todolist, name='todolist'),
    path('delete_task/<task_id>',views.delete_task, name = 'delete_task'),
    path('edit_task/<task_id>',views.edit_task, name = 'edit_task'),
    path('pending_task/<task_id>',views.pending_task, name = 'pending_task'),
    path('complete_task/<task_id>',views.complete_task, name = 'complete_task'),
]