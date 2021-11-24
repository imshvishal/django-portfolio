"""from zipfile import ZipFile

with ZipFile('main.zip', 'r') as file:
    file.extractall('')
"""
import shutil
shutil.make_archive("website", 'zip', '.')