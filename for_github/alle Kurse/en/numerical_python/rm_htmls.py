import os
from glob import glob

for fname in glob("*ipynb"):
    html_file = fname[:-5]+"html"
    if os.path.isfile(html_file):
        print(html_file)
        os.remove(html_file)

