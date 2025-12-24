# import necessary libraries
import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# load datasets
movies=pd.read_csv('..\\data\\tmdb_5000_movies.csv')
credits=pd.read_csv('..\\data\\tmdb_5000_credits.csv')

# merger movie and credits dataset
data=pd.merge(movies,credits,on='title')

# create a new dataframe with selected columns
data=data[['movie_id','title','overview','genres','keywords','cast','crew']]

# fill null values
data['overview']=data['overview'].fillna('')

# Function to convert list of dictionaries to list of names
def convert(obj):
    store=[]
    for i in ast.literal_eval(obj):
        store.append(i['name'])
    return store

# function to remove spaces between words
def remove_spaces(x):
    return [i.replace(" ","") for i in x]

data['genres'] = data['genres'].apply(convert)
data['keywords'] = data['keywords'].apply(convert)
data['keywords'] = data['keywords'].apply(remove_spaces)

# to get top 3 cast names and remove space between names of actor/actresses so model does not treat as different tokens
data['cast'] = data['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)][:3])
data['cast'] = data['cast'].apply(remove_spaces)

# same but extract directors name
data['crew'] = data['crew'].apply(lambda x:[i['name'] for i in ast.literal_eval(x) if i['job']=='Director']).apply(remove_spaces)

# create a tags column
data['tags']=data['genres']+data['keywords']+data['cast']+data['crew']

# convert list to string seperated by spaces
data['tags']=data['tags'].apply(lambda x: " ".join(x))

# add overview to the tags column
data['tags']=data['overview']+ " " +data['tags']

# drop irrelevant columns
data.drop(columns=['overview','genres','keywords','cast','crew'],inplace=True)

# lowercase the titles for easier matching later
data['title']=data['title'].str.lower()


# Create the tfidf matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['tags'])

# save the data and cosine_sim matrix using joblib
joblib.dump(data,'..\\model and data\\data.pkl')
joblib.dump(tfidf_matrix,'..\\model and data\\tfidf_matrix.pkl')

print("Model and data saved successfully.")


