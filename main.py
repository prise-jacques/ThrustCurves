import matplotlib.pyplot as plt

def read_eng_file(file_path):
    """
    Lit un fichier .eng et extrait les données de temps et de poussée.
    """
    times = []
    thrusts = []
    with open(file_path, 'r') as file:
        for line in file:
            # Ignorer les lignes de commentaires ou vides
            if line.startswith(";") or not line.strip():
                continue
            
            # Extraire les données (temps et poussée)
            try:
                time, thrust = map(float, line.split()[:2])  # Les deux premières colonnes
                times.append(time)
                thrusts.append(thrust)
            except ValueError:
                pass  # Ignore les lignes mal formatées

    return times, thrusts


def plot_thrust_curve(times, thrusts):
    """
    Trace la courbe de poussée en fonction du temps.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(times, thrusts, label="Poussée (N)", color="blue")
    plt.title("Courbe de poussée")
    plt.xlabel("Temps (s)")
    plt.ylabel("Poussée (N)")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    """
    Programme principal pour lire un fichier et tracer la courbe.
    """
    # Remplace "mon_fichier.eng" par le chemin vers ton fichier
    file_path = "PRO_98_6GXL_Red_Lightning.eng"  
    
    # Lire et parser les données
    times, thrusts = read_eng_file(file_path)

    # Vérifier que des données ont été extraites
    if not times or not thrusts:
        print("Erreur : fichier vide ou mal formaté.")
        return
    
    # Tracer la courbe
    plot_thrust_curve(times, thrusts)


if __name__ == "__main__":
    main()
