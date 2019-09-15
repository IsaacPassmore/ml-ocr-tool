import sys, getopt, csv, itertools, pickle
import numpy as np
from sklearn import neighbors, linear_model, model_selection
from joblib import dump, load
def main(argv):
  print("number of args: " + str(len(sys.argv)))
  inputfile = ""
  outputfile = ""

  #Setup Parameters
  input_layer_size = 400 #20x20 input images of letters
  letter_labels = 26 # 26 labels from a to z

  #Load Training Data
  print("Loading and Visualizing Data ...\n")

  X = [];
  y = [];

  try: 
    opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile=","predict","train","fulltrain","test"])
  except getopt.GetoptError:
    print("check.py -i <inputfile> -o <outputfile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == "-h":
      print("check.py -i <inputfile> -o <outputfile> --train --fulltrain --test")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
    elif opt in ("--train"):
      run = "train"
    elif opt in ("--fulltrain"):
      run = "fulltrain"
    elif opt in ("--test"):
      run = "test"
    elif opt in ("--predict"):
      run = "predict"
  with open(inputfile,"r") as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter = ',')
    for row in csvReader:
      #training data stored in arrays X, y
      X.append(row[0:-1])
      y.append(row[-1])

    X = np.array(X,dtype=np.float32)
    y = np.array(y,dtype=np.float32)

  def translate(digits):
    text = []
    for i in range(len(digits)):
      if digits[i] == 1:
        text.append("a")
      elif digits[i] == 2:
        text.append("b")
      elif digits[i] == 3:
        text.append("c")
      elif digits[i] == 4:
        text.append("d")
      elif digits[i] == 5:
        text.append("e")
      elif digits[i] == 6:
        text.append("f")
      elif digits[i] == 7:
        text.append("g")
      elif digits[i] == 8:
        text.append("h")
      elif digits[i] == 9:
        text.append("i")
      elif digits[i] == 10:
        text.append("j")
      elif digits[i] == 11:
        text.append("k")
      elif digits[i] == 12:
        text.append("l")
      elif digits[i] == 13:
        text.append("m")
      elif digits[i] == 14:
        text.append("n")
      elif digits[i] == 15:
        text.append("o")
      elif digits[i] == 16:
        text.append("p")
      elif digits[i] == 17:
        text.append("q")
      elif digits[i] == 18:
        text.append("r")
      elif digits[i] == 19:
        text.append("s")
      elif digits[i] == 20:
        text.append("t")
      elif digits[i] == 21:
        text.append("u")
      elif digits[i] == 22:
        text.append("v")
      elif digits[i] == 23:
        text.append("w")
      elif digits[i] == 24:
        text.append("x")
      elif digits[i] == 25:
        text.append("y")
      elif digits[i] == 26:
        text.append("z")
    
    return text

  def train(test_size):

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=test_size)
    
    print("Building Model")
    LR_model = linear_model.LogisticRegression(solver='lbfgs',max_iter=10000,multi_class='multinomial')
    KNN_model = neighbors.KNeighborsClassifier()

    print("Fitting Model")
    LR_model.fit(X_train,y_train)
    KNN_model.fit(X_train,y_train) 

    LR_save_file = "lr-ll-model.txt"
    KNN_save_file = "knn-ll-model.txt"

    pickle.dump(LR_model, open(LR_save_file, 'wb'))
    print("LogisticRegression Model saved as: " + LR_save_file)
    pickle.dump(KNN_model, open(KNN_save_file, 'wb'))
    print("K-Nearest Neighbor Model saved as: " + KNN_save_file)

    print("LogisticRegression score: %f" % LR_model.score(X_test,y_test))
    print('KNN score: %f' %KNN_model.score(X_test,y_test))
  
  if run == "train":
    test_size = 0.1
    train(test_size)

  if run == "fulltrain":
    test_size = 0.000001
    train(test_size)

  if run == "test":
    y_given_text = translate(y)
    print("Given:                           %s" % y_given_text)

    loaded_LR_model = pickle.load(open("lr-ll-model.txt","rb"))
    loaded_KNN_model = pickle.load(open("knn-ll-model.txt","rb"))
    LR_y_predict = loaded_LR_model.predict(X)
    LR_y_predict_text = translate(LR_y_predict)
    print("Logistical Regression Predicted: %s" % LR_y_predict_text)
    KNN_y_predict = loaded_KNN_model.predict(X)
    KNN_y_predict_text = translate(KNN_y_predict)
    print("K-Nearest Neighbor Predicted:    %s" % KNN_y_predict_text)

    LR_grade = 0
    KNN_grade = 0
    for i in range(len(y)):
      if LR_y_predict[i] == y[i]:
       LR_grade += 1
      if KNN_y_predict[i] == y[i]:
       KNN_grade += 1
    print("Logistical Regression correctly predicted %s out of %s = %s percent" % (LR_grade, len(y), float(LR_grade/len(y)*100)))
    print("K-Nearest Neighbor correctly predicted %s out of %s = %s percent" % (KNN_grade, len(y), float(KNN_grade/len(y)*100)))
    
if __name__ == "__main__":
  main(sys.argv[1:])
