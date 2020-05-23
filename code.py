# --------------
from csv import reader



def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    print(dataset[start:end])
    if rows_and_columns==True:
        print(len(rows_and_columns))
    
    
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based           on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    cnt1=0
    uniq=[]
    unmovies=[]
    for i in range(len(dataset)):
        cnt=0
        for j in range(len(dataset)):
            if dataset[i][index_]==dataset[j][index_] and i!=j:
                if dataset[i][index_] not in uniq:
                    uniq.append(dataset[i][index_])
                    unmovies.append(dataset[i])
    print(set(uniq))


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_=[]
    for i in dataset:
            if i[index_]==lang_:
                    movies_.append(i)
    explore_data(movies_,0,2)

    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies=[]
    for i in range(len(dataset)):
        if(float(dataset[i][11])>=rate_low ):
                rated_movies.append(dataset[i])
    explore_data(rated_movies,1,5)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)


movies_header=movies[0]
print(movies_header)
# The first row is header. Extract and store it in 'movies_header'.
movies=movies[1:]
del(movies[4553])



# Subset the movies dataset such that the header is removed from the list and store it back in movies




# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.



# Using explore_data() with appropriate parameters, view the details of the first 5 movies.

#explore_data(movies,0,5)


# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.

duplicate_and_unique_movies(movies,13)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max={}

for i in movies:
    if i[13] in ['Batman', 'The Host', 'Out of the Blue']:
        if i[13] not in reviews_max.keys():
            reviews_max[i[13]]=i[12]
        else:
            if i[12]>reviews_max[i[13]]:
                reviews_max[i[13]]=i[12]
movies_clean=movies
for i in movies_clean:
    if i[13] in ['Batman', 'The Host', 'Out of the Blue']:
        if i[12]!=reviews_max[i[13]]:
            print(1)
            movies_clean.remove(i)
# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 


print('-'*25)

# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies,3,'en')
print(movies_en)



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies=rate_bucket(movies_en,8,10)
print(high_rated_movies)



