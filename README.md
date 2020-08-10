# Fake News Classifier
## Overview
This is an LSTM RNN model that classifies news stories as fake or not.  
At this point, the answer is the probability of a given story to be fake.

The data for training this model is taken from: https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

## Usage
```python
import requests

url = 'http://localhost:9000/predict'
data = 'the news are TRUE, we all must believe that!'
r = requests.post(url, data)

print(r.json())
``` 
`data` is where the news story is stored (as python string). At this point the usage is local, the plan is to make
a web page to serve the predictions.



## TODO
1. Deploy to Heroku
2. Front-end work  
    1. Make a web page with a text box to paste the news story and a predict button  
    2. Once the model returns the `str` answer, it should be displayed in a designated place on the page (maybe an answer section)  
2. Improve logging