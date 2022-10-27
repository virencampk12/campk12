from textblob import TextBlob
a = TextBlob("I lik to plaay gmaes")
a = a.correct()
print(a)