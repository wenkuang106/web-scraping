import requests
from bs4 import BeautifulSoup
import pandas as pd

##### Setting variables that equals to which HTML/site to perform 'WEBSCRAPPING' ##### 

page = requests.get('https://top10.netflix.com/')
page_2 = requests.get('https://www.imdb.com/title/tt0898266/')

##### Loading the 'HTML/Site' ##### 

# Create a BeautifulSoup object
netflix = BeautifulSoup(page.text, 'html.parser')
TBBT = BeautifulSoup(page_2.text, 'html.parser')

# print pretty
print(netflix.prettify())
print(TBBT.prettify())

##### Beging Webscrapping ##### 

#### Site 1 #### 

movies_top_netflix = netflix.find_all('td', class_='pb-2 font-600 text-sm xs:text-base sm:text-lg leading-tight pt-2')
movies_top_netflix_2 = netflix.find_all('td', class_='pb-2 font-600 text-sm xs:text-base sm:text-lg leading-tight')
weeks_top = netflix.find_all('div', class_='w-12 text-center sm:pr-2 sm:text-right whitespace-nowrap')

#### Site 2 #### 

actor = TBBT.find_all('a', attrs={'data-testid':'title-cast-item__actor'})
character = TBBT.find_all('a', attrs={'data-testid':'cast-item-characters-link'})
length = TBBT.find_all('span', attrs={'data-testid':'title-cast-item__tenure'})

##### Cleansing Data/Information ##### 

top_net = []
for names in movies_top_netflix:
    print(names.text)
    names = names.text 
    ## clean name remove whitespace
    names = names.strip()
    ## remove new line
    names = names.replace('\n','')
    top_net.append(names)
for names_2 in movies_top_netflix_2:
    print(names_2.text)
    names_2 = names_2.text 
    names_2 = names_2.strip()
    names_2 = names_2.replace('\n','')
    top_net.append(names_2)
len(top_net) ## confirming that is the right # of items found 

weeks_in_top = []
for week in weeks_top:
    print(week.text)
    week = week.text
    week = week.strip()
    week = week.replace('\n','')
    week = week.replace(' ','')
    weeks_in_top.append(week)
len(weeks_in_top) 

cast = []
for actor in actor:
    print(actor.text)
    actor = actor.text
    actor = actor.strip()
    cast.append(actor)
len(cast)

roles = []
for role in character:
    print(role.text)
    role = role.text
    role = role.strip()
    roles.append(role)
len(roles)

duration = []
for year in length:
    print(year.text)
    year = year.text
    year = year.strip()
    duration.append(year)
len(duration)

##### Saving Data/Information Obtained as DataFrames #####

df_netflix = pd.DataFrame({
    'Currrent Top 10 Films on Netflix':top_net, 
    'Weeks in Top 10':weeks_in_top
    })
df_netflix

df_TBBT = pd.DataFrame({
    'Cast':cast,
    'Role Played':roles,
    'Year in Show':duration
})
df_TBBT

##### Saving DataFrames into '.CSV' #####

df_netflix.to_csv('Netflix_Top_10.csv')
df_TBBT.to_csv('TBBT.CSV')