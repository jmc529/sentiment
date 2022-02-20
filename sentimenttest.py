# Code used: 
# https://rapidapi.com/fyhao/api/text-sentiment-analysis-method
# https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
# https://textblob.readthedocs.io/en/latest/quickstart.html#quickstart

import json
import http.client
from textblob import TextBlob
import matplotlib.pyplot as plt

conn = http.client.HTTPSConnection("text-analysis12.p.rapidapi.com")
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "text-analysis12.p.rapidapi.com",
    'x-rapidapi-key': "add-key"
    }

def testSentimentAPIFile():
    apiRes = []
    try:
        testData = open("./datasetSentences.txt", "r")

        for i in range(50):
            line = next(testData).strip()
            line = line[line.index("	") + 1:]

            payload = json.dumps({
                "language": "english",
                "text": line 
                })
                
            conn.request("POST", "/sentiment-analysis/api/v1.1", payload, headers)
            
            res = conn.getresponse()
            data = res.read()
            compound = json.loads(data.decode("utf-8"))['aggregate_sentiment']['compound']
            apiRes.append((float(compound) + 1) / 2)
        
        testData.close()

        return apiRes
    except Exception as e:
        print(e)
        raise e


def testSentimentTextblobFile():
    textRes = []

    try:
        testData = open("./datasetSentences.txt", "r")

        for i in range(50):
            line = next(testData).strip()
            line = line[line.index("	") + 1:]

            text = TextBlob(line)

            textRes.append((float(text.sentiment.polarity) + 1) / 2)
        
        testData.close()

        return textRes
    except Exception as e:
        print(e)
        raise e


def sentimentStanford():
    standfordRes = []
    try:
        testData = open("./sentiment_labels.txt", "r")

        for i in range(50):
            line = next(testData).strip()
            line = line[line.index("|") + 1:]
            standfordRes.append(float(line))
        
        testData.close()

        return standfordRes
    except Exception as e:
        print(e)
        raise e


def deviation(observation, original):
    sum=0
    for i in range(len(observation)):
        sum += abs(original[i] - observation[i])
    mean_of_observations = sum / len(observation)
    sum_of_squared_deviation = 0

    for i in range(len(observation)):
        sum_of_squared_deviation += (abs(original[i] - observation[i]) - mean_of_observations) ** 2
    Standard_Deviation = ((sum_of_squared_deviation) / len(observation)) ** 0.5
    print("Sum of Squared Deviation of sample is ", sum_of_squared_deviation)
    print("Standard Deviation of sample is ", Standard_Deviation)

def plotSentiments():
    s = sentimentStanford()
    t = testSentimentTextblobFile()
    a = testSentimentAPIFile()


    # Sum of Squared Deviation of api is 1.9553150788445004
    # Standard Deviation of api is 0.19775313291295796
    # Sum of Squared Deviation of textblob is 1.3465313889591932
    # Standard Deviation of textblob is 0.16410553853902635
    deviation(a, s)
    deviation(t, s)
    
    plt.rcParams['figure.figsize'] = [10, 10]
    plt.subplot(211)
    plt.plot(s, color='blue', label='Standford')
    plt.plot(t, color='red', label='TextBlob')
    plt.plot(a, color='green', label='RestFUL API')
    plt.title('Sentiment Analysis')
    plt.ylabel('Sentiment')
    plt.legend()
    plt.show()

plotSentiments()
