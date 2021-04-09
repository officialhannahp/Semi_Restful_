from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.show),
    path('shows/new', views.new),
    path('shows/create', views. create),
    path('shows/<int:show_id>', views.show_info),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/destroy', views.destroy)
]