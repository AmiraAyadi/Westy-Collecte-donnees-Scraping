from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time
import json
import pypyodbc

politiciens=[
"François Fillon",
"Nicolas Dupont-Aignan",
"Michèle Alliot-Marie",
"Marine Le Pen",
"François Bayrou",
"Bastien Faudot",
"Manuel Valls",
"Arnaud Montebourg",
"Benoît Hamon",
"Sylvia Pinel",
"François de Rugy",
"Vincent Peillon" ,
"Yannick Jadot",
"Jean-Luc Mélenchon",
"Nathalie Arthaud",
"Philippe Poutou",
"Emmanuel Macron",
"François Asselineau",
"Jacques Cheminade",
"Jean Lassalle",
"Henry de Lesquen",
"Rama Yade",
"Charlotte Marchandise"
]

userID=[]

auth = tweepy.OAuthHandler("CjqvqcQ1JftvNHTWM7JJbuYDY", "jUNM4CoYq3VuovM0SlP2L9aSJVqQ5lv1yc3velhwOMxFjUNY0Z")
auth.set_access_token("824709465089966080-I8U8XMxFZUrjAZ0IGpBYuoZKcBFNW1D", "OnGOKJV7MNWCHDZzTw3MaFeAUKJDn6WQdzGmGtIIf6gdQ")

api = tweepy.API(auth)
for politicien in politiciens:
    public_tweets = tweepy.Cursor(api.search, q=politicien, lang='fr').items(50)
    with open("d.txt", 'a') as f:
        for tweet in public_tweets:
            userID.append(tweet.user.id_str)
            json.dump(tweet._json, f)
            f.write("\n")
print(userID)


