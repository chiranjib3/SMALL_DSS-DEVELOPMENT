import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import re
import numpy as np

# Function to check if values match the criteria


def check_values(land_use,slope,surface_texture,soil_depth):
    land_use=' '.join(str(land_use).lower().split())
    slope=' '.join(str(slope).lower().split())
    surface_texture=' '.join(str(surface_texture).lower().split())
    soil_depth=' '.join(str(soil_depth).lower().split())


    

# Non arable
    if ("dense forest" in land_use.split(",") or"open forest" in land_use.split(",") or "scrub lands" in land_use.split(",") or "waste lands" in land_use.split(",")) and ("moderately steeply sloping" in slope.split(",") or "steeply sloping" in slope.split(",") or "strongly sloping" in slope.split(",")) and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or"sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",") or "moderately shallow"in soil_depth.split(",")):
        return "Staggered Trench"
         
    
    if ("dense forest" in land_use.split(",") or"open forest" in land_use.split(",") or "scrub lands" in land_use.split(",") or "waste lands" in land_use.split(",")) and ("gently sloping" in slope.split(",") or"moderately sloping" in slope.split(",") or"moderately steeply sloping" in slope.split(",") or "steeply sloping" in slope.split(",") or "strongly sloping" in slope.split(",") or "very gently sloping" in slope.split(",")) and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or"sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and soil_depth =="very shallow" :
        return "Stone Bunding"
    
    if ("dense forest" in land_use.split(",") or "open forest" in land_use.split(",") or "scrub lands" in land_use.split(",") or "waste lands" in land_use.split(",")) and ("moderately sloping" in slope.split(",") or "gently sloping" in slope.split(",") or "very gently sloping" in slope.split(",")) and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or"sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",")):
        return "Trench cum bund"
    
