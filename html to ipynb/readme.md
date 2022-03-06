# Scrap HTML file to Ipyn (especially the HTML is from ipynb nbconvert)

The idea came to me when I start to study online for python and I got a website that has some tutorials but instead of ipynb it is HTML

## Usage


open the auto_file.py and enter the URL u want to convert, and just run it 


```python

url = 'https://imic.edu.vn/training/basic-python/Phan-03-Kien-thuc-Python-co-ban-2022.html'

```

## Requirements 
you need to install [PyToIpynb](https://marketplace.visualstudio.com/items?itemName=MaorBarak.pytoipynb&utm_source=VSCode.pro&utm_campaign=AhmadAwais) and of course VScode king of all code


## Logic behind the code

I use the BeautifulSoup to process the HTML file after that collect all the text-based from that HTML into 1 txt file, and it is so lucky that BeautifulSoup also save the indent between each line and ipynb will graduate to have the "In[]" box that where we run the code and now our job is just to process the string base one into py and use the PyToIpynb extension to make it into ipynb

