



 
def paths_through_maze(maze):
    current_x = 0 
    current_y = 0
    while True :
        if (current_x == 2 and current_y == 2):
            print("GOAL!!!")
            break

        elif ( current_x < 2 and maze[current_y][current_x+1] == 1):
            print("Blocked")

        elif (current_x >= 2):
            pass
        # else (maze[current_y][current_x+1] != 1):
        
        else:
            current_x += 1
            print("Right")
            
        if (current_x == 2 and current_y == 2):
           print("GOAL!!!")
           break

        elif ( current_y < 2 and maze[current_y+1][current_x] == 1):
            print("Blocked")
            
        # elif (maze[current_y+1][current_x] != 1):
        elif (current_y >= 2):
            pass
        
        else:
            current_y += 1 
            print("Down")
            
paths_through_maze([[0, 1, 0],
                    [0, 1, 1],
                    [0, 0, 0]])
# 2