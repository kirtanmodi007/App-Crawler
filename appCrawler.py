# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:57:29 2020

@author: kirta
"""

#App Crawler Replica

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import pprint
import seaborn as sns


#App store Dataset
new_ios_apps = pd.read_csv(r"C:\Users\kirta\OneDrive\Desktop\Data Science Anaconda Python\App Crawler\new_free_ios.csv")
new_ios_apps.shape

new_ios_apps.head()


#Make a dictionary to count every Genre's occurance
new_ios_apps_genre_count_dictionary = {}

for particular_Genre in new_ios_apps['genres']:
    
#Now we have to convert this String into a List
    genre_List = json.loads(particular_Genre)
    for genre in genre_List:
        if genre in new_ios_apps_genre_count_dictionary:
            new_ios_apps_genre_count_dictionary[genre] = new_ios_apps_genre_count_dictionary[genre] + 1
        else:
            new_ios_apps_genre_count_dictionary[genre] = 1
    
pprint.pprint(new_ios_apps_genre_count_dictionary)


plt.bar(*zip(*new_ios_apps_genre_count_dictionary.items()))
plt.figure(figsize=(15,8))
plt.show()

#Converting dictionary into Dataframe
#new_free_ios_genre_data_frame = pd.DataFrame(list(new_ios_apps_genre_count_dictionary.items()), columns= ['Genre', 'Count'])
new_free_ios_genre_data_frame = pd.DataFrame(list(new_ios_apps_genre_count_dictionary.items()), columns= ['Genre', 'Count'])
# new_free_ios_genre_data_frame

plt.figure(figsize=(15,8))
ax = sns.barplot(x = "Count", y = "Genre", data = new_free_ios_genre_data_frame)
#ax.set_xticklabels(ax.get_xticklabels(), rotation=50, ha="right")
#plt.tight_layout()
#plt.show()

plt.figure(figsize=(15,8))
new_free_ios_genre_data_frame.plot(X = 'Genre', Y = 'Count', kind = 'bar', color=['black', 'red', 'green', 'blue', 'cyan'])
plt.show()
