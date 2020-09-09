from django.urls import path
from .views import HomeView, EntryView, CreateEntryView, UpdateEntryView, DeleteEntryView

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry_detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'),
         name='create_entry'),
    path('entry/edit/<int:pk>/',
         UpdateEntryView.as_view(success_url='/'), name='update_entry'),
    path('entry/<int:pk>/delete/',
         DeleteEntryView.as_view(success_url='/'), name='delete_entry'),
]
