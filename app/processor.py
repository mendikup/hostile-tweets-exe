import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from app.helpers import get_weapon_list

class Processor:

    def __init__(self,data):
        nltk.download('vader_lexicon')  # Compute sentiment labels
        self.analaize = SentimentIntensityAnalyzer()
        self.data = pd.DataFrame(data)


    def run_processing(self):
        self.find_rarest_word_per_tweet()
        self.express_sentiment()
        self.weapons_detected()



    def express_sentiment(self):
        self.data['sentiment'] = self.data['Text'].apply(self._get_sentiment_score)


    def _get_sentiment_score(self,txt):
        score = self.analaize.polarity_scores(txt)
        compound = score['compound']
        if compound <= -0.5:
            return "negative"

        elif compound >= 0.5:
            return "positive"
        else:
            return "neutral"


    def find_rarest_word_per_tweet(self):
        # Ensure the required column is present
        if 'Text' not in self.data.columns:
            raise KeyError("Expected 'Text' column in input data")

        text_column = self.data['Text'].fillna("").astype(str).str.lower()
        rarest_word = text_column.map(
            lambda text: pd.Series(text.split()).value_counts().idxmin()
        )
        self.data['the_rarest_word'] = rarest_word




    def weapons_detected(self):
        if 'Text' not in self.data.columns:
            raise KeyError("Expected 'Text' column in input data")
        self.data['weapons_detected'] = (
            self.data['Text']
            .fillna("")
            .astype(str)
            .apply(self._check_weapon_in_text)
        )



    def get_df_as_dictionary(self):
        return self.data.to_dict(orient="records")





    def _check_weapon_in_text(self,text):
        weapons_list = get_weapon_list()
        weapon = ""
        for word in text.split():
            if word in weapons_list:
                weapon = word
                break
        return weapon















