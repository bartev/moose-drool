import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('pydata-book/ch02/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('pydata-book/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('pydata-book/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)

# merge tables together
data = pd.merge(pd.merge(ratings, users), movies)
# value at index = 0
data.ix[0]

# Get mean rating by gender using pivot_table
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
mean_ratings[:5]

data.groupby('title').size()


# get the indices (movie titles) of movies with at least 250 ratings
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
# Select rows from mean_ratings whose index is in active_titles
mean_ratings = mean_ratings.ix[active_titles]

# Get top female viewers
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)


mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
rating_std_by_title.order(ascending=False)[:10]
