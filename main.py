from n_queens import NQueens
import sys
import time 

def main():
    print('.: N-Queens Problem :.') 
    while True: 
        try:
            userInput = input("Please enter the number of 'queens' or 'exit' to stop the program: ").lower()
            if(userInput=="exit"):
                print("Program is stopping...")
                sys.exit()