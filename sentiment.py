from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "7ab3b52e66264693a32402ef642bfa4f"
endpoint = "https://diversifysentiment.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

def sentiment_analysis_example(client):

    documents = ["Feeling good, like I should\r\nWent and took a walk around the neighborhood\r\nFeeling blessed, never stressed\r\nGot that sunshine on my sunday best\r\nEveryday can be a better day despite the challenge\n\nAll you gotta do is leave it better than you found it\n\nIt's gonna get difficult to stand but hold your balance\n\nI just say whatever cause there is no way around it cause\n\n\n\nEveryone falls down sometimes\n\nBut you just gotta know it'll all be fine\n\nIt's ok, uh-huh\n\nIt's ok, it's ok\n\n\n\nFeeling good, like I should\n\nWent and took a walk around the neighborhood\n\nFeeling blessed, never stressed\n\nGot that sunshine on my sunday best\n\n\n\nSomedays you wake up and nothing works you feel surrounded\n\nGotta give your feet some gravity to get you grounded\n\nKeep good things inside your ears just like the waves and sound did\n\nAnd just say whatever cause there is no way around it\n\n\n\nEveryone falls down sometimes\n\nBut you just gotta know it'll all be fine\n\nIt's ok, uh-huh\n\nIt's ok, it's ok\n\n\n\nFeeling good, like I should\n\nWent and took a walk around the neighborhood\n\nFeeling blessed, never stressed\n\nGot that sunshine on my sunday best\n\n\n\nFeeling good, like I should\n\nWent and took a walk around the neighborhood\n\nFeeling blessed, never stressed\n\nGot that sunshine on my sunday best"]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))

client = authenticate_client()     
print(sentiment_analysis_example(client))