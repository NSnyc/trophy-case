from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about', views.about, name='about'),
  path('trophies/', views.trophy_index, name='trophy-index'),
  path('trophies/<int:trophy_id>/', views.trophy_detail, name='trophy-detail'),
  path('trophies/create/', views.TrophyCreate.as_view(), name='trophy-create'),
  path('trophies/<int:pk>/update/', views.TrophyUpdate.as_view(), name='trophy-update'),
  path('trophies/<int:pk>/delete/', views.TrophyDelete.as_view(), name='trophy-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]