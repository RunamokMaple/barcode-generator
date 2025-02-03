import barcode
from barcode.writer import ImageWriter
import sys
import os
from PIL import ImageFont
import stat
import tempfile
import shutil

def generate_itf14_barcode(itf, file_directory, filename="barcode.png"):
    """Generates an ITF-14 barcode and saves it as a PNG & SVG image."""

    font = ImageFont.load_default()

    # Create the barcode object
    itf14_barcode_png = barcode.get_barcode_class('itf')(itf, writer=ImageWriter())

    # Save the barcode as an image
    itf14_barcode_png.save(f"{file_directory}/{filename}")

    # Create SVG as well
    itf14_barcode_svg = barcode.get_barcode_class('itf')(itf)
    itf14_barcode_svg.save(f"{file_directory}/vectors/{filename}")

def generate_upc_barcode(gtin, file_directory, filename="barcode.png"):
    """Generates an UPC barcode and saves it as a PNG & SVG image."""

    font = ImageFont.load_default()

    # Create the barcode object
    upc_barcode_png = barcode.get_barcode_class('upc')(gtin, writer=ImageWriter())

    # Save the barcode as an image
    upc_barcode_png.save(f"{file_directory}/{filename}")

    # Create SVG as well
    upc_barcode_svg = barcode.get_barcode_class('upc')(gtin)
    upc_barcode_svg.save(f"{file_directory}/vectors/{filename}")