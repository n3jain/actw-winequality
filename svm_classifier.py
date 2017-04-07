import preprocessor

train_data, test_data, labels_train, labels_test = preprocessor.prepare_wine_type_data()

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='linear', C=10)
clf.fit(train_data, labels_train)
labels_pred = clf.predict(test_data)

print accuracy_score(labels_test, labels_pred)
