import csv

# Constantes des masses atomiques (en g/mol)
MASSE_CARBONE = 12.0107
MASSE_HYDROGENE = 1.00794
MASSE_CHLORE = 35.453

def calculer_ratio(nombre_chlore, nombre_carbone):
    nombre_hydrogene = 2 * nombre_carbone + 2 - nombre_chlore
    masse_chlore_totale = MASSE_CHLORE * nombre_chlore
    masse_carbone_totale = MASSE_CARBONE * nombre_carbone
    masse_hydrogene_totale = MASSE_HYDROGENE * nombre_hydrogene
    numerateur = masse_chlore_totale
    denominateur = masse_carbone_totale + masse_hydrogene_totale + masse_chlore_totale
    return numerateur / denominateur

# Plage des valeurs de chlore et de carbone
plage_chlore = range(3, 31)
plage_carbone = range(6, 37)

# Création du fichier CSV
with open('matrice_chlore_carbone.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    
    # Écrire l'en-tête
    header = ["Nombre de Carbone / Nombre de Chlore"] + [f"Cl{nombre_chlore}" for nombre_chlore in plage_chlore]
    writer.writerow(header)
    
    # Écrire les lignes de la matrice
    for nombre_carbone in plage_carbone:
        ligne = [f"C{nombre_carbone}"]
        for nombre_chlore in plage_chlore:
            ratio = calculer_ratio(nombre_chlore, nombre_carbone)
            ligne.append(ratio)
        writer.writerow(ligne)

print("Le fichier CSV 'matrice_chlore_carbone.csv' a été généré avec succès.")
