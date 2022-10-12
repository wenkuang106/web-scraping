# HHA 507 Webscrapping Assignment 

For this assignment to be able to be completed properly the below packages must be imported/installed on the local system: 
```sh 
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
My approach to this assignment was to first look for the type of data/information that I am trying to collect and then use the ``` inspect ``` function of Google Chrome to look at their ```HTML Tag```. Once I find that the information/data I wish to collect have the same tag I begin coding it into the ```main.py``` file. If the tag I wish to use does not contain all the data/information I wish to collect, then I would write another line of code that would contain the tag that data/information would be in. After that I would then merge all the information collected into their respect lists. 