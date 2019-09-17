# -*- coding: utf-8 -*-
import nltk
import os
import dill
from pythainlp.tokenize import word_tokenize
from pythainlp.tools import get_full_data_path

def load_data(data):
    pass

def basic_features(document):
    document_words = word_tokenize(document)
    #print(document_words)
    features = {}
    features["love"]="รัก" in  document
    features["unlove"]="เกลียด" in  document
    return features

def naive_bayes(train_data,get_features,test_data=None):
    data_train = [(get_features(text), tag) for (text, tag) in train_data]
    #print(data_train)
    classifier = nltk.NaiveBayesClassifier.train(data_train)
    if test_data!=None:
        data_test= [(get_features(text), tag) for (text, tag) in test_data]
        return (classifier,nltk.classify.accuracy(classifier, data_test))
    return (classifier,)

class model:
    def __init__(self,name,model_type="naive_bayes",train_dataset=None,test_dataset=None,path=None,features=basic_features):
        self.name=name
        self.model=None
        self.features=features
        self.train_dataset=train_dataset
        self.test_dataset=test_dataset
        self.model_type=model_type
        if self.model_type=="naive_bayes":
            self.model_type=naive_bayes
        else:
            raise NameError("Not support this model")
        if path==None:
            self.path=get_full_data_path(self.name+".pythaisa")
        else:
            self.path=os.path.join(path,self.name+".pythaisa")
        if os.path.exists(self.path):
            with open(self.path, 'rb') as file:
                self.model=dill.load(file)
        else:
            if train_dataset==None:
                raise Exception("Not found data")
    def train(self):
        self.model=self.model_type(train_data=self.train_dataset,get_features=self.features,test_data=self.test_dataset)
        with open(self.path, 'wb') as file:
            dill.dump(self.model, file)
        return True
    def predict(self,txt):
        self.temp=self.features(txt)
        return self.model[0].classify(self.temp)