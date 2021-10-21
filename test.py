import tweepy
from textblob import TextBlob
import os
import matplotlib.pyplot as plt

consumer_key='your consumer_key'
consumer_secret='your consumer_secret'

access_token='your access_token'
access_token_secret='access_token_secret'

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
os.system('figlet -t Report:')
user = api.me()
file=open ("o.txt","r")
opt=file.read()
public_tweets=api.search(opt,lang='en')
print("Analyze the tweets containing your word!")
print("API user info:")
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
saverp=[]
savernu=[]
savern=[]
for tweet in public_tweets:
    print("--------------------------Loaded Tweet from twitter.com-------------------------")
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print("\n        *********Analysis of this tweet : **********\n")
    a=(analysis.polarity)
    c=(analysis.polarity)
    d=(analysis.polarity)
    if(a>0):
        print("Overall tweet is POSITIVE!,Polarity value is ",a)
        saverp.append(a)
    if(c==0):
        print("Overall Tweet is Neutral!,Polarity value is ",c)
        savernu.append(c)
    if(d<0):
        print("Overall Tweet is Negative!,Polarity value is ",d)
        savern.append(d)
    b=(analysis.subjectivity)
    if(b==0):
        print("\nOverll Tweet is Very Objective!,Subjectivity value is ",b)
    if(b==1):
        print("\nOverall Tweet is Very Subjective!,Subjectivity value is ",b)
    if(b==0.5):
        print("\nOverall Tweet is Neutral towards the topic!,Subjectivity value is ",b)
    if(b<0.5):
        print("\nOverall tweet is Objective!,Subjectivity value is ",b)
    if(b>0.5):
        print("\nOverall Tweet is Subjective!, Subjectivity value is ",b)
    print("\nOverall Sentiment Analysis along with special word Analysis for this Tweet is :\n")
    print(analysis.sentiment_assessments)
    
    print("\n********************************************************************************\n\n")
x=(len(saverp))
y=(len(savernu))
z=(len(savern))
labels=['Positive Tweets','Neutral Tweets','Negative Tweets']
colors=['green','blue','red']
exp=(0.07,0,0)
j=[x,y,z]

plt.pie(j,colors=colors,labels=labels,shadow=True,explode=exp,autopct='%1.1f%%')
plt.title('Sentiment Analysis')
plt.text(-1.2243,-1.24188,'[Close this window to view Sentiment Analysis per Tweet.]')
plt.show()
