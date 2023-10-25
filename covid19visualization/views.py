from django.shortcuts import render
from io import BytesIO
import pandas as pd
import base64
import seaborn as sns
import random
import matplotlib.pyplot as plt
# Create your views here.
def home(request):
   dpath = '/home/gachara/PycharmProjects/djangoProject8/covid_19_clea n_complete.csv'
   data = pd.read_csv(dpath)
   num1 = random.randint(0,20)
   num2 = random.randint(21,300)
   data = data.iloc[num1:num2]
   data = data[["Country/Region","Date","Confirmed","Deaths","Recovered","Active"]]
   sns.pairplot(data,hue="Country/Region")
   plt.savefig("static/charts/chart1.png")
   return render(request,'home.html',{"data":data})