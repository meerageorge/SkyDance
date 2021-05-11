#!/usr/bin/env python
import os
import fileinput

class Actions:
    # Class Variable

    # The init method or constructor
    def __init__(self, PAction, text=""):
        self.f = open("DataBase.txt", "a")
        self.f.close()
        self.PAction = PAction
        self.dataPassed = text

    def AddActionCall(self):
        print("AddAction Call")
        print(self.PAction)
        if not self.dataPassed:
            print ("Nothing Added to the file {}...!!!".format(os.path.abspath(self.f.name)))
        else:
            with open("DataBase.txt", "a") as f:
                f.write(self.dataPassed)
                f.close()
            print("Details Added to the file {}...!!!".format(os.path.abspath(f.name)))

    def WriteActionCall(self):
        print("WriteAction Call")
        print(self.PAction)
        if not self.dataPassed:
            print ("Nothing Added to the file {}...!!!".format(os.path.abspath(self.f.name)))
        else:
            with open("DataBase.txt", "w") as f:
                f.write(self.dataPassed)
                print("Details Wrote into the file {}...!!!".format(os.path.abspath(f.name)))

    def ReadActionCall(self):
        print("ReadAction Call")
        print(self.PAction)
        Fnd = 0
        try:
            with fileinput.input(files=("DataBase.txt")) as f:
                if os.path.getsize(os.path.abspath("DataBase.txt")) == 0:
                    print ("{} File is empty".format(os.path.abspath("DataBase.txt")))
                else:
                    for line in f:
                        print (line)

        except FileNotFoundError as error:
            print (error) 

# Main Code
if __name__ == "__main__":

    print("Supported Actions: Add, Write, Read, Exit")

    while True:
        val = input("\nEnter your Action: ")
        val = val.upper()

        if  val == "ADD":
            textToAdd = input("\nPass text to add to file: ")
            Act = Actions(val, textToAdd)
            Act.AddActionCall()
        elif val == "WRITE":
            textToAdd = input("\nWhat do you want to write?: ")
            Act = Actions(val, textToAdd)
            Act.WriteActionCall()
        elif val == "READ":
            Act = Actions(val)
            Act.ReadActionCall()
        elif val == "EXIT":
            print("Application Exit..!!!\n")
            break
        else:
            print("Please Enter Supported Action..!!!\n")