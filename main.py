from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
   

@app.route("/liked-movie",   )
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    
   

@app.route("/unliked-movie",)
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    
   

@app.route("/did-not-watch", )
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    

if __name__ == "__main__":
  app.run()
