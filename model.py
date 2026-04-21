from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

def train(data):
    model.fit(data)

def predict(data):
    return model.predict(data)
