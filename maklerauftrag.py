# Definition einer Funktion, die die Fläche eines Rechtecks anhand seiner Länge und Breite berechnet

def rechnung_flaeche(laenge, breite): 
    return laenge * breite

# Hauptfunktion/ Gesamter Ablauf des Programms

def main():
    gesamtflaeche = 0
    raumanzahl = 0

    print("Wohnung betreten. Beginne mit der Messung der Räume.")

    # Schleife, bis keine weiteren Räume gemessen werden

    fortsetzen = True
    while fortsetzen:
        print("\nRaum betreten.")
        rechteckanzahl = int(input("Wie viele Rechtecke enthält dieser Raum? "))
        
        # Berechnung der Rechtecke

        raumflaeche = 0
        for i in range(rechteckanzahl):
            print(f"Rechteck {i+1}:")
            laenge_cm = float(input("Länge in cm (wird in m umgerechnet): "))
            breite_cm = float(input("Breite in cm (wird in m umgerechnet): "))
            laenge_m = laenge_cm  # 1 cm entspricht 1 m in unserer Annahme
            breite_m = breite_cm  # 1 cm entspricht 1 m in unserer Annahme
            raumflaeche += rechnung_flaeche(laenge_m, breite_m)
        
        print(f"Die Fläche des Raumes beträgt {raumflaeche:.2f} m^2.")
        gesamtflaeche += raumflaeche
        raumanzahl += 1

        fortsetzen = input("Gibt es noch weitere Räume zu messen? (ja/nein): ") == "ja"

    print(f"\nGesamtfläche der Wohnung beträgt: {gesamtflaeche:.2f} m^2.")
    print(f"Anzahl der gemessenen Räume: {raumanzahl}.")

    if raumanzahl > 0:
        durchschnittliche_raumgroesse = gesamtflaeche / raumanzahl
        print(f"Durchschnittliche Raumgröße: {durchschnittliche_raumgroesse:.2f} m^2.")
    else:
        print("Es wurden keine Räume gemessen.")
