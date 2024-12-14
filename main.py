import matplotlib.pyplot as plt

def read_eng_file(file_path):
    """
    Read a .eng file and extract the Time and Thrust data.
    """
    times = []
    thrusts = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignore the comments or empty lines
                if line.startswith(";") or not line.strip():
                    continue
            
                # Extract the data (Time and Thrust)
                try:
                    time, thrust = map(float, line.split()[:2])  # First two columns
                    times.append(time)
                    thrusts.append(thrust)
                except ValueError:
                    pass  # Ignore lines with wrong format
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' cannot be found")

    return times, thrusts


def plot_thrust_curve(times, thrusts, file_name, combined=False):
    """
    Plot the thrust curves as a function of time for the chosen display mode
    """
    if not combined: 
        # New graph window if not combined
        plt.figure(figsize=(8, 5))
    
    plt.plot(times, thrusts, label=f"Poussée ({file_name})")
    plt.title(f"Courbe de poussée pour {file_name}")
    plt.xlabel("Temps (s)")
    plt.ylabel("Poussée (N)")
    plt.grid(True)
    
    if combined: 
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
        "Thrust_Curves_List\PRO_94_4G_M1800.eng",
        "Thrust_Curves_List\PRO_94_4G_M6400.eng",
        # "Thrust_Curves_List\PRO_98_4G_M795.eng",
        # "Thrust_Curves_List\PRO_98_4G_M1790.eng",
        # "Thrust_Curves_List\PRO_98_5G_N2200.eng",
        # "Thrust_Curves_List\PRO_98_6G_N1975.eng",
        # "Thrust_Curves_List\PRO_98_6G_N2850.eng",
        # "Thrust_Curves_List\PRO_98_6G_N5600.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N1560.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N2540.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N2900.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N3400.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_Red_Lightning.eng"
            # Add other files above this line and a comma and the end of the previous line
    ]
    
    # Binary test : True for combined graphs, False for serapate graphs
    combined_plot = True     
        # Change the value to change display modes

    if combined_plot:
        plt.figure(figsize=(10, 6))
        plt.title("Combined Thrust Curves")

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
        plot_thrust_curve(times, thrusts, file_name, combined=combined_plot)

    if combined_plot:
        # Add the legend on the combined graph
        plt.legend()
        plt.grid(True)

    # Show each graph in a different window
    plt.show()

if __name__ == "__main__":
    main()
