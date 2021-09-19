import pandas as pd
from os.path import abspath
from typing import List, Set, Dict, Tuple, Optional
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump, load


def main():
    seed = 200
    csv_path = abspath('./processedData.csv')
    df = pd.read_csv(csv_path)
    df = df.set_index('_id')
    print("total rows: ", len(df))
    # Make a train/test split using 30% test size
    X_train, X_test, y_train, y_test = train_test_split(df.loc[:, df.columns != "isGoodSong"], df.loc[:, "isGoodSong"],
                                                        test_size=0.30,
                                                        random_state=seed)
    clf = DecisionTreeClassifier(
        criterion="entropy", min_samples_leaf=40, max_depth=10, random_state=seed)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(accuracy_score(y_test, y_pred))

    dump(clf, 'model.joblib')


if __name__ == "__main__":
    main()
