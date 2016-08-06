# Twift-Bay

Project for Major League Hacking Prime Spring Finale 2016

### Description

Provide E-Bay Gift suggestions based on the user's Twitter Account.

### Technology Stack

- [Ember](http://emberjs.com/) (frontend)
- [Flask](http://flask.pocoo.org/) (api server)
- [IBM Bluemix](https://personality-insights-livedemo.mybluemix.net/) (personality insight)
- [Twitter API](https://dev.twitter.com/overview/documentation) (tweets)
- [E-Bay API](https://go.developer.ebay.com/) (products)

### Todo

- Using E-Bay's API, get a list of popular products based on rating 
- Get the user reviews of those products, and concatenate them into a single blob of text
- Perform a personality insight analysis based on the blob of reviews and save the results in a database
- Use Twitter's API to get the most recent 100 tweets given a username and concatenate them into a single blob of text
- Based on the analysis, suggest the top 10 most likely products that the user will like (buy) given a price range
- Display the results in a interactive and impressive manner
- Add the ability to check the probability that a given product on E-Bay will be liked by a given user. The product will be a added to the database if its new.


### Authors
- [Hanchen Wang](https://github.com/g3wanghc)
- [Kyle Zhou](https://github.com/kylemsguy)