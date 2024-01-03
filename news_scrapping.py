# Scraping news data
# from id.inversting.com to get header of news daily

# {python}
# using selenium to process web scraping with chromedriver
from selenium import webdriver

filename ="scrap.csv"
f = open(filename, 'w')
headers ="Title, Time\n"

for i in range(1,1001):
    chrome_path = r"/usr/bin/chromedriver"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://id.investing.com/indices/idx-composite-news/{}".format(i))
    header = driver.find_elements_by_xpath("//*[@id='leftColumn']/div[8]/article/div[1]/a")
    time_stamp = driver.find_elements_by_xpath("//*[@id='leftColumn']/div[8]/article/div[1]/div/span[2]")
    for title, time in zip(header, time_stamp):
        print(title.text+"    "+time.text)
        f.write(title.text + ";" + time.text  + "\n")
    driver.quit()
