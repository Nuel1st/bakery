from django.urls import path
from . import views

urlpatterns= [
    path('', views.home , name="home" ),
    path('about/', views.about , name="about" ),
    path('blog/', views.blog , name="blog" ),
    path('book/', views.book , name="book" ),
    path('contact/', views.contact , name="contact" ),
    path('event/', views.event , name="event" ),
    path('menu/', views.menu , name="menu" ),
    path('service/', views.service , name="service" ),
    path('team/', views.team , name="team" ),
    path('testimonial/', views.testimonial , name="testimonial" )
    
]