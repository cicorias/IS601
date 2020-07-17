from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='bake-index'),
    path('bake/', views.bake, name='bake-form'),
    path('bakeapi/', views.bakeapi, name='bake-form-api'),
    path('bakeapi/<int:item_id>/', views.bakeapidetail, name='bake-form-api-detail'),
    path('<int:item_id>/', views.detail, name='bake-detail'),
    #  path('(?P<item_id>[0-9]+)/$', views.detail, name='bake-detail')
]
