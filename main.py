from flask import Flask,jsonify,request
import csv

allmovies=[]
with open("movies.csv" ,encoding="utf-8" ) as f:
    r=csv.reader(f)
    data=list(r)
    allmovies= data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome"
    
@app.route("/get-movie")
def get_movie():
    return jsonify({
     "data" : allmovies[0],
     "status" :"success"
    })
    
@app.route("/liked-movie", methods=["POST"])
def liked_movie():  
    global allmovies
    m=allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(m) 
    return jsonify({
     "status" :"success"
    }),200

@app.route("/unliked-movie", methods=["POST"])
def not_liked_movie():  
    global allmovies
    m=allmovies[0]
    allmovies = allmovies[1:]
    not_liked_movies.append(m) 
    return jsonify({
     "status" :"success"
    }),200

@app.route("/did_not_watch", methods=["POST"])
def did_not_watch():  
    global allmovies
    m=allmovies[0]
    allmovies = allmovies[1:]
    did_not_watch.append(m) 
    return jsonify({
     "status" :"success"
    }),200

app.run(debug=True)



