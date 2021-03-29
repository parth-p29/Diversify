from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class AzureAnalyticsClient():

    def __init__(self):

        self.client = TextAnalyticsClient(
            endpoint="https://diversifysentiment.cognitiveservices.azure.com/",
            credential=AzureKeyCredential("7ab3b52e66264693a32402ef642bfa4f"))
    
    def sentiment_analysis(self, lyrics):

        output_dict = lambda **data: data

        documents = [lyrics]
        response = self.client.analyze_sentiment(documents=documents)[0]

        overall_sentiment = response.sentiment
        positive = response.confidence_scores.positive
        negative = response.confidence_scores.negative
        neutral = response.confidence_scores.neutral

        return output_dict(overall=overall_sentiment, positive=positive, negative=negative, neutral=neutral)

    def key_phrase_extraction(self, lyrics):

        documents = [lyrics]
        response = self.client.extract_key_phrases(documents = documents)[0]

        return response.key_phrases