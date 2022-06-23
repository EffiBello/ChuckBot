from bs4 import BeautifulSoup
import requests

def getJokes(jokeNumber):
    URL = "https://parade.com/968666/parade/chuck-norris-jokes/"
    chuckNorrisPage = requests.get(URL)
    soup = BeautifulSoup(chuckNorrisPage.content, 'html.parser')
    olTag = soup.find("ol") #scrap the ol tag that contains the jokes
    jokesArray = []
    for li in olTag.find_all('li'):
        jokesArray.append(li.getText())
    return jokesArray[jokeNumber-1]


