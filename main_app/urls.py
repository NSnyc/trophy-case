from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('trophies/', views.trophy_index, name='trophy-index'),
  path('trophies/<int:trophy_id>/', views.trophy_detail, name='trophy-detail'),
  path('trophies/create/', views.TrophyCreate.as_view(), name='trophy-create')
]