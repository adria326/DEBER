# Extraer las horas y minutos de la cadena
# Determinar si es AM o PM
# Salida: "1:45 PM"
def convertir_a_12_horas(hora_24):
    horas, minutos = map(int, hora_24.split(':'))
    
    if horas == 0:
        periodo = "AM"
        horas_12 = 12
    elif horas < 12:
        periodo = "AM"
        horas_12 = horas
    elif horas == 12:
        periodo = "PM"
        horas_12 = 12
    else:
        periodo = "PM"
        horas_12 = horas - 12
    
    # Formatear la salida en formato de 12 horas
    resultado = f"{horas_12}:{minutos:02d} {periodo}"
    return resultado

entrada = "13:45"
salida = convertir_a_12_horas(entrada)
print(salida)  