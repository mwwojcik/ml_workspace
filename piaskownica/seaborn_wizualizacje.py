import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)



# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
plt.show()



iris = sns.load_dataset("iris")
iris.head()
plt.show()

sns.pairplot(iris, hue='species', size=2.5);
plt.show()


