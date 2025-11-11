# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

df_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]

plt.hist(netflix_df['duration'], 10000)
plt.show()

df_action90s = df_1990s[df_1990s['genre'] == "Action"]
print(df_action90s)
short_movie_count = 0

