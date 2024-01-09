from django.urls import path
from website import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("Schedule/", views.Schedule, name="schedule"),
    path("Rules/", views.Rules, name="rules"),
    path("Schedule/", views.Schedule, name="schedule"),
    path("Committees/", views.Committees, name="committees"),
    path('Committees/<int:committee_id>/', views.Committee_Detail, name='committee_detail'),
    path("About/", views.About, name="about"),
    path("Contact/", views.Contact, name="contact"),    
    path("FAQ/", views.Faq, name="faq"),
]