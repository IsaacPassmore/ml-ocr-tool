import csv
import sys, getopt

def main(argv):
  print("number of args: " + str(len(sys.argv)))
  inputfile = ""
  outputfile = ""


  training_blobs = [];
  letters = [];
  a=[];
  b=[];
  c=[];
  d=[];
  e=[];
  f=[];
  g=[];
  h=[];
  i=[];
  j=[];
  k=[];
  l=[];
  m=[];
  n=[];
  o=[];
  p=[];
  q=[];
  r=[];
  s=[];
  t=[];
  u=[];
  v=[];
  w=[];
  x=[];
  y=[];
  z=[];

  i_data=[];

  try: 
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print("check.py -i <inputfile> -o <outputfile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == "-h":
      print("check.py -i <inputfile> -o <outputfile>")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
  #filename = "llu-1-data.txt"
  with open(inputfile,"r") as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter = ',')
    for row in csvReader:
      letters.append(row[-1])
      if int(row[-1]) == 1:
        a.append(row[-1])
      elif int(row[-1]) == 2:
        b.append(row[-1])
      elif int(row[-1]) == 3:
        c.append(row[-1])
      elif int(row[-1]) == 4:
        d.append(row[-1])
      elif int(row[-1]) == 5:
        e.append(row[-1])
      elif int(row[-1]) == 6:
        f.append(row[-1])
      elif int(row[-1]) == 7:
        g.append(row[-1])
      elif int(row[-1]) == 8:
        h.append(row[-1])
      elif int(row[-1]) == 9:
        i.append(row[-1])
        i_data.append(len(row[:-1]))
      elif int(row[-1]) == 10:
        j.append(row[-1])
      elif int(row[-1]) == 11:
        k.append(row[-1])
      elif int(row[-1]) == 12:
        l.append(row[-1])
      elif int(row[-1]) == 13:
        m.append(row[-1])
      elif int(row[-1]) == 14:
        n.append(row[-1])
      elif int(row[-1]) == 15:
        o.append(row[-1])
      elif int(row[-1]) == 16:
        p.append(row[-1])
      elif int(row[-1]) == 17:
        q.append(row[-1])
      elif int(row[-1]) == 18:
        r.append(row[-1])
      elif int(row[-1]) == 19:
        s.append(row[-1])
      elif int(row[-1]) == 20:
        t.append(row[-1])
      elif int(row[-1]) == 21:
        u.append(row[-1])
      elif int(row[-1]) == 22:
        v.append(row[-1])
      elif int(row[-1]) == 23:
        w.append(row[-1])
      elif int(row[-1]) == 24:
        x.append(row[-1])
      elif int(row[-1]) == 25:
        y.append(row[-1])
      elif int(row[-1]) == 26:
        z.append(row[-1])
      
  print("a: " + str(len(a)))
  print("b: " + str(len(b)))
  print("c: " + str(len(c)))
  print("d: " + str(len(d)))
  print("e: " + str(len(e)))
  print("f: " + str(len(f)))
  print("g: " + str(len(g)))
  print("h: " + str(len(h)))
  print("i: " + str(len(i)))
  print("j: " + str(len(j)))
  print("k: " + str(len(k)))
  print("l: " + str(len(l)))
  print("m: " + str(len(m)))
  print("n: " + str(len(n)))
  print("o: " + str(len(o)))
  print("p: " + str(len(p)))
  print("q: " + str(len(q)))
  print("r: " + str(len(r)))
  print("s: " + str(len(s)))
  print("t: " + str(len(t)))
  print("u: " + str(len(u)))
  print("v: " + str(len(v)))
  print("w: " + str(len(w)))
  print("x: " + str(len(x)))
  print("y: " + str(len(y)))
  print("z: " + str(len(z)))
  print("i_data: ")
  print(i_data)


  print('Input file is ' + inputfile)
if __name__ == "__main__":
  main(sys.argv[1:])
