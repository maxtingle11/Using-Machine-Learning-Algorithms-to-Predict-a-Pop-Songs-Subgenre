"""Helper scripts for 'Predicting Pop Subgenres'"""


import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def print_metrics(labels, preds, title=None):
    '''This function prints accuracy score of two series (labels, predictions)'''
    print(f"{title} Accuracy Score: {accuracy_score(labels, preds)}")


def find_best_k_acc(X_train, y_train, X_test, y_test, min_k=1, max_k=50):
    '''This function takes X_train, y_train, X_test, and y_test data and 
    returns the best K value defined by best accuracy'''
    best_k = 0
    best_score = 0.0
    for k in range(min_k, max_k+1):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        preds = knn.predict(X_test)
        acc = accuracy_score(y_test, preds)
        if acc > best_score:
            best_k = k
            best_score = acc
    
    print("Best Value for k: {}".format(best_k))
    print("Accuracy: {}".format(best_score))
    

def plot_confusion_matrix(cm, classes, normalize=False, cmap=plt.cm.Greens):
    """Add Normalization Option."""
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.figure(figsize=(10,10))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize=15)
    plt.yticks(tick_marks, classes, fontsize=15)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt, ),
                 horizontalalignment="center", fontsize=18, fontweight='bold',
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label', fontsize=15)
    plt.xlabel('Predicted label', fontsize=15)
    
