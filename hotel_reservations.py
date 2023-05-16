from builtins import map

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

hotels = pd.read_csv("hotel_reservations.txt")
print(hotels.head(), '\n')

print(hotels.info(), '\n')

print(hotels['type_of_meal_plan'].value_counts(), '\n')
type_of_meal_plan_mapping = {'Not Selected': 0, 'Meal Plan 1': 1, 'Meal Plan 2': 2, 'Meal Plan 3': 3}
hotels['type_of_meal_plan'] = hotels['type_of_meal_plan'].map(type_of_meal_plan_mapping)

print(hotels['room_type_reserved'].value_counts(), '\n')
room_type_reserved_mapping = {'Room_Type 1': 1, 'Room_Type 2': 2, 'Room_Type 3': 3, 'Room_Type 4': 4, 'Room_Type 5': 5, 'Room_Type 6': 6, 'Room_Type 7': 7, }
hotels['room_type_reserved'] = hotels['room_type_reserved'].map(room_type_reserved_mapping)

print(hotels['market_segment_type'].value_counts(), '\n')
market_segment_type_mapping = {'Online': 1, 'Offline': 2, 'Corporate': 3, 'Complementary': 4, 'Aviation': 5}
hotels['market_segment_type'] = hotels['market_segment_type'].map(market_segment_type_mapping)

print(hotels['booking_status'].value_counts(), '\n')
booking_status_mapping = {'Not_Canceled': 0, 'Canceled': 1}
hotels['booking_status'] = hotels['booking_status'].map(booking_status_mapping)

print(hotels.isna().sum(), '\n')

sns.heatmap(hotels.corr(numeric_only=True), annot=True)
plt.show()

hotels = hotels.drop('Booking_ID', axis=1)
X = hotels.iloc[:, :17]
y = hotels.iloc[:, 17]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rf = RandomForestClassifier(max_depth=40, n_estimators=220, criterion='gini')
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

accuracy_rf = accuracy_score(y_test, y_pred)
print('Accuracy: ', accuracy_rf, '\n')

print(classification_report(y_test, y_pred, labels=[1, 0]))

confusion_matrix = confusion_matrix(y_pred, y_test)
print('Confusion matrix: \n', confusion_matrix)
sns.heatmap(confusion_matrix, annot=True, fmt='d')
plt.title('Confusion matrix')
plt.show()
