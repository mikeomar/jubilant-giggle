
# coding: utf-8

# Michael Omoruan, computes the mean of the movies' duration and 

# ## Assignment 20
# 
# This assignment will use the IMDb dataset of the top 1000 movies from Lab 10, Part 2. The data CSV file is on GitHub here:  [imdb_1000.csv](https://github.com/justmarkham/DAT8/blob/master/data/imdb_1000.csv)  To download, right lick on Raw and save the CSV file. 
# 
# Write a piece of code that samples from this IMDb dataset, computes the mean of the movies' duration for each sample, and displays a histogram of these means.  Use a sample size of at least 30 and use at least 500 samples.

# In[122]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
film = pd.read_csv("imdb_1000.csv")
film_hours= film["duration"]
sample30 = film.sample(30)


# In[123]:


means = []


# In[125]:


sample30["duration"].mean()


# In[128]:


sample30["duration"].hist()


# In[130]:


sample30["duration"].max()


# In[131]:


sample30["duration"].min()


# In[133]:


sample30["duration"].median()


# In[ ]:


1. The range of the distribution would be 189-70 which is equal to 119 minutes.
2. The median value of the distribution would be 108.5 minutes.


# 1. What is the range of the empirical distribution displayed by your histogram?
# 2. What is the median value of the empirical distribution displayed by your histogram?
# 
# You can either esimate the answers from the histogram or figure out how to calculate them with code.
# 
# Write your answers below.

#  

#  
