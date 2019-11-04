import pickle

nickList = open(r"ids.txt",'rb')
nicks = pickle.load(nickList)
nickList.close()

print("Registarted users : \n\n",nicks)