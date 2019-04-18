import numpy as np
import csv

class SudokuSolver:
    def __init__(self):
        list_of_lists = []
        with open('sudokuinput.csv','r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                list_of_lists.append([int(x) for x in row if x]) # last element of rows is empty
        self.vals = np.asarray(list_of_lists) # 9X9 , 2d array
        self.flags = np.zeros((9,9,9)) #flags for 9 possible entries in the 9X9 2d array

    def __set_flags(self, x, y, digit):
        if self.vals[x][y] == 0:
            self.vals[x][y] = digit
        qx, qy = x//3, y//3
        for i in range(0, 9):
            self.flags[i][y][digit-1] = 1
            self.flags[x][i][digit-1] = 1
            self.flags[x][y][i] = 1
            r, c = divmod(i, 3)
            self.flags[3*qx+r][3*qy+c][digit-1] = 1
        
    def initial_set_flags(self):
        for indices in np.ndindex(self.vals.shape):
            x, y = indices
            digit = self.vals[x][y]
            if digit > 0:
                self.__set_flags(x,y,digit)

    def check_completion(self):
        for indices in np.ndindex(self.vals.shape):
            x,y = indices
            if int(sum(self.flags[x][y])) == 8:
                for digit in range(1,10):             
                    if self.flags[x][y][digit-1] == 0:
                        break
                self.__set_flags(x, y, digit)

    def end_reached(self):
        for indices in np.ndindex(self.flags.shape):
            x,y,z = indices
            if self.flags[x][y][z] == 0:
                return False
        return True

if __name__ == '__main__':
    ss = SudokuSolver()
    ss.initial_set_flags()
    while(ss.end_reached() == False):
        ss.check_completion()
    print(ss.vals)