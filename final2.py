import pandas

import pandas as pd

df = pd.read_csv("/Users/ellenmahoney/Desktop/donations - donations.csv")

print(df.to_string()) 

pip install matplotlib

import matplotlib

import matplotlib.pyplot as plt 
import csv

x = [] 
y = [] 
  
with open('/Users/ellenmahoney/Desktop/donations - donations.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for column in plots: 
        x.append([3]) 
        y.append((9)) 
  
plt.bar(x, y, color = 'g', width = 0.72, label = "Donations") 
plt.xlabel('Where donations are directed') 
plt.ylabel('Where donations originate') 
plt.title('Flow of Donations in US') 
plt.legend() 
plt.show() 

pip install requests

import requests

response = requests.get(url="https://cartes.io/")

pip install py-cartes-io

import py_cartes_io as cartes


params = {
    'lat': row['lat'],
    'lng': row['lng'],
    'description': row['description'],
    'category_name': row['category_name'],
    'link': row['link']
}

cartes.Maps('048eebe4-8dac-46e2-a947-50b6b8062fec').markers().create(params)