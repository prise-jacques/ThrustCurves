# ThrustCurves
 Student Project Report  
 *Jacques Bonfils 5821750  
 ESTACA 5th Year - Space (Advanced Launchers)*

## Overview
This project is a Python-based tool designed to visualize the thrust curves of rocket engines from .eng files.  
It provides a simple way to analyze engine performance data by plotting thrust vs. time.  
The end goal is to implement an interactive menu allowing users to :
- View a list of available engines.
- Select specific engines to plot.
- Choose between displaying curves in separate windows or on a single graph for direct comparison.

## Current Features
- Read .eng files : The program parses .eng files to extract thrust and time data.  
- Plot thrust curves : It generates plots for the selected engines.  

## Future Enhancements
1. Two display modes :
   - Separate windows : Each curve opens in its own plot window;
   - Single comparison graph : Multiple curves are overlaid on a single plot for easy comparison.
2. Interactive Menu :
    - Display list of available engines in the directory;
    - Let the user select which engines to plot via input;
    - Let the user select the display mode.

 
## Requirements and Preparation
1. Ensure you have the following Python libraries installed :
 - *`matplotlib`*  
    You can install it via : 
    ```bash
    pip install matplotlib 
    ```
2. Ensure you have downloaded the thrust curve files.  
You will find them in the file named *'ThrustCurves'*  
If you need more than the ones included, you can find them here :  https://www.thrustcurve.org/
3. Ensure you have modified the file path to your own current file location.

## Errors you might encounter
- When extracting the data:
  - Delete and re-download the file

- When adding engine files to the list :    
  - Check the path and name of the file  
  - Add a comma at the end of the previous line  
