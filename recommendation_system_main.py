from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
#content based filtering
# Sample movie data assigned by me with movie name and genre
my_movies_database = {
    'The Dark Knight': 'Action Crime Drama',
    'Inception': 'Action Adventure Sci-Fi',
    'Pulp Fiction': 'Crime Drama',
    'Forrest Gump': 'Drama Romance',
    'The Shawshank Redemption': 'Drama',
    'The Godfather': 'Crime Drama',
    'The Matrix': 'Action Sci-Fi',
    'The Lord of the Rings: The Return of the King': 'Adventure Drama Fantasy',
    'The Avengers': 'Action Adventure Sci-Fi',
    'Interstellar': 'Adventure Drama Sci-Fi',
    'me before you': 'Drama Romance',
    'titanic': 'Drama Romance',
    'the departed': 'Crime Drama Thriller',
    'the wolf of wall street': 'Comedy Biograpy Crime',
    'Dont look up': 'Comedy Drama Sci-Fi',
    'shutter island': 'Mystery Thriller',
    'catch me if u can': 'Crime Drama Biography',
    'mad max': 'Thriller Comedy Mystery'
}


# Function for generating movie recommendations based on movie genres
def recommend_movies(movie_title, num_recommendations=5):   #5recommendations for eac movie
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(list(my_movies_database.values()))
    cosine_sim = linear_kernel(tfidf_matrix, tfidf.transform([my_movies_database[movie_title]]))

    # Get movies list based on their cosine similarities
    movie_indices = cosine_sim.argsort(axis=0)[::-1].flatten()

    # for excluding input moive so it dont shown again
    similar_movies = [list(my_movies_database.keys())[i] for i in movie_indices if list(my_movies_database.keys())[i] != movie_title]

    return similar_movies[:num_recommendations]



print("Welcome to the Movie Recommendation System!")
while True:
    user_input_movie = input("Enter a movie title (or type 'exit' to quit): ")

    if user_input_movie.lower() == 'exit':
        print("Thank you for using the recommendation system. Goodbye!")
        break

    if user_input_movie in my_movies_database:
        recommendations = recommend_movies(user_input_movie)
        print(f"Recommended movies based on '{user_input_movie}':")
        for movie in recommendations:
            print(movie)
    else:
        print("Movie not found. Please enter another movie title.")