# Arable
    if land_use=="arable lands" and ("moderately steeply sloping" in slope.split(",") or "steeply sloping" in slope.split(",") or "strongly sloping" in slope.split(",")) and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or"sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or"moderately deep" in soil_depth.split(",") or "very shallow"in soil_depth.split(",")):
      return "Terrace"
    
    if land_use =="arable lands" and (slope =="moderately sloping") and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",") or "very shallow"in soil_depth.split(",")):
      return "Gradded bund"
    
    if land_use =="arable lands" and (slope =="gently sloping") and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",") or "very shallow"in soil_depth.split(",")):
      return "Trench cum bund"
    
    if land_use =="arable lands" and (slope =="very gently sloping") and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",") or "very shallow"in soil_depth.split(",")):
      return "Field bunding"
    
    if land_use =="arable lands" and ("gently sloping" in slope.split(",") or"moderately sloping" in slope.split(",") or"moderately steeply sloping" in slope.split(",") or "steeply sloping" in slope.split(",") or "strongly sloping" in slope.split(",") or "very gently sloping" in slope.split(","))  and ("sand" in surface_texture.split(",") or"loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or"slit loam" in surface_texture.split(",") or"sandy clay loam" in surface_texture.split(",") or"clay loam" in surface_texture.split(",") or"silt clay loam" in surface_texture.split(",") or"sandy clay" in surface_texture.split(",") or"silty clay" in surface_texture.split(",") or"clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and ("shallow" in soil_depth.split(",") or "deep" in soil_depth.split(",") or "moderately deep" in soil_depth.split(",") or "very shallow"in soil_depth.split(",")):
      return "Strengthning of Bund"


    else:
        return "No match found" 
    
    
    
# Function to handle file upload and processing 
def process_file():
    # Open file dialog to select Excel file 
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    # Read Excel file into pandas ExcelFile object
    excel_file = pd.ExcelFile(file_path)
    
    # Create empty list to store output dataframes for each sheet
    output_dfs = []
    
    # Loop through all sheet names in Excel file
    for sheet_name in excel_file.sheet_names:  
        # Read sheet into pandas DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_name)


                # Check for column names in different cases
        if "land use" not in df.columns and "Land Use" not in df.columns and "lulc" not in df.columns and "LULC" not in df.columns:
            messagebox.showerror("Error", "Column 'Land use' or 'LULC' not found in the Excel file.")
            return
        if "slope" not in df.columns and "Slope" not in df.columns and "New_Slope" not in df.columns:
            messagebox.showerror("Error", f"Column 'Slope' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "surface texture" not in df.columns and "Surface Texture" not in df.columns and "Surface_Te" not in df.columns:
            messagebox.showerror("Error", f"Column 'Surface Texture' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "soil depth" not in df.columns and "Soil Depth" not in df.columns and "Soil_Depth" not in df.columns:
            messagebox.showerror("Error", f"Column 'Soil depth' not found in sheet '{sheet_name}' of Excel file.")
            return
        
        
        
        # Rename columns to lowercase if necessary
        if "lulc" in df.columns:
            df.rename(columns={"lulc": "land use"}, inplace=True)
        elif "LULC" in df.columns:
            df.rename(columns={"LULC": "land use"}, inplace=True)
        elif "Land Use" in df.columns:
            df.rename(columns={"Land Use": "land use"}, inplace=True)
        if "New_Slope" in df.columns:
            df.rename(columns={"New_Slope": "slope"}, inplace=True)
            df["New_Slope"] = df["New_Slope"].str.replace(r'\s*%\d+-\d+%\s*', '', regex=True)
            df["New_Slope"] = df["New_Slope"].str.replace(r'\s*%\s*', '', regex=True)
            df["New_Slope"] = df["New_Slope"].str.replace(r'\s*\([^()]*\)\s*', '', regex=True)
            df["New_Slope"] = df["New_Slope"].str.replace(r'\(>[0-9]+\s*%\)', '', regex=True)
        elif "Slope" in df.columns:
            df.rename(columns={"Slope": "slope"}, inplace=True)
            df["slope"] = df["slope"].str.replace(r'\s*%\d+-\d+%\s*', '', regex=True)
            df["slope"] = df["slope"].str.replace(r'\s*%\s*', '', regex=True)
            df["slope"] = df["slope"].str.replace(r'\s*\([^()]*\)\s*', '', regex=True)
            df["slope"] = df["slope"].str.replace(r'\(>[0-9]+\s*%\)', '', regex=True)
        if "Soil_Depth" in df.columns:
            df.rename(columns={"Soil_Depth": "soil depth"}, inplace=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\(\d+-\d+\s*cm\)', '', regex=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\s*\d+-\d+\s*cm\s*', '', regex=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\s*\([^()]*\)\s*', '', regex=True)

        elif "Soil Depth" in df.columns:
            df.rename(columns={"Soil Depth": "soil depth"}, inplace=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\(\d+-\d+\s*cm\)', '', regex=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\s*\d+-\d+\s*cm\s*', '', regex=True)
            df["soil depth"] = df["soil depth"].str.replace(r'\s*\([^()]*\)\s*', '', regex=True)
        
        
        if "Surface_Te" in df.columns:
            df.rename(columns={"Surface_Te": "surface texture"}, inplace=True)

        elif "Surface Texture" in df.columns:
            df.rename(columns={"Surface Texture": "surface texture"}, inplace=True)
        
        
        
        #df["slope"] = pd.to_numeric(df["slope"].astype(str).str.replace('[^0-9]+', ''), errors='coerce'
        

        
        
        
        

        

            # Apply check_values function to each row and store the result in "Output" column
        df["Output"] = df.apply(lambda row: check_values(row["land use"], row["slope"], row["surface texture"], row["soil depth"]), axis=1)
        
        
        # Split the string by whitespace, remove extra empty elements, and join the words with a single space
        df["slope"] = df["slope"].fillna('').map(lambda x: ' '.join(filter(None, str(x).split())) if not isinstance(x, float) else np.nan)
        df["soil depth"] = df["soil depth"].fillna('').map(lambda x: ' '.join(filter(None, str(x).split())) if not isinstance(x, float) else np.nan)

        # Perform the desired operation
        df.loc[df["slope"].str.lower().str.contains("moderately steeply sloping"), "slope"] += " (10-15%)"
        df.loc[(df["slope"].str.lower().str.contains("steeply sloping")) & (~df["slope"].str.lower().str.contains("moderately steeply sloping")), "slope"] += " (15-25%)"
        df.loc[df["slope"].str.lower().str.contains("gently sloping") & ~df["slope"].str.lower().str.contains("very"), "slope"] += " (3-5%)"
        df.loc[df["slope"].str.lower().str.contains("very gently sloping"), "slope"] += " (1-3%)"
        df.loc[df["slope"].str.lower().str.contains("moderately sloping"), "slope"] += " (5-10%)"
        df.loc[df["slope"].str.lower().str.contains("strongly sloping"), "slope"] += " (>25 %)"
        
            
        df.loc[df["soil depth"].str.lower().str.contains("shallow") & ~df["soil depth"].str.lower().str.contains("very") & ~df["soil depth"].str.lower().str.contains("moderately"), "soil depth"]  += " (25-50 cm)"
        df.loc[df["soil depth"].str.lower().str.contains("very shallow"), "soil depth"] += " (0-25 cm)"
        df.loc[df["soil depth"].str.lower().str.contains("moderately shallow"), "soil depth"] += " (50-70 cm)"
        df.loc[df["soil depth"].str.lower().str.contains("deep") & ~df["soil depth"].str.lower().str.contains("moderately"), "soil depth"] += " (100-150 cm)"
        df.loc[df["soil depth"].str.lower().str.contains("moderately deep"), "soil depth"] += " (75-100 cm)"

        

        




        

        
        # Add output dataframe to list
        output_dfs.append(df)
    
    # Combine output dataframes into single dataframe
    output_df = pd.concat(output_dfs)
    print(output_df)
    
    # Create new Excel file with output value
    output_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    output_df.to_excel(output_path, index=False)
    
    # Show success message
    messagebox.showinfo("Success", "New Excel file created with output value.")

    
# Create Tkinter window
root = tk.Tk()
root.title("Excel File Processor")

# Add button to upload Excel file and process it
upload_button = tk.Button(root, text="Soil Conservation Structure", command=process_file)
upload_button.pack()

# Run Tkinter event loop


import tkinter.ttk as ttk
# Function to check values and return output
def check_values1(stream_order,length1,length2,stream_width,surface_texture,stream_alignement):
 
    stream_order = ' '.join(stream_order.lower().split())
    stream_width = ' '.join(stream_width.lower().split())
    surface_texture = ' '.join(surface_texture.lower().split())  
    stream_alignement = ' '.join(stream_alignement.lower().split())


    if stream_order == "1st" and (length1 >=0 and length2 <=200) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "straight":
        return "Brushwood Check dam/Vegetative"
    
    if stream_order == "1st" and (length1 >=200 and length2 <=400) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "straight":
        return "Loose boulder check dam"
    
    if stream_order == "1st" and (length1 >=400 and length2 <=1000) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "straight":
        return "Gabion structure"
    
    if stream_order == "2nd" and (length1 >=0 and length2 <=1000) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "straight":
        return "LBCD(if 1st Order is Brushwood/Vegetative and Gabion structure(if 1st Order is LBCD))"
    
    if stream_order == "2nd" and (length1 >=0 and length2 <=1000) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("course" in surface_texture.split(",") or "sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "depresion":
        return "Percolation Tank"
    
    if ("3rd" in stream_order.split(",") or  "4th" in stream_order.split(",")) and (length1 >=0 and length2 <=1000) and ( "medium" in stream_width.split(",") or  "narrow" in stream_width.split(",") or "wide" in stream_width.split(",") ) and  ("sand" in surface_texture.split(",") or "loamy sand" in surface_texture.split(",") or "sandy loam" in surface_texture.split(",") or"loam" in surface_texture.split(",") or "slit loam" in surface_texture.split(",") or "sandy clay loam" in surface_texture.split(",") or "clay loam" in surface_texture.split(",") or "silt clay loam" in surface_texture.split(",") or "sandy clay" in surface_texture.split(",") or "silty clay" in surface_texture.split(",") or "clay" in surface_texture.split(",") or "silt" in surface_texture.split(",")) and stream_alignement == "straight":
        return "Masonary Check Dam/Earthen Check Dam"
    
    else:
        return "No match found"

# Function to open new window for drainage line processing
def open_drainage_line_window():

    # Create new Tkinter window
    new_window = tk.Toplevel(root)
    new_window.title("Drainage Line Structure")
    
    # Add label to new window
    label = tk.Label(new_window, text="Upload and Process File for Drainage Line")
    label.pack(pady=20)
    
    # Add button to new window
    button = tk.Button(new_window, text="Upload and Process File", command=process_drainage_file)
    button.pack(pady=10)
    
# Function to handle file upload and processing for drainage line
def process_drainage_file():
    # Open file dialog to select Excel file 
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    # Read Excel file into pandas ExcelFile object
    excel_file = pd.ExcelFile(file_path)
    
    # Create empty list to store output dataframes for each sheet
    output_dfs = []
    
    # Loop through all sheet names in Excel file
    for sheet_name in excel_file.sheet_names:  
        # Read sheet into pandas DataFrame
        df = pd.read_excel(excel_file,sheet_name=sheet_name)

        # Check for column names in different cases
        if "stream order" not in df.columns and "Stream Order" not in df.columns:
            messagebox.showerror("Error", f"Column 'Stream Order' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "length1" not in df.columns and "Length1" not in df.columns:
            messagebox.showerror("Error", f"Column 'Length1' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "length2" not in df.columns and "Length2" not in df.columns:
            messagebox.showerror("Error", f"Column 'Length2' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "stream width" not in df.columns and "Stream Width" not in df.columns:
            messagebox.showerror("Error", f"Column 'Stream Width' not found in sheet '{sheet_name}' of Excel file.")
            return
        if "surface texture" not in df.columns and "Surface Texture" not in df.columns:
            messagebox.showerror("Error", f"Column 'Surface Texture' not found in sheet '{sheet_name}' of Excel file.")
            return
        
        if "stream alignement" not in df.columns and "Stream Alignement" not in df.columns:
            messagebox.showerror("Error", f"Column 'Stream Alignement' not found in sheet '{sheet_name}' of Excel file.")
            return

        
        # Rename columns to lowercase if necessary

        df.rename(columns={
           'Stream Order': 'stream order',
           'Length1': 'length1' ,
           'Length2': 'length2' ,
           'Stream Width': 'stream width' ,
           'Surface Texture': 'surface texture' ,
           'Stream Alignement': 'stream alignement'
        }, inplace=True)


        df["length1"] = df["length1"].apply(lambda x: re.sub('[^0-9\.]','', str(x)))
        df["length1"] = df["length1"].astype(float)
        df["length2"] = df["length2"].apply(lambda x: re.sub('[^0-9\.]','', str(x)))
        df["length2"] = df["length2"].astype(float)
        

        # Add output dataframe to list
        df["Output"] = df.apply(lambda row: check_values1(row["stream order"], row["length1"],row["length2"], row["stream width"],row["surface texture"],row["stream alignement"]), axis=1)
        output_dfs.append(df)
        print(output_dfs)


    # Combine output dataframes into single dataframe
    output_df = pd.concat(output_dfs)
    
    # Create new Excel file with output value
    output_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    output_df.to_excel(output_path, index=False)
    
    # Show success message
    messagebox.showinfo("Success", "New Excel file created with output value for drainage line.")
    
    
# Add button to main window to open new window for drainage line processing
drainage_button = tk.Button(root,text="Drainage Line Structure", command=open_drainage_line_window)
drainage_button.pack(pady=20)

root.mainloop()
 