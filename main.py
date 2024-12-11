import matplotlib.pyplot as plt

def read_eng_file(file_path):
    """
    Read a .eng file and extract the Time and Thrust data.
    Lire un fichier .eng et extraire les données de Temps et de Poussée.
    """
    times = []
    thrusts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignore the comments or empty lines
                # Ignorer les lignes de commentaires ou vides
                if line.startswith(";") or not line.strip():
                    continue
            
                # Extract the data (Time and Thrust)
                # Extraire les données (Temps et Poussée)
                try:
                    time, thrust = map(float, line.split()[:2])  # Les deux premières colonnes
                    times.append(time)
                    thrusts.append(thrust)
                except ValueError:
                    pass  # Ignore les lignes mal formatées
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' cannot be found")

    return times, thrusts


def plot_thrust_curve(times, thrusts, file_name):
    """
    Trace la courbe de poussée en fonction du temps.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(times, thrusts, label=f"Poussée ({file_name})", color="blue")
    plt.title(f"Courbe de poussée pour {file_name}")
    plt.xlabel("Temps (s)")
    plt.ylabel("Poussée (N)")
    plt.grid(True)
    plt.legend()


def main():
    """
    Main program to read multiple files and plot the graphs.
    Programme principal pour lire plusieurs fichiers et tracer les courbes.
    """
    # Creation of the engines' list
    # Création de la liste des moteurs
    file_paths = [
        # Be careful to change the path of the files on your machine
        "Thrust_Curves_List\PRO_98_6GXL_Red_Lightning.eng",
        "Thrust_Curves_List\PRO_98_4G_M795.eng"
        # Add other files above this line and a comma and the end of the previous line
    ]
    
    for file_path in file_paths:
        # Lire et parser les données
        times, thrusts = read_eng_file(file_path)

        # Vérifier que des données ont été extraites
        if not times or not thrusts:
            print(f"Error: the file '{file_path}' cannot be found or in the wrong format.")
            continue

        # Get the file name for the graph title
        file_name = file_path.split("/")[-1]

        # Configure the graph in a new window
        plot_thrust_curve(times, thrusts, file_name)

    # Show each graph in a different window
    plt.show()

if __name__ == "__main__":
    main()
