from django.urls import path
from producto import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('producto/',views.ProductoView.as_view(),name='producto'),
    path('producto/<int:p_id>',views.ProductoDetailView.as_view())
]