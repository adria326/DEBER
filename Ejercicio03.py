# Diccionario para convertir el nombre del mes en su número correspondiente
meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, 
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8, 
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

# Función para convertir la fecha
def convertir_fecha(fecha):
   
    fecha = fecha.replace(",", "")
    partes = fecha.split()
    
    # Obtener día, mes y año
    dia = int(partes[0])
    mes = partes[1]
    año = int(partes[2])
    
    mes_num = meses[mes]
    
    print(dia, mes_num, año)

# Entrada de ejemplo
fecha_entrada = "15, Febrero, 1989"
convertir_fecha(fecha_entrada)