from django.urls import path
from . import views

urlpatterns = [
    # path(url-path-to-access, views-file-location, name-for-html?)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('todos/', views.todos_index, name='todos'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todos'),
    path('todos/create/', views.TodoCreate.as_view(), name='todos_create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
]