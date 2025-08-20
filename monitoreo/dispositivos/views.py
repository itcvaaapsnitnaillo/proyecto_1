from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "dispositivos/inicio.html", {})

def panel_dispositivos(request):
    # La clave 'dispositivos' contiene una lista de diccionarios.
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    # La clave 'consumo_maximo' contiene un número entero.
    consumo_maximo = 100

    # Se crea el diccionario de contexto.
    contexto = {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo,
    }

    # Se pasa el diccionario a la plantilla.
    return render(request, "dispositivos/panel.html", contexto)

def mi_plantilla(request):
    datos = {"productos": [], "consumo_maximo": 100}
    productos = [
        {"producto": "Sensor Temperatura", "consumo": 50},
        {"producto": "Medidor Solar", "consumo": 120},
        {"producto": "Sensor Movimiento", "consumo": 30},
        {"producto": "Calefactor", "consumo": 200}
    ]
    for producto in productos:
        if producto["consumo"] <= 100:
            producto["estado"] = True
            datos["productos"].append(producto)
        else:
            producto["estado"] = False
            datos["productos"].append(producto)

    return render(request, "dispositivos/mi_primera_plantilla.html", datos)