from twitterscraper import query_tweets
import pandas as pd
import datetime as dt

begin_date = dt.date(2020,1,1)
end_date = dt.date(2020,5,25)

tweets = query_tweets('from:realDonaldTrump', begindate = begin_date, enddate = end_date, limit = 10000)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_excel(r'C:\Users\User\Desktop\usa.xlsx')

#did the same for the following accounts
#ScottMorrisonMP - australia
#jairbolsonaro - brazil
#JustinTrudeau - canada
#EmmanuelMacron - france
#narendramodi - india
#GiuseppeConteIT - italy
#sanchezcastejon - spain
#BorisJohnson - uk
#realDonaldTrump - usa

#also checked for Germany but Angela Merkel is not on twitter
#and for New Zealand, even though Jacinda Ardern is on twitter,
#she barely uses it; <5 tweets in the past 5 months. 


