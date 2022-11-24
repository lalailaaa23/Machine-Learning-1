from sklearn.neighbors import NearestCentroid

# database: gerbang logika AND
# x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1],[2,0], [2,1], [1,2], [0,2],[3,0], [3,1], [1,3], [0,3]]
y = [0,0,0,1,2,3,4,5,6,7,8,9]

# Training and classify
clf = NearestCentroid()
clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Decision Tree")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("2 0 = ", clf.predict([[2,0]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("0 2 = ", clf.predict([[0,2]]))
print ("3 0 = ", clf.predict([[3,0]]))
print ("3 1 = ", clf.predict([[3,1]]))
print ("1 3 = ", clf.predict([[1,3]]))
print ("0 3 = ", clf.predict([[0,3]]))
