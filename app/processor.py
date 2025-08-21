import pandas as pd
from app.fetcher import Fetcher
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from app.helpers import get_weapon_list


nltk.download('vader_lexicon')# Compute sentiment labels
tweet = 'Skillcate is a great Youtube Channel to learn DataScience'
score=SentimentIntensityAnalyzer().polarity_scores(tweet)


class Processor:

    def __init__(self,data):
        self.data = pd.DataFrame(data)
        print(self.data.head())





    def find_rarest_word_per_twwet(self):
        text_column = self.data['Text']
        rarest_word = text_column.map(lambda x: pd.Series(x.split()).value_counts().idxmin())
        self.data['the_rarest_word'] = rarest_word



    def weapons_detected(self):
        self.data['weapons_detected'] = self.data['Text'].apply(Processor.check_weapon_in_text)
        print(self.data.head().to_string())

# TODO implement this function
    # def express_sentiment(self):
    #     self.df['sentiment'] = self.df['Text'].apply(Processor.check_sentiment)




    @staticmethod
    def check_weapon_in_text(text):
        weapons_list = get_weapon_list()
        weapon = ""
        for word in text.split():
            if word in weapons_list:
                weapon = word
                break
        return weapon
















