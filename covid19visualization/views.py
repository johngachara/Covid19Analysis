from django.shortcuts import render
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
# Create your views here.
def home(request):
   dpath = '/home/gachara/PycharmProjects/djangoProject8/covid_19_clea n_complete.csv'
   data = pd.read_csv(dpath)
   num1 = random.randint(0,20)
   num2 = random.randint(21,1000)
   data = data.iloc[num1:num2]
   data = data[["Country/Region","Date","Confirmed","Deaths","Recovered","Active"]]
   sns.pairplot(data,hue="Country/Region")
   plt.savefig("static/charts/photo1.jpg")
   return render(request,'home.html',{"data":data})
def other(request):
   path = '/home/gachara/PycharmProjects/djangoProject8/covid_19_clea n_complete.csv'
   data = pd.read_csv(path)
   data = data.head(3000)
   comp = data['Confirmed']
   death = data['Deaths']
   recov = data['Recovered']
   sns.barplot(data=data, x=death, y=comp)
   plota = plt.savefig("static/page2/chart2.png")
   sns.catplot(data,x=death,y=comp)
   plotb = plt.savefig("static/page2/chart3.png")
   sns.catplot(data,x=recov,y=death)
   plotc = plt.savefig("static/page2/chart4.jpg")
   return render(request,'other.html')
