from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name="gallery"),
    path('category/<str:category_slug>/',views.gallery,name="gallery_category"),
    path('category/<str:category_slug>/<str:pk>/',views.photo,name="photo"),
    path('add_photo/',views.add_photo,name="add_photo"),
]
