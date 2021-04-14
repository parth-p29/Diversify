from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class AzureAnalyticsClient():

    def __init__(self):

        self.client = TextAnalyticsClient(
            endpoint="YOUR AZURE ENDPOINT",
            credential=AzureKeyCredential("YOUR AZURE KEY"))
    
    def sentiment_analysis(self, lyrics):

        output_dict = lambda **data: data

        documents = [lyrics]

        try:
            response = self.client.analyze_sentiment(documents=documents)[0]
            overall_sentiment = response.sentiment
            positive = response.confidence_scores.positive
            negative = response.confidence_scores.negative
            neutral = response.confidence_scores.neutral

            return output_dict(overall=overall_sentiment, positive=positive, negative=negative, neutral=neutral)
        
        except:
            return output_dict(overall="Lyrics not able to be analyzed", positive=100, negative=100, neutral=100)

    def key_phrase_extraction(self, lyrics):
        
        try:
            documents = [lyrics]
            response = self.client.extract_key_phrases(documents = documents)[0]
            return response.key_phrases
        
        except:
            return ['none']
