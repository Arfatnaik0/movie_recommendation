from flask import Flask,request, render_template
import joblib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "model and data", "data.pkl")
tfidf_path = os.path.join(base_dir, "model and data", "tfidf_matrix.pkl")

data=joblib.load(data_path)
tfidf_matrix=joblib.load(tfidf_path)

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
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))