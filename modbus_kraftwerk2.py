import time
import random
from pyModbusTCP.client import ModbusClient

# Anfangssequenz
print("\nHerzlich Willkommen bei...")
time.sleep(2)
print("\033[94m")
print("  __  __  ____  _____  ____  _    _  _____   _  _______            ______ _________          ________ _____  _  __ ")
print(" |  \/  |/ __ \|  __ \|  _ \| |  | |/ ____| | |/ /  __ \     /\   |  ____|__   __\ \        / /  ____|  __ \| |/ / ")
print(" | \  / | |  | | |  | | |_) | |  | | (___   | ' /| |__) |   /  \  | |__     | |   \ \  /\  / /| |__  | |__) | ' /  ")
print(" | |\/| | |  | | |  | |  _ <| |  | |\___ \  |  < |  _  /   / /\ \ |  __|    | |    \ \/  \/ / |  __| |  _  /|  <   ")
print(" | |  | | |__| | |__| | |_) | |__| |____) | | . \| | \ \  / ____ \| |       | |     \  /\  /  | |____| | \ \| . \  ")
print(" |_|  |_|\____/|_____/|____/ \____/|_____/  |_|\_\_|  \_\/_/    \_\_|       |_|      \/  \/   |______|_|  \_\_|\_\ ")
print("  Version 1.0 von Nils Kruchem")
print("\033[0m")
time.sleep(1)

ip_address = input('Geben Sie die IPv4-Adresse des Modbus-Systems ein: ')
server_port = 502

lower_register = int(input('Untere Registeradresse eingeben: '))
upper_register = input('Obere Registeradresse eingeben (leer lassen, falls nur eine Adresse): ')
upper_register = int(upper_register) if upper_register else lower_register
print("")

def generate_realistic_value(register):
    # Definieren realistischer Wertebereiche für die verschiedenen Register
    if register == 1:  # Turbinendrehzahl
        return random.randint(1500, 3000)
    elif register == 2:  # Generator-Leistung
        return random.randint(20000, 60000)  # z.B. in kW
    elif register == 3:  # Kesseldruck
        return random.randint(150, 250)
    elif register == 4:  # Kesseltemperatur
        return random.randint(350, 500)
    elif register == 5:  # Generator-Spannung
        return random.randint(11000, 23000)
    elif register == 6:  # Generator-Stromstärke
        return random.randint(1000, 2000)
    elif register == 7:  # Kühlwassertemperatur
        return random.randint(70, 90)
    elif register == 8:  # Durchflussrate des Kühlwassers
        return random.randint(500, 800)
    elif register == 9:  # Status des Not-Aus-Schalters
        return random.randint(0, 1)
    elif register == 10:  # Status der Brandmeldeanlage
        return random.randint(0, 1)
    else:  # Für den Fall zusätzlicher Register (Leistungsfaktor)
        return random.randint(0, 120)

def describe_register_change(register, value):
    # Beschreibungen der Registeränderungen mit Einheiten
    if register == 1:
        return f"Turbinendrehzahl auf {value} Umdrehungen pro Minute gesetzt."
    elif register == 2:
        return f"Generator-Leistung auf {value} kW gesetzt."
    elif register == 3:
        return f"Kesseldruck auf {value} bar gesetzt."
    elif register == 4:
        return f"Kesseltemperatur auf {value} °C gesetzt."
    elif register == 5:
        return f"Generator-Spannung auf {value} V gesetzt."
    elif register == 6:
        return f"Generator-Stromstärke auf {value} A gesetzt."
    elif register == 7:
        return f"Kühlwassertemperatur auf {value} °C gesetzt."
    elif register == 8:
        return f"Durchflussrate des Kühlwassers auf {value} l/min gesetzt."
    elif register == 9:
        return f"Status des Not-Aus-Schalters auf {'aktiv' if value == 1 else 'inaktiv'} gesetzt."
    elif register == 10:
        return f"Status der Brandmeldeanlage auf {'Alarm' if value == 1 else 'normal'} gesetzt."
    else:
        return f"Leistungsfaktor auf {value} % gesetzt."

while True:
    client = ModbusClient(host=ip_address, port=server_port, auto_open=True)
    try:
        if client.open():
            print("Verbindung zum Modbus-Server erfolgreich.")
            
            # Alle Register initial mit einem realistischen Wert setzen
            for register in range(lower_register, upper_register + 1):
                value = generate_realistic_value(register)
                if client.write_single_register(register, value):
                    print(f"\033[92m{describe_register_change(register, value)}\033[0m")
                else:
                    print(f"\033[91mFehler beim Setzen von Register {register} auf {value}.\033[0m")

            # Endlosschleife: Alle 8 Sekunden ein zufälliges Register ändern
            while True:
                time.sleep(2)  # Kurze Pause nach dem Initialisieren der Register
                register = random.randint(lower_register, upper_register)
                value = generate_realistic_value(register)
                if client.write_single_register(register, value):
                    print(f"\033[92m{describe_register_change(register, value)}\033[0m")
                else:
                    print(f"\033[91mFehler beim Ändern von Register {register} auf {value}.\033[0m")
                time.sleep(8)  # 8 Sekunden warten nach jeder Registeränderung
        else:
            print("Verbindung zum Modbus-Server fehlgeschlagen.")
    except Exception as e:
        print(f"Modbus-Fehler: {e}")
    finally:
        client.close()
        print("Verbindung zum Modbus-Server getrennt. Neuer Verbindungsversuch in 5 Sekunden.")
        time.sleep(5)