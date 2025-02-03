import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from directories import create_directories
from barcodes import generate_itf14_barcode, generate_upc_barcode
import subprocess

# Function to open file dialog and get file path
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        main(file_path)

    subprocess.run(['/usr/bin/open', "/tmp/output"])

# Function to open Finder window
def open_finder_window():
    output_dir = os.path.join(os.getcwd(), 'output')
    subprocess.run(['open', output_dir])  # This opens the folder in Finder

def main(file_path):
    # cwd = os.getcwd()
    cwd = '/tmp'
    df = pd.read_excel(file_path)

    # Initialize variables to keep track of current category and sub-category
    current_category = None
    current_sub_category = None

    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():

        ##############################
        # Create Directory Structure #
        ##############################

        # Update category if the current row has a non-NaN value
        if pd.notna(row['Category']):
            current_category = row['Category']
            current_sub_category = None

        # Update sub-category if the current row has a non-NaN value
        if pd.notna(row['Sub Category']):
            current_sub_category = row['Sub Category']

        # Only create directories if both category and sub-category are valid
        if current_category and current_sub_category:
            print(f"Creating directories for Category: {current_category}, Sub-Category: {current_sub_category}")
            create_directories(current_category, current_sub_category)

        ##########################
        # Generate Case Barcodes #
        ##########################

        if pd.notna(row['Sales Code']) and pd.notna(row['ITF-14 (Case Code)']) and pd.notna(row['Case']):
            file_directory = f"{cwd}/output/{current_category}/{current_sub_category}"
            filename = f"{row['Sales Code']}-{row['Case']}-CASE"

            itfCode = int(row['ITF-14 (Case Code)'])

            generate_itf14_barcode(str(itfCode), file_directory, filename)

        ##########################
        # Generate EACH Barcodes #
        ##########################

        if pd.notna(row['Sales Code']) and pd.notna(row['GTIN-12 (U.P.C.) (Each  Code)']) and pd.notna(row['Each']):
            file_directory = f"{cwd}/output/{current_category}/{current_sub_category}"
            filename = f"{row['Sales Code']}-{row['Each']}-EACH"

            gtin12 = int(row['GTIN-12 (U.P.C.) (Each  Code)'])

            generate_upc_barcode(str(gtin12), file_directory, filename)
    
    open_finder_window()

# Tkinter UI setup
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open file dialog to select the Excel file
open_file_dialog()