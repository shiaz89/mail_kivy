import cv2
import pytesseract
from pathlib import Path


class ImgReader:
    def __init__(self, tesseract_path: Path = Path("C:\Program Files\Tesseract-OCR")) -> None:
        """
        Класс для чтения текста с картинки.

        :param tesseract_path: Путь до tesseract.
        """
        pytesseract.pytesseract.tesseract_cmd = tesseract_path.joinpath("tesseract.exe")
        self.tessdata_dir_config = f"--tessdata-dir '{tesseract_path.joinpath('tessdata')}'"

    def read_img(self, filename: str, lang: str = "eng"):
        # Подключение фото
        image = cv2.imread(filename)
        s = pytesseract.image_to_string(image, config=self.tessdata_dir_config, lang=lang)
        return s

    def read_processing_img(self, filename: str, lang: str, chan: int = 100, size: int = 150):
        # Подключение фото
        image = cv2.imread(filename)
        scale_percent = int(size)  # Процент от изначального размера
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  #
        ret, threshold_image = cv2.threshold(gray, chan, 150, 1, cv2.THRESH_BINARY)
        s = pytesseract.image_to_string(threshold_image, config=self.tessdata_dir_config, lang=lang)
