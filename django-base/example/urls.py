from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='bake-index'),
    path('bake/', views.bake, name='bake-form'),
    path('<int:item_id>/', views.detail, name='bake-detail'),
    #  path('(?P<item_id>[0-9]+)/$', views.detail, name='bake-detail')
]
