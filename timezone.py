from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print('La Fecha actual de Bogotá:', bogota_date.strftime('%d/%m/%y, %H:%M:%S'))


mexico_city_timezone = pytz.timezone('America/Mexico_City')
mexico_city_date = datetime.now(mexico_city_timezone)
print('La Fecha actual de Mexico:', mexico_city_date.strftime('%d/%m/%y, %H:%M:%S'))

caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)
print('La Fecha actual de Caracas:', caracas_date.strftime('%d/%m/%y, %H:%M:%S'))


