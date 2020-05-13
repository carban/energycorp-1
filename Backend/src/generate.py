import json
import random
import math
import geopy.distance
from geopy.geocoders import Nominatim
from django.contrib.auth.hashers import make_password

#========================== generate clientes ================================
a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
trans = str.maketrans(a,b)
names= [
    "Shamika Voces Ferrero",
    "Kiova Baz Badiola",
    "Cristóbal Cero Buedo",
    "Cecilia Urquijo Barma",
    "Teófilo Egusquiza Madariaga",
    "Nayelli Orbiz Espinosa",
    "Pancracio Ispuzua Chave",
    "Begsaida Cora Balpuesta",
    "Celeste Ganzo Vicente",
    "Luis Valino Vango",
    "Florencia Cucho Ahedo",
    "Nicomedes Monteagudo Ceniceros",
    "Stephanie Ludueña Gavilanes",
    "Mariano Mogrovejo Gante",
    "Maixa Troncoso Mazuelas",
    "América Olar Narganes",
    "Angélica Ter Tosantos",
    "Tzuruhan Berrueta Egusquiza",
    "Antonio Incera Fontoria",
    "Lupita Soret Garmendia",
    "Sayana Villarruel Saga",
    "Laila Herriaga Herreria",
    "Leví Encinas Durana",
    "Wendy Brena Suane",
    "Celia Malmonje Buyeres",
    "Reinaldo Maja Matuta",
    "Telesforo Rico Colombres",
    "Leonela Suane Ayuso",
    "Mariela Brasa Collazos",
    "Patricia Sesmilo Aranda",
    "Ataulfo Pañalosa Lera",
    "Maribel Urizar Castañiza",
    "Aleyda Valverde Villena",
    "Orsini Baraña Soret",
    "Erinelva Revuelta Ribero",
    "Nayade Artadi Urquijo",
    "Adam Idigoras Faes",
    "Máximo Corrales Balaunde",
    "Isaí Hita Carrera",
    "Juan Forcelledo Bodes",
    "Nicole Rioz Millares",
    "Yasnin Cedron Grandas",
    "Yosniel Estancion Cospedal",
    "América Rayon Sereno",
    "Viannette Orodea Rebellon",
    "Adelaida Carces Surco",
    "Danila Torienzo Piñeiros",
    "Jordana Charlo Jara",
    "Visitación Machicao Gañona",
    "Felisa Senabres Brochero",
    "Pamela Briñas Telego",
    "Yamila Vizcaya Arbaiza",
    "Ibar Escobar Verdeces",
    "Jeronimo Villarragut Bullido",
    "Yadel Herreria Atienza",
    "Pía Manzanedo Pedrueza",
    "Salomé Lejobeitia Courel",
    "Marlon Avalos Marentos",
    "Frida Ciaño Esqueira",
    "Amanda Marote Mortal",
    "Erlantz Bocinos Pierredonda",
    "Mariela Pablo Palma",
    "Marina Hernaez Iñarra",
    "Leonela Azcoitia Poladura",
    "Bruk Hoz Osaviaga",
    "Nerea Zuya Anderica",
    "Wenceslao Verga Maria",
    "Nieves Estua Galdia",
    "Rodame Paredes Cotarelo",
    "Lisbeth Riesgo Riguera",
    "Faustino Candolias Jalon",
    "Argelia Cifontes Lasarte",
    "Aaron Davila Landeta",
    "Willy Jubitero Ayarza",
    "Sabine Taran Inguanzo",
    "Bradley Bispo Valdecañas",
    "Natali Chumacero Folgar",
    "Ubaldo Cavallosa Rioseco",
    "Lasset Santotis Bernabeytia",
    "Jacinto Tablares Pico",
    "Aique Monterrey Ordoñez",
    "Carmela Catalan Roman",
    "Eugenio Arindez Cruz",
    "Adrián Villajane Porlier",
    "Sabrina Argandoña Agudo",
    "Crispín Corneja Argos",
    "Joel Espantoso Duran",
    "Gilda Alcivia Rubio",
    "Odaliz Curro Marote",
    "Jade Vidaurre Negro",
    "Ricardo Briceño Marcha",
    "Irmin Lordaliego Ruales",
    "Naylu Amilburu Angeriz",
    "Yadira Villamediana Toro",
    "Sabrina Mancobo Barcaiztegui",
    "David Nurueña Pizaño",
    "Elo San Tros",
    "Vladimir Iruz Urquioja",
    "Silvia Cardeiro Olavarria"
]

barrios =[
    'Aguablanca',
    'Belen',
    'Calipso',
    'Calima',
    'Eduardo Santos',
    'El vergel',
    'Sindical',
    'Manuela Beltran',
    'Potrero Grande',
    'Llano verde',
    'Mojica',
    'Marroquin',
    'El Retiro',
    'El vallado',
    'El bronx',  
    'Los Robles'  
]

