#Import Pandas & datetime, read CSV files, setting to variables
import pandas as pd
from datetime import datetime
albums_file = "./data/spotify_albums.csv"
artists_file = "./data/spotify_artists.csv"
tracks_file = "./data/spotify_tracks.csv"
albums = pd.read_csv(albums_file, header=0)
artists = pd.read_csv(artists_file, header=0)
tracks = pd.read_csv(tracks_file, header=0)
#### head(), tail(), and .shape ####

# The head() function is used to displays the top n rows of a dataframe. n being the parameter fo the function, default being 5.
# The tail() function is the inverse of the head() function. It displays the bottom n rows of a dataframe The default is still 5.
# the .shape is used to return the dimensions of our data sets in a tuple (rows, columns)

## The output here tells us that this dataset is indeed about spotify albums. It has unique IDs for the artists and links to the album, suggesting that this dataset is used by the spotify app and used to return things to the user. Beyond that we can also see that it includes album types, track numbers, name, release date, and IDs to be read by (assuming) the app. 
albums.head()
## The output is telling us the same information here, with this though we can see that this data frame is 75510 rows. We also spot a new input for release_date_precision, instead of day we can now see year inputted.
albums.tail(10)
## Output here is pretty simple. rows = 75511 columns = 16
albums.shape

## With the output on the artists file we can see popularity rankings, follower count, genres, unique ID, name of the artist, track ID and the type of data (artist)
artists.head()
## Output for artists file here is again is the exact same data type, but we can now see the end of dataset. Which is 56128 rows.
artists.tail(9)
## again, rows = 56129 columns = 9
artists.shape

## The output for the tracks file is showing us specific songs along with properties of those tracks like: acousticness, countries the song can be accessed in, country of origin, danceability, duration, speechiness, tempo, time signature, track number in the album, and the valence.
## something to note here is that our energy,href,id,instrumentalness,key,liveness,loudness,lyrics,mode,name,playlist,popularity, which can be seen from the csv file are not displayed here for brevity sake.
tracks.head()
## Again here same data is available, but sommething to note is that we are still not getting all of our columns displayed at this time. We can see that there's 101,938 rows in this dataset.
tracks.tail(10)
## returns rows = 101939 columns = 32
tracks.shape

#For Albums, use .loc to show just rows 10-20 of the 'name' and 'release_date' columns
albums.loc[10:20, ['name', 'release_date']]

#Remove duplicates from each dataset
albums.drop_duplicates()
artists.drop_duplicates()
tracks.drop_duplicates()

    #For Artists: Write a map() function to replace the empty list ([]) entries in the genres column with NaNs
    #(but don't alter the list entries in genres that contain values!)
def empty_field_destroyer(value):
    if value == '[]':
        return float()
    else:
        return value
artists["genres"] = artists["genres"].map(empty_field_destroyer)
artists.head(9)
# Im not sure if this is the best way to get a NaN, but everything else i've tried returns it as a string. Which isn't a true NaN floating point object.
# I considered using numpy, which has a way to produce a NaN object with numpy.nan. But we haven't covered that so I left it as is!

# For Tracks:
    #Print the names of the columns in Tracks
def print_track_cols(col):
    for col in tracks.columns:
        print(col)
print_track_cols(tracks)
    # First, look at the values for lyrics to see why you think they don't parse well in Excel and some other programs
print(tracks.lyrics)
    # Drop the lyrics column
tracks.drop("lyrics", axis=1, inplace=True)
    # Target tracks file, drop the following: "lyrics" column, use the axis of columns, and do it inplace(modifying the dataframe permanently)
    # Print the names of the Tracks columns again, to show that the 'lyrics' column has been dropped
print_track_cols(tracks)
# Using Pandas, perform the following joins, choosing the join type that you think is appropriate.
# Make a comment in your code file on why you chose that join type

    # Join artists and albums on the artist ID
artists_albums = pd.merge(artists, albums, how='inner', left_on='id', right_on='artist_id')
    # I used the default inner join, I added it to the code to show that.
    # I did this because it retains the most amount of data and merging the shared value between the tables.
    # The other joins would produce a lot of empty fields, which clogs up our dataset.
# print the head() and shape of the resulting DataFrame
# print(artists_albums.head(), artists_albums.shape)
# Join albums and tracks on the album ID
albums_tracks = pd.merge(albums, tracks, left_on='id', right_on='album_id')
    # Another inner join, unless I know the use for this dataset I am going to leave as much data as possible.
# print the head() and shape of the resulting DataFrame
print(albums_tracks.head(), albums_tracks.shape)
# Use the Pandas to calculate some statistics on the data, and print the results:

#     Which artists appear the most times in the Artists data?
# display just artists column and then sort in descending order
artists_count = artists['name'].value_counts()
print(artists_count)
        # Sasha
# Which artists have the highest 'artist_popularity' rankings? (list the top ten in descending order)
artists_pop = artists['artist_popularity'].value_counts()
print(pd.DataFrame(artists['name'],artists_pop).head(10))
        # Jay Soto, The Winans, Johnathan Cohen, etc...(rest are displayed below for your viewing pleasure)   
# Bonus Point: How many albums came out in each year? (Notice that the values in the release_date column of Albums is in the format yyyy-mm-dd)
albums['release_date'] = pd.to_datetime(albums['release_date'])
years = albums['release_date'].dt.year
year_count = years.value_counts()
print(year_count)