from sklearn import tree, svm
from sklearn.neighbors import KNeighborsClassifier

def convertShoeSize(shoe):
	return (((shoe+23.5) / 3) * 2.5 * 1.5) + 1.5
#[height, weight, shoe_size]

X = [[181,80,44], [177,70,43], [160,60,38], [154, 54, 37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf2 = KNeighborsClassifier()
clf3 = svm.SVC()


clf = clf.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 =  clf3.fit(X, Y)

height = int(input("Enter height: \n")) * 2.54
weight = int(input("Enter weight: \n ")) / 2.204622618
shoe_size = int(input("Enter shoe_size: \n")) 
shoe_size = convertShoeSize(shoe_size)

prediction = clf.predict([[height, weight, shoe_size]])
prediction2 = clf2.predict([[height, weight, shoe_size]])
prediction3 = clf3.predict([[height, weight, shoe_size]])

print(prediction)
print(str(prediction2))
print(prediction3)

