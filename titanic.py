import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. LOAD DATA (Updated Link)
print("1. Loading Titanic Data...")
# This is the new, working link:
url = "https://raw.githubusercontent.com/dsindy/kaggle-titanic/master/data/train.csv"
df = pd.read_csv(url)

# 2. CLEAN DATA
# Convert 'Sex' to numbers: Male=0, Female=1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Fill missing Ages with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Select inputs and answers
features = ['Pclass', 'Sex', 'Age']
X = df[features]
y = df['Survived']

# 3. TRAIN THE BRAIN
print("2. Training the AI Brain...")
model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

# 4. VISUALIZE IT
print("3. Drawing the Decision Tree...")
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=features, class_names=['Died', 'Survived'], filled=True)

plt.title("How the AI Decides Who Survives")
plt.savefig("titanic_brain.png")
print("4. SUCCESS! Saved 'titanic_brain.png'. Go look at it!")