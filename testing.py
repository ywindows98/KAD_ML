from kad import KAD
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from combinations import elems_comp


def format_rule(rule, columns):
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

    return rule_string

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
kad.rules.sort(key=lambda x: x[-1], reverse=True)
for rule in kad.rules:
    print(format_rule(rule, df_columns))

y_pred = []
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

print(f"{'='*40}")
print("INPUT YOUR OWN RECORD:")
while input("Enter 'q' to quit: ").strip() != 'q':
    user_input = []
    for column in df_columns:
        value = input(f"Enter value for attribute '{column}': ").strip()
        if not value:
            value = None
        user_input.append(value)

    if any(user_input):
        for rule in kad.rules:
            if elems_comp(user_input, rule[0]):
                print(f'By the {format_rule(rule, df_columns)}')
                print(f"The predicted class is: {rule[1]}")
                break
        else:
            print("No matching rule found.")
    else:
        print("No matching rule found.")