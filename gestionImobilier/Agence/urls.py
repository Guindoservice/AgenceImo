from django.urls import path

from .views import base, accueil, suivi_bien, location_bien, bien_proprietaire, bien_en_location, decharge_effectuer, \
    caisse, list_proprietaire, nouveau_list, liste_detail_bien, liste_bien, locataire

urlpatterns=[
    path('',base, name="base"),
    path('accueil',accueil, name="accueil"),
    path('location_bien',location_bien, name="location_bien"),
    path('suivi_bien',suivi_bien, name="suivi_bien"),
    path('bien_proprietaire',bien_proprietaire, name="bien_proprietaire"),
    path('bien_en_location',bien_en_location, name="bien_en_location"),
    path('decharge_effectuer',decharge_effectuer, name="decharge_effectuer"),
    path('caisse',caisse, name="caisse"),
    path('list-proprietaire',list_proprietaire, name="list-proprietaire"),
    path('nouveau-liste',nouveau_list, name="nouveau-liste"),
    path('list-des-bien',liste_bien, name="list_des_bien"),
    path('list-detail-bien',liste_detail_bien, name="list_detail_bien"),
    path('list-locataire',locataire, name="list_locataire"),
]