ncalle = [
    'Calle',
    'Carrera',
    'Transversal',
    'Diagonal',
    'Avenida',
]

nncalle = ['A', 'B', 'C', 'D', 'E']
mails = ['gmail', 'yahoo', 'hotmail']
users = []
clients= []
for i in range (4,10):
    name = names[i]
    fname = name.split()[0].translate(trans)
    user ={
        "model": "users.CustomUser",
        "pk": i,
        "fields": {
            "id_user": str(random.randint(111111111,1144999999)),
            "name": name,
            "email": fname + "@"+random.choice(mails)+".com",
            "password": make_password(fname + str(len(fname))),
            "phone": str(random.randint(3000000,4999999)),
            "address": random.choice(ncalle) +" "+ str(random.randint(1,99)) + random.choice(nncalle) + " # " + str(random.randint(1,99)) + " - " + str(random.randint(10,200)),
            "neighborhood": random.choice(barrios),
            "stratus": random.randint(2,6),
            "is_active": True,
            "is_staff": False,
            "is_superuser": False    
        }
    }
    client ={
        "model": "users.Client",
        "pk": i,
        "fields": {
            "user": i,
            "user_type": 1
        }
    }    
    users.append(user)
    clients.append(client)
users.extend(clients)

#============================== energytrasfer ======================
subcoor = [
    [3.372908, -76.532479], 
    [3.428119, -76.479726],
    [3.425783, -76.508505],
    [3.456173, -76.532861],
    [3.467536, -76.495797]
]
substations = []
for i in range (1,len(subcoor)+1):
    substation = {
        "model": "energytransfers.substation",
        "pk": i,
        "fields": {
            "latitudeSubstation": str(subcoor[i-1][0]),
            "lengthSubstation": str(subcoor[i-1][1]),
            "is_active": True
        }
    }
    substations.append(substation)
    

transcoor = [
    [3.395716, -76.548220], 
    [3.380439, -76.544490],
    [3.426220, -76.480782],
    [3.418405, -76.471679],
    [3.427807, -76.500480],
    [3.433637, -76.504623],
    [3.448340, -76.538648],
    [3.448628, -76.523636],
    [3.465657, -76.500669],
    [3.484713, -76.497644]
]
ransformators = []
number = 1
for i in range (1,len(transcoor)+1):
    transformator = {
        "model": "energytransfers.transformator",
        "pk": i,
        "fields": {
            "latitudeTransformator": str(transcoor[i-1][0]),
            "lengthTransformator": str(transcoor[i-1][1]),
            "is_active": True,
            "substationTransformator": math.ceil(i/2)
        }
    }
    ransformators.append(transformator)


countercoors = [
    #transf 1
    [3.429708, -76.501172],
    [3.429556, -76.504896],
    [3.428764, -76.506723],
    [3.430769, -76.508757],
    [3.437480, -76.508385],

    #transf2
    [3.470128, -76.490096],
    [3.462938, -76.504564],
    [3.459106, -76.487694],
    [3.475513, -76.501320],
    [3.471357, -76.498292]
]

countdir = [
    'Cra. 28c #50-2 a 50-178',
    'Tv. 33g #28e-2 a 28e-64',
    'Dg. 28d #29-2 a 29-96',
    'Tv. 28a #27a-89 a 27a-1',
    'Cl. 33f #23-12 a 23-64',

    'Cl. 64a #2d-39 a 2d-1',
    'Cl. 46 #4b-8 a 4b-28',
    'Cra. 7f #64-65 a 64-1',
    'Cra. 1B #5450',
    'Cra. 1d 2 #56-94'
]
counters = []

for i in range (4, 14):
    number = 1
    if i > 8:
        number = 2
    counter = {
        "model": "energytransfers.counter",
        "pk": i-3,
        "fields": {
            "latitudeCounter": str(countercoors[i-4][0]),
            "lengthCounter": str(countercoors[i-4][1]),
            "counter": random.randint(30, 50),
            "is_active": True,
            "addressCounter": countdir[i-4],
            "clientCounter": i,
            "transformatorCounter": number
        }
    }
    counters.append(counter)

"""
geolocator = Nominatim(user_agent="geogenerator")
for i in range (len(countercoors)):
    location = geolocator.reverse(countercoors[i])
    print(location.address)
"""
"""
coors3 = (3.471357, -76.498292)
for i in range (len(transcoor)):
    print (geopy.distance.vincenty(tuple(transcoor[i]), coors3).km)
"""



jsonData=json.dumps(counters, ensure_ascii=False)



print(jsonData)

#========================== FIN generate clientes ================================
