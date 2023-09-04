from django.urls import path
from .views import list_tasks, create_task, update_task, delete_task, put_task


urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name='create_task'),
    path('update_task/<int:id>', update_task, name='update_task'),
    path('put_task/<int:id>/', put_task, name='put_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task')
]
