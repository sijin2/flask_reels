import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


df = pd.read_csv('count.csv')

print(df)

count = Counter(df['hash']) 
count

kmean_count = dict()
for tag, counts in count.most_common(80):
    if(len(str(tag))>=1): 
        kmean_count[tag] = counts 
        print("%s : %d" % (tag, counts))

posts = list(kmean_count.keys())[:5]
recruits = list(kmean_count.values())[:5]

from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    print()
    return render_template("index.html", posts = posts, recruits = recruits)



if __name__ == '__main__':
    app.run(debug=True, port=5500) 