import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox, Toplevel
import os


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


def create_graph_window(fig, title):
    """
    Create a Tkinter window with the graph and a return to menu button
    """
    graph_window = Toplevel()
    graph_window.title(title)

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    tk.Button(
        graph_window,
        text="Return to Menu",
        font=("Arial", 10),
        command=lambda: [graph_window.destroy(), launch_menu()],
    ).pack(pady=10)

# def plot_thrust_curve(times, thrusts, file_name):
#     """
#     Plot the thrust curves as a function of time for the chosen display mode
#     """
#     if not combined: 
#         # New graph window if not combined
#         plt.figure(figsize=(8, 5))
    
#     plt.plot(times, thrusts, label=f"Poussée ({file_name})")
#     # plt.title(f"Courbe de poussée pour {file_name}")
#     plt.xlabel("Temps (s)")
#     plt.ylabel("Poussée (N)")
#     plt.grid(True)
    
#     if combined: 
#         plt.legend()


def main(combined_plot):
    """
    Main program to read multiple files and plot the graphs.
    """
    # Creation of the engines' list
    file_paths = [
            # Be careful to change the path of the files on your machine
        "Thrust_Curves_List\PRO_94_4G_M1800.eng",
        "Thrust_Curves_List\PRO_94_4G_M6400.eng",
        "Thrust_Curves_List\PRO_98_4G_M795.eng",
        "Thrust_Curves_List\PRO_98_4G_M1790.eng",
        "Thrust_Curves_List\PRO_98_5G_N2200.eng",
        "Thrust_Curves_List\PRO_98_6G_N1975.eng",
        # "Thrust_Curves_List\PRO_98_6G_N2850.eng",
        # "Thrust_Curves_List\PRO_98_6G_N5600.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N1560.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N2540.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N2900.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_N3400.eng",
        # "Thrust_Curves_List\PRO_98_6GXL_Red_Lightning.eng"
            # Add other files above this line and a comma and the end of the previous line
    ]

    if combined_plot:
        # Combined graph figure
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title("Combined Thrust Curves")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Thrust (N)")
        ax.grid(True)

    for file_path in file_paths:
        # Lire et parser les données
        times, thrusts = read_eng_file(file_path)

        # Skip files with no valid data
        if not times or not thrusts:
            print(f"Error: the file '{file_path}' is empty or in the wrong format.")
            continue

        # Get the file name for the graph title
        file_name = os.path.basename(file_path)

        if combined_plot:
            # Plot on the combined figure
            ax.plot(times, thrusts, label=file_name)
        else:
            # Create a separate figure for each file
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.set_title("Thrust Curves: {file_name}")
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Thrust (N)")
            ax.grid(True)
            ax.legend()

            # Create a graph window for separate graphs
            create_graph_window(fig, f"Graph: {file_name}")

    if combined_plot:
        # Add the legend on the combined graph
        ax.legend()
        create_graph_window(fig, "Combined Graphs")


def launch_menu():
    """
    Display a menu with display mode choice options
    """
    def set_combined():
        root.destroy()
        main(combined_plot=True)

    def set_separate():
        root.destroy()
        main(combined_plot=False)

    root = tk.Tk()
    root.title("Thrust Curve Plotter - Choose Display Mode")

    tk.Label(
        root,
        text="Welcome to the Thrust Curve Plotter! \n Please choose the display mode:",
        font=("Arial", 12),
        pady=10,
    ).pack()

    tk.Button(
        root,
        text="Combined Graphs (Comparison Mode)",
        font=("Arial", 10),
        width=30,
        command=set_combined,
    ).pack(pady=10)

    tk.Button(
        root,
        text="Separate Graphs (Individual Mode)",
        font=("Arial", 10),
        width=30,
        command=set_separate,
    ).pack(pady=10)

    tk.Button(
        root,
        text="Exit",
        font=("Arial", 10),
        width=15,
        command=root.destroy,
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    launch_menu()
