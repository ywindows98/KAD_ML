from kad import KAD
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from combinations import elems_comp


def print_rule(rule, columns):
    attributes = rule[0]
    target_class = rule[1]
    rule_string = "Rule: IF"
    noa=0
    for i in range(len(attributes)):
        if attributes[i] != None:
            noa+=1
            if noa>1:
                rule_string += f" AND {columns[i]}:{attributes[i]}"
            else:
                rule_string += f" {columns[i]}:{attributes[i]}"

    rule_string += f" THEN CLASS:{target_class}"

    print(rule_string)

shrooms = pd.read_csv('dataset/mushrooms.csv', usecols=['class', 'cap-shape','cap-surface', 'cap-color', 'gill-size', 'stalk-shape', 'veil-type', 'ring-number', 'population'])
shrooms_sample = shrooms.groupby('class').sample(n=500, random_state=123)
# shrooms_sample

X = shrooms_sample[shrooms_sample.columns.drop('class')]
df_columns = X.columns
y = shrooms_sample[['class']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123, stratify=y)

kad = KAD(X_train, y_train)
kad.process()

print(f"{'='*40}")
print("RULES:")
for rule in kad.rules:
    print_rule(rule, df_columns)

y_pred = []
kad.rules.sort(key=lambda x: x[-1], reverse=True)
for elem in np.array(X_test):
    for rule in kad.rules:
        if elems_comp(elem, rule[0]):
            y_pred.append(rule[1])
            break

n = len(y_pred)
print(f"{'='*40}")
print("CONFUSION MATRIX:")
print(confusion_matrix(y_test[:n], y_pred))
print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test[:n], y_pred))