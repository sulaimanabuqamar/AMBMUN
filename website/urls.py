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
    path("Editor/", views.Editor, name="editor"),
    path("listDir/", views.listDir, name="listdir"),
    path("getFile/", views.getFile, name="getfile"),
    path("writeTextFile/", views.writeTextFile, name="writetextfile"),
    path("deleteFile/", views.deleteFile, name="deleteFile"),
    path("uploadFile/", views.uploadFile, name="uploadFile"),
]