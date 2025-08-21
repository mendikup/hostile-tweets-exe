import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from app.helpers import get_weapon_list

class Processor:

    def __init__(self,data):
        nltk.download('vader_lexicon')  # Compute sentiment labels
        self.analaize = SentimentIntensityAnalyzer()
        self.data = pd.DataFrame(data)

    def express_sentiment(self):
        self.data['sentiment'] = self.data['Text'].apply(self.get_sentiment_score)


    def get_sentiment_score(self,txt):
        score = self.analaize.polarity_scores(txt)
        compound = score['compound']
        if compound <= -0.5:
            return "negative"
        elif 0.5 < compound > -0.5 :
            return "neutral"
        else:
            return "positive"



    def find_rarest_word_per_twwet(self):
        text_column = self.data['Text']
        rarest_word = text_column.map(lambda x: pd.Series(x.split()).value_counts().idxmin())
        self.data['the_rarest_word'] = rarest_word



    def weapons_detected(self):
        self.data['weapons_detected'] = self.data['Text'].apply(Processor.check_weapon_in_text)



    def get_df_as_dictionary(self):
        return self.data.to_dict(orient="records")




    @staticmethod
    def check_weapon_in_text(text):
        weapons_list = get_weapon_list()
        weapon = ""
        for word in text.split():
            if word in weapons_list:
                weapon = word
                break
        return weapon















