import re
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

messages_data = pd.read_csv("data/SMSSpamCollection", sep='\t',
                            names=["label", "message"])

ps = PorterStemmer()
corpus = []

for i in range(len(messages_data)):
    review = re.sub("[^a-zA-Z]", " ", messages_data["message"][i]).lower()
    review = review.split()

    review = [ps.stem(word) for word in review if not word in stopwords.words("english")]
    review = " ".join(review)
    corpus.append(review)

cv = CountVectorizer(max_features=5000)
X = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(messages_data["label"])
y = y.iloc[:, 1].values # ignore 'ham' column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=135)

spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred = spam_detect_model.predict(X_test)
print("Test metrics")
print(classification_report(y_test, y_pred), "\n\n")

y_pred = spam_detect_model.predict(X_train)
print("Training metrics")
print(classification_report(y_train, y_pred), "\n\n")
