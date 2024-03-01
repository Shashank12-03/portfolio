from . import views
from django.urls import path
urlpatterns = [
    path('',views.show,name='index'),
    path('portfolio-details1/',views.portfolio_1,name='portfolio-details1'),
    path('portfolio-details2/',views.portfolio_2,name='portfolio-details2'),
    path('view_pdf', views.view_pdf),
]
