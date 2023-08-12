import os
from datetime import date

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

SEED = 20
np.random.seed(SEED)
MODEL_BASE_PATH = "model/modelo"



def train_model():
    file = [item for item in os.listdir() if item.endswith('.csv')][0]

    df = pd.read_csv(file)
    y = df["2urvived"]
    x = df.drop("2urvived", axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.27, stratify=y)

    # Modelo KNN
    model = KNeighborsClassifier(metric="euclidean")
    model.fit(x_train, y_train)

    baseline = np.ones_like(y_test)
    accuracy_baseline = accuracy_score(y_test, baseline)*100

    x_test = x_test.fillna(0)
    contiguous_x = np.ascontiguousarray(x_test)
    previsions = model.predict(contiguous_x)

    model_accuracy = accuracy_score(y_test, previsions)*100

    # Exportar o modelo
    if not os.path.exists(MODEL_BASE_PATH):
        os.makedirs(MODEL_BASE_PATH)
    joblib.dump(model, f"{MODEL_BASE_PATH}/modelo{str(date.today())}.joblib")

    print(classification_report(y_test, previsions))

    return {
        "accuracy_baseline": accuracy_baseline,
        "model_accuracy": model_accuracy
        }
