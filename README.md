# Barcode Generator

This is a barcode generator for GTIN-12 and ITF-14 barcodes. It takes in a spreadsheet as input, refer to "Master GS1 UPC GTIN", with the following column configuration.

A : Category

B : Sub Category

C : Item

D : Sales Code

E : Each

F : GTIN-12 (U.P.C.) (Each  Code)

G : Case

H : ITF-14 (Case Code)

## How to Run

1. Download a copy of the "Master GS1 UPC GTIN" spreadsheet located in Google Drive (if not already present on local system) **DOWNLOAD AS EXCEL SPREADSHEET XLSX** 
2. Download the [latest release](https://github.com/RunamokMaple/barcode-generator/releases/latest) of the barcode generator
3. Navigate to the folder containing the barcode generator. Then navigate to **barcode-generator/dist**
4. Right click *barcode-generator.app* and click "Open". Apple will notify you that it is an unknown application and warn you before you are able to open it. **this is normal**
5. Give it a second to start up,  it will open a file explorer which you can use to navigate to your Downloads directory containing "Master GS1 UPC GTIN" and click "Open".
6. The program will run, then open up a folder containing the generated barcode images in png and svg (vector) formats
7. Upload all or a subset of the generated barcodes to a Google Drive.

## How to Build

```
pyinstaller --onefile --windowed --add-data "/Users/bender/Library/Fonts/DejaVuSans.ttf:fonts" main.py --collect-data barcode
```