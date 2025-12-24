from flask import Flask,request, render_template
import joblib
data=joblib.load("..\\model and data\\data.pkl")
tfidf_matrix=joblib.load("..\\model and data\\tfidf_matrix.pkl")

from recommender import get_recommendations
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie=request.form['movie']
    recommendations=get_recommendations(movie,data,tfidf_matrix)
    return render_template('index.html', movie=movie, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=False)
