from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.home, name="home"),
    # path('', views.create_article, name='create_article'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    # path('recherche/', views.recherche_page_web_merde, name='recherche_page_web_merde'),   # replace 'desired_path' and 'search_web_page' accordingly
]


