# UdemyProject1Exercise-national_debt

# Exercise
Debt to GDP ratio by country
So your job is to scrape the national debt to GDP for each country 
listed in this website 'http://worldpopulationreview.com/countries/countries-by-national-debt/'.

# Scrapy command:
- run scrapy script -----> scrapy crawl gdp_debt
- run scrapy shell ------> scrapy shell

- Create New Scrpay Project -------> scrapy startproject national_debt

- You can start your first spider with:
    - cd national_debt
    - scrapy genspider example example.com

- Create Scrapy spider -------> scrapy genspider gdp_debt worldpopulationreview.com/countries/countries-by-national-debt

- Export Excel Command -----> scrapy crawl gdp_debt -o gdpRatio.csv

# Anaconda command: 
- install dependencies ----> conda install -c conda-forge scrapy==1.6 pylint autopep8 -y
- install iPython ---------> conda install iPython