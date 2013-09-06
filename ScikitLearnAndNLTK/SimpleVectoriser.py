'''
Created on Jun 18, 2013

@author: phcostello
'''


##Simple Example

from sklearn.feature_extraction.text import CountVectorizer
train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.",
"We can see the shining sun, the bright sun.")
count_vectorizer = CountVectorizer( min_df=1, stop_words='english')
count_vectorizer.fit_transform(train_set)
print "Vocabulary:", count_vectorizer.vocabulary_

# Vocabulary: {u'blue': 0, u'sun': 3, u'bright': 1, u'sky': 2}

freq_term_matrix = count_vectorizer.transform(test_set)
print freq_term_matrix.todense()

#[[0 1 1 1]
# [0 1 0 2]]
