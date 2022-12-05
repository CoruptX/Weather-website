from flask import Flask,render_template,request
import requests
import json
app=Flask(__name__)
cities=["Sus","Baka"]

@app.route("/",methods=['GET','POST'])
def home():

    if request.method=="POST":
        cities.append(request.form["city"].strip())
    api="14fa0ae8418824259cd5d41ad2d48c03"
    posts=[]
    for city in cities:

        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}"

        data=requests.get(url).json()
        temp=data["main"]["temp"]
        desc=data["weather"][0]["description"]
        icon=data["weather"][0]["icon"]

        info={"temp":temp,"desc":desc,"icon":icon,"name":city.title()}
        posts.append(info)
    return render_template("weather.html",posts=posts)

if __name__ == "__main__":
    app.run(debug=True)