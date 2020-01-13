from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo


app=Flask(__name__)



@app.route("/")
def index():
    #setup mongo
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
    mongo=PyMongo(app)
    # data=mongo.db.marsdict.find()
    data = mongo.db.marsdict.find_one()
    return render_template("index.html", data=data)
        
   
@app.route("/scrape")
def scrape():
    #setup mongo
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
    mongo=PyMongo(app)

    data=mongo.db.marsdict
    listings_data=scrape_mars.scrape()
    print(listings_data)
    data.update({},listings_data)
    return redirect("/", code=302)
    


if __name__=="__main__":
    app.run(debug=True)
