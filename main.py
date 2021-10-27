#main.py
import settings
import modulo
import time

# La inicialización de settings se hace en el main y no hace falta hacerla en el módulo. 

settings.init_settings()
settings.print_settings() 

time.sleep(10)
print('.............')
modulo.print_desde_modulo()
