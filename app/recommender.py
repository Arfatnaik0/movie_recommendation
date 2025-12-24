from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(title,data,tfidf_matrix):
    title = title.lower()
    if title not in data['title'].values:
        return ["Movie not found. Please check the title and try again."]
    
    idx = data[data['title'] == title].index[0]
    sim=cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
    sim_score = list(enumerate(sim[0]))
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    sim_score = sim_score[1:11]
    recommendations=[]
    for i in sim_score:
        recommendations.append(data['title'].iloc[i[0]])
    return recommendations