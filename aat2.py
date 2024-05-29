import requests
from surprise import Dataset, Reader, SVD

# A list to store the user data
user_data = []


api_key = "4d096121f63b2c55f74cc40d13d3f2f4"
# Iterate through the users
for user_id in range(1, 100):
  
    # Make a request to the API to get the user's watched movies
    url = f"https://api.themoviedb.org/3/account/{user_id}/rated_movies?api_key={api_key}&language=en-US"
    response = requests.get(url)

    # Get the JSON data from the response 
    data = response.json()

    # Iterate through the user's watched movies
    for movie in data["results"]:
        # Extract the relevant information from the movie
        user_data.append([user_id, movie["id"], movie["rating"]])


# Create a Reader object
reader = Reader(line_format='user item rating', rating_scale=(0, 10))

# Load the data into a Dataset object
data = Dataset.load_from_df(pd.DataFrame(user_data, columns=['user', 'item', 'rating']), reader)

# Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.25)

# Create and train the model
algo = SVD()
algo.fit(trainset)


# Use the trained model to make predictions
predictions = algo.test(testset)

# Evaluate the model
from surprise import accuracy
print(accuracy.rmse(predictions))


# Get the top n recommendations for a user
def get_top_n(predictions, n=10):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

# Print the top 10 recommendations for user 1
top_n = get_top_n(predictions, n=10)
print(top_n[1])
