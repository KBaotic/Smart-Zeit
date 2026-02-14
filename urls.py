from django.urls import path
from meine_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("registrieren", views.registrieren, name="registrieren"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("admin_antraege", views.admin_antraege, name="admin_antraege"),
    path("admin_benutzerverwaltung", views.admin_benutzerverwaltung, name="admin_benutzerverwaltung"),
    path("admin_modulverwaltung", views.admin_modulverwaltung, name="admin_modulverwaltung"),
    path("administrator_werden", views.administrator_werden, name="administrator_werden"),
    path("neuer_bericht", views.neuer_bericht, name="neuer_bericht"),
    path("profil", views.profil, name="profil"),
    path("vip_datenmanagement", views.vip_datenmanagement, name="vip_datenmanagement"),
    path("vip_werden", views.vip_werden, name="vip_werden"),
    path("zeituebersicht", views.zeituebersicht, name="zeituebersicht"),
    path('bericht_speichern', views.bericht_speichern, name='bericht_speichern'),
    path('bericht_loeschen/<int:index>/', views.bericht_loeschen, name='bericht_loeschen'),
    path('bericht_bearbeiten_<int:index>/', views.bericht_bearbeiten, name='bericht_bearbeiten'),
    path('antrag_genehmigen/<str:username>/', views.antrag_genehmigen, name='antrag_genehmigen'),
    path('antrag_ablehnen/<str:username>/', views.antrag_ablehnen, name='antrag_ablehnen'),
    path("modul_erstellen", views.modul_erstellen, name="modul_erstellen"),
    path("modul_loeschen/<str:modul_id>/", views.modul_loeschen, name="modul_loeschen"),
    path("benutzer_loeschen/<str:username>/", views.benutzer_loeschen, name="benutzer_loeschen"),
    path('export/json/', views.export_json, name='export_json'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/xml/', views.export_xml, name='export_xml'),
    path('import/', views.import_berichte, name='import_berichte'),
    path("cookie_hinweis_akzeptieren", views.cookie_hinweis_akzeptieren, name="cookie_hinweis_akzeptieren"),
]

urlpatterns += staticfiles_urlpatterns()







































































  





