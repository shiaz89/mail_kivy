import os
import pathlib
import sys

AS_EXE = hasattr(sys, "MEIPASS")
APP_DIR = pathlib.Path(os.path.dirname(__file__))
HOME_DIR = pathlib.Path.home()
TESSERACT_DIR = APP_DIR.parent / "Tesseract-OCR"
