import folium
from django.shortcuts import render
import folium
import geocoder


# Create your views here.
def base(request):
    return render(request,'base.html')
# pour le tableau de bord
def accueil(request):
    return render(request,'dashbord/accueil.html')
def location_bien(request):
    return render(request,'dashbord/location_bien.html')
def suivi_bien(request):
    return render(request,'dashbord/suivi_bien.html')

# Proprietaire
def bien_proprietaire(request):
     return render(request,'proprietaire/bien_proprietaire.html')

def bien_en_location(request):
    return render(request, 'proprietaire/bien_en_location.html')

def decharge_effectuer(request):
    return render(request, 'proprietaire/decharge_effectuer.html')
def caisse(request):
    return render(request, 'proprietaire/caisse.html')

# gestion des propretaires
def list_proprietaire(request):
    return render(request,'g-proprietaire/list-proprietaire.html')
def nouveau_list(request):
    location= geocoder.osm('Bankass')
    lat= location.lat
    lng = location.lng
    country = location.country

    m= folium.Map(location=[19, -12], zoom_start= 2)
    folium.Marker( [17.579758,  -3.998823], tooltip='click plus', popup='Mali').add_to(m)
    folium.Marker([lat, lng], tooltip='click plus', popup=country).add_to(m)
    m = m._repr_html_()
    context= {
        'm':m,
    }
    return render(request,'g-proprietaire/nouveau-liste.html',context)

# gestion des BIENS
def liste_bien(request):
    return render(request,'g-bien/list-des-bien.html')

def liste_detail_bien(request):
    return render(request,'g-bien/list-detail-bien.html')
def locataire(request):
    return render(request,'g-locataire/list-locataire.html')


