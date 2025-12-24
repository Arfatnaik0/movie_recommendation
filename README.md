# Movie Recommendation System

## Overview
This project is a content-based movie recommendation system that suggests similar movies based on movie metadata.  
Instead of using user ratings, the system recommends movies by comparing content such as genres, keywords, cast, director, and plot overview.

The goal is to demonstrate how recommendation systems work using text representation and similarity measures.

![alt text](output.png)

---

## Dataset
**Source:** TMDB 5000 Movies Dataset (Kaggle)

The dataset contains information such as:
- Movie title
- Plot overview
- Genres
- Keywords
- Cast
- Crew (director)

---

## Project Structure
```
movie_recommendation_system/
│
├── data/
│ ├── tmdb_5000_movies.csv
│ └── tmdb_5000_credits.csv
│
├── notebook/
│ ├── rec.ipynb # Data processing and model building
│ └── test.ipynb # Load saved model and test recommendations
│
├── model and data/
│ ├── data.pkl # Processed movie data
│ └── tfidf_matrix.pkl # TF-IDF feature matrix
│
├── src/
│ └── model.py # Clean, runnable script
│
├── output.png
├── README.md
└── requirements.txt

```



---

## Approach
- Merged movie and credits datasets
- Selected relevant features: genres, keywords, cast, director, and overview
- Used only the top 3 cast members to reduce noise
- Extracted only the director from crew data
- Normalized names by removing spaces to treat them as single tokens
- Combined all features into a single text column (`tags`)
- Converted text data into numerical vectors using **TF-IDF**
- Computed **cosine similarity on demand** for recommendations

---

## Recommendation Logic
1. Convert movie content into TF-IDF vectors
2. When a movie title is provided:
   - Compute cosine similarity between the selected movie and all other movies
   - Sort similarity scores
   - Return the top most similar movies (excluding the input movie)

Unlike naive implementations, the project **does not compute a full similarity matrix**, improving space efficiency.

---

## Time and Space Optimization
- Cosine similarity is computed **on demand**, not precomputed for all movie pairs
- Space complexity reduced from **O(n²)** to **O(n)**
- Suitable for small to medium-sized datasets

This approach improves scalability while maintaining recommendation quality.

---

## Making Recommendations
The system takes a movie title as input and returns similar movies.

Example:
Enter movie name: interstellar


The system outputs a list of recommended movies based on content similarity.

Inference logic is demonstrated using:
- Saved TF-IDF matrix
- Saved processed movie data
- Reusable recommendation function

---

## Technologies Used
Python, Pandas, Scikit-learn, Joblib

---

## Limitations
- No personalization (same recommendations for all users)
- Does not use user ratings or viewing history
- On-demand similarity still requires comparison with all movies
- Not optimized for very large datasets

These limitations are expected for a content-based recommendation system.

---

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the notebook to build the model:
jupyter notebook notebook/rec.ipynb

3. Use the saved model for recommendations:
python src/model.py


---

## Conclusion
This project demonstrates how a content-based recommendation system can be built using text feature engineering, TF-IDF vectorization, and cosine similarity.  
It focuses on clean preprocessing, efficient similarity computation, and reproducible inference.
