import matplotlib.pyplot as plt 
import numpy as np
from sklearn.datasets import make_classification

# Generating data
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_classes=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=1234
)

fig, ax = plt.subplots()
ax.scatter(X[:,0], X[:,1], c=y)

plt.title("Some data distribution")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend()

fig
