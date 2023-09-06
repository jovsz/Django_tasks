from django.urls import path
from .views import list_tasks, create_task, update_task, delete_task, put_task,signup, home


urlpatterns = [
    
    path('', home),
    path('signup/', signup),
    path('main/', list_tasks),
    path('main/new/', create_task, name='create_task'),
    path('main/update_task/<int:id>', update_task, name='update_task'),
    path('main/put_task/<int:id>/', put_task, name='put_task'),
    path('main/delete_task/<int:id>/', delete_task, name='delete_task')
    
]
