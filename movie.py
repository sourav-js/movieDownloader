import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request
app=Flask(__name__)

@app.get("/")
def home_page():

    return render_template("input.html") 

@app.post("/findMovies")

def finding():
     Name=request.form["movie"]
     html=requests.get(f"https://thepiratebay.party/search/{Name}/1/99/0")
     data=BeautifulSoup(html.text,"html.parser")
     alldata=data.select("tr")
     
     return render_template("finder.html",lens=len(alldata),items=alldata) 

if __name__=="__main__":
 app.run(debug=True,port=os.environ.get('PORT', 5000))
