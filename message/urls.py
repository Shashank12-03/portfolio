from . import views
from django.urls import path
urlpatterns = [
    path('',views.show,name='index'),
    path('portfolio-details/',views.portfolio,name='portfolio-details')
]
