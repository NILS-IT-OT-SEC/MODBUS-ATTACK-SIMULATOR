import time
from pyModbusTCP.client import ModbusClient

# Anfangssequenz
print("\nHerzlich Willkommen bei...")
time.sleep(2)
print("\033[38;5;206m")
print("   __  __  ____  _____  ____  _    _  _____ _  _______ _      _      ______ _____ ©  ")
print("  |  \/  |/ __ \|  __ \|  _ \| |  | |/ ____| |/ /_   _| |    | |    |  ____|  __ \   ")
print("  | \  / | |  | | |  | | |_) | |  | | (___ | ' /  | | | |    | |    | |__  | |__) |  ")
print("  | |\/| | |  | | |  | |  _ <| |  | |\___ \|  <   | | | |    | |    |  __| |  _  /   ")
print("  | |  | | |__| | |__| | |_) | |__| |____) | . \ _| |_| |____| |____| |____| | \ \   ")
print("  |_|  |_|\____/|_____/|____/ \____/|_____/|_|\_\_____|______|______|______|_|  \_\  ")
print("  Version 1.1 mit manueller IP-Adresseingabe von Nils Kruchem ")
print("\033[0m")
time.sleep(1)

ip_address = input('Geben Sie die IPv4-Adresse des Modbus-Systems ein: ')
server_port = 502

lower_register = int(input('Untere Registeradresse eingeben: '))
upper_register = input('Obere Registeradresse eingeben (leer lassen, falls nur eine Adresse): ')
upper_register = int(upper_register) if upper_register else lower_register

client = ModbusClient(host=ip_address, port=server_port, auto_open=True)

try:
    if client.open():
        print("Verbindung zum Modbus-Server erfolgreich.")
        while True:
            # Alle Register auf 4444 setzen
            for register in range(lower_register, upper_register + 1):
                if client.write_single_register(register, 4444):
                    print(f"Register {register} erfolgreich auf 4444 gesetzt.")
                else:
                    print(f"Fehler beim Setzen von Register {register} auf 4444.")
            time.sleep(0.1)  # Eine Sekunde warten

            # Alle Register auf 11 setzen
            for register in range(lower_register, upper_register + 1):
                if client.write_single_register(register, 1111):
                    print(f"Register {register} erfolgreich auf 1111 gesetzt.")
                else:
                    print(f"Fehler beim Setzen von Register {register} auf 1111.")
            time.sleep(0.1)  # Eine Sekunde warten
    else:
        print("Verbindung zum Modbus-Server fehlgeschlagen.")
except Exception as e:
    print(f"Modbus-Fehler: {e}")
finally:
    client.close()
    print("Verbindung zum Modbus-Server getrennt.")
