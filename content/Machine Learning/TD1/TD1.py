import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.svm import SVC
import imageio
from IPython.display import Image, display

def afficher_graphique(
    X, y,                        # X = input data, y = associated classes
    titre="",                    # Figure title, default: empty
    xlabel="Feature 1",          # x-axis label, default: 'Feature 1'
    ylabel="Feature 2",          # y-axis label, default: 'Feature 2'
    w0=None, w1=None, w2=None,   # w0 and w=[w1,w2]^T, parameters defining the separating hyperplane
    svm=None,                    # trained SVM output, used to highlight the margin
    support=None,                # matrix containing support vectors (each row = one support vector)
):
    fig, ax = plt.subplots(1, 1, figsize=(12, 5))
    
    # Data
    ax.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Class 0')
    ax.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Class 1')
    
    # Decision boundary
    if w0 and w1 and w2 is not None:
        x_values = np.array([X[:, 0].min(), X[:, 0].max()])
        y_values = -(w0 + w1 * x_values) / w2
        ax.plot(x_values, y_values, 'g-', label='Decision boundary')
        
    # Support vectors and margin visualization
    if svm and support is not None:
        xx, yy = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 100),
                             np.linspace(X[:, 1].min(), X[:, 1].max(), 100))
        Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.3, colors=['gray', 'gray', 'gray'])
        ax.scatter(support[:, 0], support[:, 1], s=100,
                   facecolors='none', edgecolors='green', label='Support vectors')
        
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    fig.suptitle(titre, fontsize=16, y=.95)
    plt.show()

# Loading of the dataset
data = pd.read_csv('data_class_1.csv')
X = data.iloc[:, :2].to_numpy() # input data
y = data.iloc[:, 2].to_numpy() # class of the data
# afficher_graphique(X, y, titre="Data used") # display of the data


# Create and train the SVM
clf = SVC().fit(X, y)

# Display the result
# afficher_graphique(X, y, titre="Result", svm=clf, support=clf.support_vectors_)

# Display coordinates of support vectors
print(clf.support_vectors_)

# Display the number of support vectors per class
print(clf.support_vectors_.shape)
coef = clf.coef0
print(coef)

# afficher_graphique(
#     X, y,
#     w0=clf.coef_[0][0], w1=, w2=,
#     svm=clf, support=clf.support_vectors_,
# )
