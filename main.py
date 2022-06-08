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
                        start = time.time()
                        time.process_time()
                        bfs_solutions = n_queens.solve_bfs()
                        elapsed = time.time() - start

                        if(print_solutions=='y'):
                                for i, solution in enumerate(bfs_solutions):
                                    print('BFS Solution %d:' % (i + 1))
                                    n_queens.print(solution)
                                print('\nTotal BFS solutions: %d\n' % len(bfs_solutions))
                                break

                        elif(print_solutions=='n'):
                            print('\nTotal BFS solutions: %d\n' % len(bfs_solutions))
                            break

                        else: 
                            print('You should only type Y or N!\n') 
                    break     

                    
                    
                     elif(chooseAlgorithm=="dfs"):
                     while True: 
                        print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() 
                        start = time.time()
                        time.process_time()
                        dfs_solutions = n_queens.solve_dfs()
                        elapsed = time.time() - start

                        if(print_solutions=='y'):
                            for i, solution in enumerate(dfs_solutions):
                                print('DFS Solution %d:' % (i + 1))
                                n_queens.print(solution)
                            print('\nTotal DFS solutions: %d\n' % len(dfs_solutions))
                            break
                            
                             elif(print_solutions=='n'):
                            print('\nTotal DFS solutions: %d\n' % len(dfs_solutions))
                            break
                        
                        else: 
                            print('You should only type Y or N!\n')
                     break
                            
                else:
                    print('You should only type BFS or DFS!\n')

            minutes = int(elapsed//60)
            hours = int(elapsed // 3600)
            print("Time: ", hours,":",minutes,":",(round(elapsed, 4))%60)
                
        except ValueError:
            print("You should only enter an integer number of queens or exit to stop the program!\n")
    
if __name__ == '__main__':
    main()
