import glassdoor_scraper as gs
import pandas as pd 

# location of my chrome driver
# path = "C:/Users/Ken/Documents/ds_salary_proj/chromedriver"

path = "C:/Users/rache/Documents/intern_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',50, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
