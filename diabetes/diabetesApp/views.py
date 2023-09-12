from django.shortcuts import render
from diabetesApp.models import users

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
# Create your views here.
def loginview(request): 
    return render(request,'login.html')

def registerview(request):
    return render(request,'registration.html')

def saveuser_view(request):
    userName=request.POST["username"]
    passWord=request.POST["password"]
    Name=request.POST["name"]
    phoneNumber=request.POST["phone"]
    email=request.POST["email"]
    address=request.POST["address"]

    newuser=users(username=userName,password=passWord,name=Name,phone=phoneNumber,email=email,address=address)
    newuser.save()
    return render(request,'login.html')

def userlogin_view(request):
    userName=request.POST["username"]
    passWord=request.POST["password"]

    uname=users.objects.filter(username=userName)

    for u in uname:
        if u.password == passWord:
            return render(request,'home.html')
        else:
            
            return render(request,'login.html')

def check_diabetesview(request):
    Pregnancies=request.POST["pregnancies"]
    Glucose=request.POST["glucose"]
    Bloodpressure=request.POST["bloodpressure"]
    SkinThickness=request.POST["skinthickness"]
    Insulin=request.POST["insulin"]
    BMI=request.POST["bmi"]
    DPF=request.POST["dpf"]
    Age=request.POST["age"]

    dataset=pd.read_csv("diabetes.csv")
    x=dataset.iloc[:,:-1] #rows and columns
    y=dataset.iloc[:,-1]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.10) #or train_size=0.90 can be given
    #model object creation
    model=RandomForestClassifier(random_state=48) #random_state is used to shuffle the model

    model.fit(x_train,y_train)

   
    #data=[6,80,1,35,0,33.6,0.627,58]
    data=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DPF,Age]
    reshaped_data=np.reshape(data,(1,-1))
    predicted_result=model.predict(reshaped_data)
    if predicted_result[0]=="Yes":
        print("You have diabetes")
        result="You have diabetes"
    else:
        print("No diabetes")
        result="You are normal"

    return render(request,'result.html',{'result':result})

def homeview(request):
    return render(request,'home.html')
    