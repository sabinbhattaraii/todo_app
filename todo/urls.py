from django.urls import path
from .views import ( 
                TodoListView,
                TodoDetailView,
                TodoCreateView,
                TodoUpdateView,
                TodoDeleteView,
                )


urlpatterns = [
    path('',TodoListView.as_view(),name='home'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='detail'),
    path('todo/create/',TodoCreateView.as_view(),name="todo_new"),
    path('todo/<int:pk>/edit/',TodoUpdateView.as_view(),name='todo_edit'),
    path('todo/<int:pk>/delete/',TodoDeleteView.as_view(),name='todo_delete')
]
