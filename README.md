# ThrustCurves
 Student Project Report  
 *Jacques Bonfils 5821750  
 ESTACA 5th Year - Space (Advanced Launchers)*

## Overview
This project is a Python-based tool designed to visualize the thrust curves of rocket engines from `.eng` files.  
It provides a simple way to analyze engine performance data by plotting thrust vs. time.  

## Current Features
 - Read .eng files : The program parses .eng files to extract thrust and time data.  
- Plot thrust curves : It generates plots for the selected engines.
- Interactive Menu : 
    - Display list of available engines in the directory;
    - Let the user select which engines to plot via input;
    - Let the user select the display mode for visualization.
- Visualization Modes :
   - Separate plots : All selected curves are displayed on a single graph, allowing direct comparison.
   - Combined plots : Individual plots for each selected engine are displayed within a single window.

 
## Requirements and Preparation
1. Ensure you have the following Python libraries installed :
 - *`matplotlib`*  
    You can install it via : 
    ```bash
    pip install matplotlib 
    ```
 - *`tkinter`*  
    Built into Python for most distributions. No installation needed.
 - *`screeninfo`*  
    You can install it via : 
    ```bash
    pip install screeninfo 
    ```
2. Ensure you have downloaded the thrust curve files.  
You will find them in the file named *'ThrustCurves'*  
If you need more than the ones included, you can find them here :  https://www.thrustcurve.org/
3. Ensure you have modified the file path to your own current file location.

## How to use
1. Run the script :
Execute the Python script in your terminal or IDE.  
2. Select Engines :
A menu will display the list of available .eng files with checkboxes.  
Select the engines you want to analyze.
3. Choose Display Mode:
Combined Graph: Displays all selected thrust curves on one graph.
Separate Graphs: Displays each thrust curve on its own subplot within a single window.
4. View and Interact:
Use the "Back to Menu" button on the graph window to return to the main menu.

## Errors you might encounter
- When extracting the data:
  - Delete and re-download the file

- When adding engine files to the list :    
  - Check the path and name of the file  
  - Add a comma at the end of the previous line
 
## Future Enhancements (Planned)
- Support for additional file formats (e.g., .csv).
- Real-time zoom and pan functionality for graphs.
- Improved error handling and user feedback.
- Graph export options (e.g., .png, .pdf).
