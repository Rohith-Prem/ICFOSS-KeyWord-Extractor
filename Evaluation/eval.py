from sklearn.model_selection import KFold
from numpy import array

f = open("/home/rohith/ICFOSS-KeyWord-Extractor/CRF/train.txt", 'r')
dataset = f.read()
datalist = dataset.split('\n')
dataarray = array(datalist)
print(dataarray)
labels = array(["B_K", "N_K"])
kf = KFold(n_splits=10)
for train, test in kf.split(dataarray):
    print("TRAIN:", train, "TEST:", test)
    #X_train, X_test = dataarray[train_index], dataarray[test_index]
    #y_train, y_test = labels[train_index], labels[test_index]

