# subfile.py
import os
import settings

# settings.init_settings()

def print_desde_modulo():
    print("Desde módulo")
    print(settings.usuario)
    print(settings.path_base)
    print(settings.hora)
    print(settings.host)
    print(os.path.basename(__file__))