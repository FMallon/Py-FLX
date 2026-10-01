from pathlib import Path
import os
import shutil




class Validation:

    @staticmethod
    def file_exists(file: Path) -> int:

        if not file:
            print("\n[INFO] The File Name is empty - this may be an internal issue!")
            return 1

        if not Path(file).is_file():
            print(f"\n[INFO] The File {file} doesn't exist")
            return 2

        return 0


    @staticmethod
    def file_is_executable(file: Path) -> int:

        if not file:
            print("\n[INFO] The File Name is empty - this may be an internal issue!\n")
            return 1

        if not os.access(file, os.X_OK):
            print(f"\n[INFO] The file {file} is not executable\n")
            return 2

        return 0


    @staticmethod
    def is_a_command(command: str) -> int:

        if not command:
            return 1

        if not shutil.which(command):
            return 2

        return 0


    @staticmethod
    def directory_exists(directory: Path) -> int:

        if not directory:
            print("\n[INFO] The Directory Name is empty - this may be an internal issue!\n")
            return 1

        if not Path(directory).is_dir():
            print(f"\n[INFO] The directory {directory} doesn't exist\n")
            return 2

        return 0



    @staticmethod
    def validate_image(image: Path) -> int:

        from PIL import Image
        import xml.etree.ElementTree as ET


        if not image.is_file():
            return 1

        suffix = image.suffix.lower()

        if suffix == ".svg":

            try:
                
                ET.parse(image)

            except (ET.ParseError, OSError):
                
                return 2

            return 0

        try:
            with Image.open(image) as img:

                img.verify()

        except (OSError, Image.UnidentifiedImageError):

            return 2

        return 0