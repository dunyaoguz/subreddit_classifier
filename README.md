# subreddit_classifier

## Executive Summary

In this project, I scraped data from two of my favorite subreddits, Shower Thoughts and Crazy Ideas, and built a classifier that can identify which of the two subreddits a given post belongs to, using a variety of Natural Language Processing techniques on the posts' titles.

**Glossary**:

* *Subreddit*: A public web forum with a niche focus, hosted by Reddit, where users discuss related concepts via posts and comments.

* *Shower Thought:* A seemingly mundane detail about the world, that becomes weird and interesting when viewed from a slightly different perspective while in the shower, such as:
  
  > If you're living without having studied anatomy or medicine you're actually using your body without reading its user manual.
  
  > What are snails even trying to do?
  
  > Moms and dads work hard to buy a nice house and send their kids to good schools so that their kids can get a good job, work hard to buy a nice house and send their kids to good schools, so that their grandchildren can get good jobs, buy nice houses and send their kids to good schools.

* *Crazy Idea*: Unconventional, eccentric ideas of things, such as:

  > Tinder but I instead of matching with people it just shows you how many people swiped left on you. No messages or anything

  > A program that everyone can download that randomly browses Amazon, Facebook, and Google on autopilot so that they would have to collect tons of useless data from websites you would never visit or products you would never buy, making data collection unreliable and pointless.
  
  > Soccer would be a lot more interesting if you could get more points for scoring goals from afar like 3 pointers in basketball

As can be seen from these examples, the content of these subreddits is pretty similar: they are both extremely random, and written in a manner that can be considered congruent. The difference between a shower thought and a crazy idea is highly nuanced, such that even a human may have a difficult time distinguishing between the two. ...Can a machine?

## Highlights

- Scraped 3432 Shower Thoughts and Crazy Ideas posts from Reddit's API using the `requests` library 
- Analysed the sentiment polarity of the posts with `TextBlob` 
- Modelled post topics using `Latent Dirichlet Allocation`
- Created 1-dimensional document embeddings using `Doc2Vec` from `gensim`
- Tokenized and lemmatized words in each post based on their part of speech tag with `nltk`
- Vectorized each post with `Count Vectorizer` and `Term Frequency–Inverse Document Frequency Vectorizer`
- Classified posts using `Logistic Regression`, `Multinomial Naive Bayes`, `Gradient Boosting` and `Random Forest` algorithms, compared them based on their `accuracy` and `roc-auc score`
