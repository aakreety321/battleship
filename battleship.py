#this is a multidimensional container defined as grid
grid = [
    ['_', '_', 'x'],
    ['_', '_', '_'],
    ['_', 'x', 'x']
]
#here we are printing the grid to show user initially defined area if they are targeted or not
print(grid[0])
print(grid[1])
print(grid[2])
#now we will ask input from user about coordinates they want to target
coordinates=input("Enter target coordinates: ")
#split() function used to differentiate two different input
split=coordinates.split()
row=int(split[0])
column=int(split[1])
#checking condition if user gives valid coordinate from 0-2
if 0<=row<3 and 0<=column<3:
    if grid[row][column] =="_":
        grid[row][column]="x"
        print("Attacked sucessfully!")
        print(grid[0])
        print(grid[1])
        print(grid[2])
    elif grid[row][column]=="x":
        print("Already hit!")
        print(grid[0])
        print(grid[1])
        print(grid[2])
    else:
        print("Invalid input!")
else:
    print("out of bound!")