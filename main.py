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
                            if (size <= 3):
                print("Number of queens should be bigger or equal to 4!\n")
                continue
        
            while True: 
                chooseAlgorithm=input('Choose the algorithm (BFS - for Breadth First Search or DFS for Depth First Search): ').lower()
                n_queens = NQueens(size)
                if(chooseAlgorithm=="bfs"):
                    while True: 
                        print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower()
                        bfs_solutions = n_queens.solve_bfs()

