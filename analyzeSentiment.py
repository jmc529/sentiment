# Code used: 
# https://rapidapi.com/fyhao/api/text-sentiment-analysis-method

import json
import http.client
from textblob import TextBlob
import matplotlib.pyplot as plt


blackwoman = []
whiteman = []
whitewoman = 0

blackwoman1 = []
whiteman1 = []
whitewoman1 = 0

def awsFile():
    try:
        for i in range(5):
            testData = json.load(open("./awsData/transcribedData/blackwoman"+str(i+1)+".json", "r"))

            transcript = testData['results']["transcripts"][0]['transcript']
            text = TextBlob(transcript)
            blackwoman.append((float(text.sentiment.polarity) + 1) / 2)

        for i in range(2):
            testData = json.load(open("./awsData/transcribedData/whiteman"+str(i+1)+".json", "r"))
            
            transcript = testData['results']["transcripts"][0]['transcript']
            text = TextBlob(transcript)
            whiteman.append((float(text.sentiment.polarity) + 1) / 2)
            
        testData = json.load(open("./awsData/transcribedData/whitewoman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        whitewoman = (float(text.sentiment.polarity) + 1) / 2


        testData = json.load(open("./awsData/transcribedData/whiteman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        whiteman.append((float(text.sentiment.polarity) + 1) / 2)

        testData = json.load(open("./awsData/transcribedData/blackwoman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        blackwoman.append((float(text.sentiment.polarity) + 1) / 2)
    except Exception as e:
        print(e)
        raise e


def transcribedFile():
    try:
        for i in range(5):
            testData = json.load(open("./awsData/analyzedData/blackwoman"+str(i+1)+".json", "r"))

            transcript = testData['results']["transcripts"][0]['transcript']
            text = TextBlob(transcript)
            blackwoman1.append((float(text.sentiment.polarity) + 1) / 2)

        for i in range(2):
            testData = json.load(open("./awsData/analyzedData/whiteman"+str(i+1)+".json", "r"))
            
            transcript = testData['results']["transcripts"][0]['transcript']
            text = TextBlob(transcript)
            whiteman1.append((float(text.sentiment.polarity) + 1) / 2)
            
        testData = json.load(open("./awsData/analyzedData/whitewoman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        whitewoman1 = (float(text.sentiment.polarity) + 1) / 2

        testData = json.load(open("./awsData/analyzedData/whiteman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        whiteman1.append((float(text.sentiment.polarity) + 1) / 2)

        testData = json.load(open("./awsData/analyzedData/blackwoman.json", "r"))
        transcript = testData['results']["transcripts"][0]['transcript']
        text = TextBlob(transcript)
        blackwoman1.append((float(text.sentiment.polarity) + 1) / 2)

    except Exception as e:
        print(e)
        raise e

def plotSentiments():    
    plt.rcParams['figure.figsize'] = [10, 10]
    plt.subplot(211)
    plt.plot(whiteman, color='blue', label='AWS')
    plt.plot(whiteman1, color='red', label='Actual')
    plt.title('Sentiment Analysis White Men')
    plt.ylabel('Sentiment')
    plt.legend()
    plt.show()

awsFile()
transcribedFile()
plotSentiments()