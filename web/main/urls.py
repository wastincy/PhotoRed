from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('editor', views.editor),
    path('cap', views.capture),
    path('filters1', views.filters1),
    path('filters2', views.filters2),
    path('filters3', views.filters3),
    path('filters4', views.filters4),
    path('filters5', views.filters5),
    path('filters6', views.filters6),
    path('filters7', views.filters7),
    path('filters8', views.filters8),
    path('filters9', views.filters9),
    path('filters10', views.filters10),
    path('filters11', views.filters11),
    path('filters12', views.filters12),
    path('download', views.download),
]
