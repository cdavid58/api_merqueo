import json, requests

list_category = [
	"Irresistibles",
	"Frutas y Verduras","Lácteos y Huevos", "Arroz Granos Pastas", "Aceites, Sal y Endulzantes",
	"Despensa", "Sazonadores Salsas Sopas", "Congelados", "Cuidado de la Ropa", "Aseo del Hogar",
	"Cuidado Personal", "Bebés", "Saludables","Café, Té y Chocolate", "Pan, Arepas y Galletas",
	"Pasabocas y Mecatos","Bebidas", "Licores", "Mascotas"
]

list_subcategory = {
	"Irresistibles":[
		"Súper Ofertas","Imbatibles","Los del Ahorro","Más vendidos"
	],
	"Frutas y Verduras" : ["Frutas", "Verduras","Papa","Desgranados","Hierbas y Especias"],
	"Lácteos y Huevos" : ["Leches","Huevos","Mantequillas y Margarinas","Lácteos Saborizados","Lácteos con Adicionales",
					"Gelatinas","Cremas","Leche en polvo","Bebidas Vegetales"
				],
	"Arroz Granos Pastas":["Arroz","Granos","Pastas"],
	"Aceites, Sal y Endulzantes":["Aceites","Margarinas","Azucar","Panela","Endulzantes"],
	"Despensa":["Atunes y Sardinas","Enlatados y Conservas","Harinas","Mezclas Listas","Cereales"],
	"Sazonadores Salsas Sopas":[
		"Salsas y Vinagres","Sopas y Cremas","Bases","Caldos","Condimentos, Especias y Adobos"
	],
	"Congelados":[
		"Comidas Listas y Snacks","Paps y Yucas","Fruta Congelada","Verdura Congelada","Helados"
	],
	"Cuidado de la Ropa":[
		"Detergente Líquido","Detergente Polvo","Desmanchadores","Suavizantes","Jabón en Barra"
	],
	"Aseo del Hogar":[
		"Baño","Ambientadores","Lavaloza y Quitagrasa","Toallas de cocina, Servilletas y Paños",
		"Implementos de Limpieza", "Limpia Pisos","Limpieza de Superficies y Ceras",
		"Insecticidas","Bolsa, Desechables y Miscelánea","Desinfección"
	],
	"Cuidado Personal":[
		"Cuidado Bucal","Shampoo","Acondicionadores","Cremas para Peinar, Tratamientos y Gel",
		"Jabón","Desodorantes","Cremas Corporales","Talcos y Copitos","Afeitado y Depilación",
		"Cuidado Facial","Cuidado Íntimo","Protección Solar y Repelente","Coloración",
		"Maquillaje y Uñas", "Cuidado del Adulto"
	],
	"Bebés":[
		"Alimento para Bebé","Fórmulas Infantiles","Hora del Baño",
		"Humectación y Colonias","Pañales","Pañitos y Cremas Antipañalitis"
	],
	"Saludables":[
		"Alimentos Funcionales","Carnes Frias y Embutidos"
	],
	"Café, Té y Chocolate":[
		"Café Soluble","Café Molido","Chocolate de Mesa","Cápsulas y Complementos de Café",
		"Aromáticas e Infusiones","Té"
	],
	"Pan, Arepas y Galletas":[
		"Arepas","Galletas Saladas","Galletas Dulces","Tostadas y Hojaldres","Tortillas"
	],
	"Pasabocas y Mecatos":[
		"Papas","Mixtos","Snacks","Tortillas de Maíz","Platanitos","Crispetas","Maní, Nueces y Snacks",
		"Frutos Deshidratados"
	],
	"Bebidas":[
		"Gaseosas","Jugos y Néctares","Modificadores de Leche","Bebidas Vegetales","Té Líquido","Energizantes"
	],
	"Licores":[
		"Cervezas","Aguardiente","Ron","Whisky","Vodka","Ginebra","Vino Tinto","Vino Blanco","Otros Licores"
	],
	"Mascotas":[
		"Concentrado Gatos","Concentrado Perros","Snacks y Juguetes","Higiene de la Mascota",
		"Arena para Gatos","Alimento Húmedo Gatos"
	]
}

print(len(list_category))
print(len(list_subcategory))
n= 0
url = "http://localhost:9090/api/Create_SubCategory/"
# url = "http://localhost:9090/api/Create_Category/"

# for i in list_category:
# 	payload = json.dumps({
# 	  "name": i
# 	})
# 	headers = {
# 	  'Content-Type': 'application/json'
# 	}

# 	response = requests.request("POST", url, headers=headers, data=payload)
# 	print(response.text)


for i, j in list_subcategory.items():
	if i == list_category[n]:
		for x in j:
			print(i,' ',str(x))
			payload = json.dumps({
			  "category": i,
			  "subcategory": x.replace(' ','_')
			})
			headers = {
			  'Content-Type': 'application/json'
			}

			response = requests.request("POST", url, headers=headers, data=payload)
			print(response.text)
	else:
		print("No iguales",i)
	n += 1


