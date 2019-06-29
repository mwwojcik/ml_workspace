import pandas as pd
import matplotlib.pyplot as plt

# *************
def printdf(df):
    print(df.to_string())

def headdf(df):
    print(df.head().to_string())

def raport(nazwa,wartosc):
    print('{}=>{}'.format(nazwa,wartosc))
# *************