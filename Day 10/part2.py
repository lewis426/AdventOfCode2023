# %%
import pandas as pd

# %%
# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# split on ('\n')
data_list = data.split("\n") 

# %%
data_list = [[*data] for data in data_list]

# %%
data_dict = {}
for idx, data in enumerate(data_list):
    data_dict[idx] = data

# %%
for idx, data in enumerate(data_dict.values()):
    if "S" in data:
        list_idx = data.index("S")
        dict_idx = idx
        break
    else:
        pass

# %%
print(f"The entry point was in row {dict_idx} and column {list_idx}")

# %%
north_list = ["|", "7", "F"]
south_list = ["|", "J", "L"]
west_list = ["-", "F", "L"]
east_list = ["-", "J", "7"]

# %%

up = dict_idx - 1
down = dict_idx + 1
left = list_idx - 1
right = list_idx + 1

route_dicts = {}

if data_dict[up][list_idx] in north_list:
    route_dicts["North"] = [(up, list_idx)]
if data_dict[down][list_idx] in south_list:
    route_dicts["South"] = [(down, list_idx)]
if data_dict[dict_idx][left] in west_list:
    route_dicts["West"] = [(dict_idx, left)]
if data_dict[dict_idx][right] in east_list:
    route_dicts["East"] = [(dict_idx, right)]

    

# %%
route_dicts

# %%
def move_further(row, col, idx, complete, num_steps):
    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    if (data_dict[row][col] in south_list) & (data_dict[up][col] in north_list) & ((up, col) not in route_dicts[idx]):
        for i in route_dicts.keys():
            if (up, col) in route_dicts[i]:
                complete = True
                print(f"Finished in {num_steps} steps")
        route_dicts[idx].append((up, col))
    elif (data_dict[row][col] in north_list) & (data_dict[down][col] in south_list)  & ((down, col) not in route_dicts[idx]):
        for i in route_dicts.keys():
            if (down, col) in route_dicts[i]:
                complete = True
                print(f"Finished in {num_steps} steps")
        route_dicts[idx].append((down, col))
    elif (data_dict[row][col] in east_list) & (data_dict[row][left] in west_list) & ((row, left) not in route_dicts[idx]):
        for i in route_dicts.keys():
            if (row, left) in route_dicts[i]:
                complete = True
                print(f"Finished in {num_steps} steps")
        route_dicts[idx].append((row, left))
    elif (data_dict[row][col] in west_list) & (data_dict[row][right] in east_list) & ((row, right) not in route_dicts[idx]):
        for i in route_dicts.keys():
            if (row, right) in route_dicts[i]:
                complete = True
                print(f"Finished in {num_steps} steps")
        route_dicts[idx].append((row, right))
    else:
        raise ValueError(f"No route found at {row}, {col}")
    
    return complete
    

# %%
complete = False
num_steps = 1
while complete == False:
    num_steps += 1
    for i in route_dicts.keys():
        complete = move_further(route_dicts[i][-1][0], route_dicts[i][-1][1], i, complete, num_steps)
        print(f"{num_steps} steps taken with {i} route at {route_dicts[i][-1]}")
        #print(route_dicts)
    #print(num_steps)

# %%
route_dicts['North'][-4:]

# %%
route_dicts['West'][-4:]

# %%
"""pipe_locations = route_dicts['North'] + route_dicts['West']
outcome_dict = {}

for row, dict in enumerate(data_dict.values()):
    for col, list in enumerate(dict):
        if (row, col) in pipe_locations:
            outcome = "Pipe"
        else:
            above = [row-1, col]
            above_complete = False
            below = [row+1, col]
            below_complete = False
            right = [row, col+1]
            right_complete = False
            left = [row, col-1]
            left_complete = False
            outcome = "Inside"

            while above_complete == False:
                if tuple(above) in pipe_locations:
                    above_complete = True
                    #print("Pipe Above")
                elif above[0] <= 0:
                    above_complete = True
                    outcome = "Outside"
                else:
                    above[0] -= 1
            while below_complete == False:
                if tuple(below) in pipe_locations:
                    below_complete = True
                    #print("Pipe Below")
                elif below[0] >= len(data_dict):
                    below_complete = True
                    outcome = "Outside"
                else:
                    below[0] += 1
            while right_complete == False:
                if tuple(right) in pipe_locations:
                    right_complete = True
                    #print("Pipe Right")
                elif right[1] >= len(data_dict[0]):
                    right_complete = True
                    outcome = "Outside"
                else:
                    right[1] += 1
            while left_complete == False:
                if tuple(left) in pipe_locations:
                    left_complete = True
                    #print("Pipe Left")
                elif left[1] <= 0:
                    left_complete = True
                    outcome = "Outside"
                else:
                    left[1] -= 1

        print(f"Space at row {row}, column {col} is defined as {outcome}")
        outcome_dict[(row, col)] = outcome"""


# %%
from collections import Counter
#Counter(outcome_dict.values())

# %%
def spread_outside(row, col, outcome_dict, num_steps):
    above = [row-1, col]
    below = [row+1, col]
    right = [row, col+1]
    left = [row, col-1]
    num_steps += 1
    
    for dir in [above, below, right, left]:
        if (dir[0] >= 0) & (dir[1] >= 0) & (dir[0]<= 139) & (dir[1]<=139):
            if tuple(dir) not in outcome_dict:
                outcome_dict[tuple(dir)] = "Outside"
                print(f"Step {num_steps}: Spreading from {row}, {col} to {dir[0]},{dir[1]} ")
                outcome_dict = spread_outside(dir[0], dir[1], outcome_dict, num_steps)

    return outcome_dict



# %%
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

# %%
pipe_locations = route_dicts['North'] + route_dicts['West']
outcome_dict = {}

for row, dict in enumerate(data_dict.values()):
    for col, list in enumerate(dict):
        if (row == 0) | (row == len(data_dict)-1) | (col == 0) | (col == len(data_dict)-1):
            if (row, col) not in pipe_locations:
                outcome_dict[(row, col)] = "Outside"
            else:
                pass
        else:
            pass
for pipe in pipe_locations:
    outcome_dict[pipe] = "Pipe"

# %%
from collections import Counter
Counter(outcome_dict.values())

# %%
for row in range(140):
    for col in range(140):
        print(row, ",", col)
        if outcome_dict[(row, col)] == "Outside":
            outcome_dict = spread_outside(row, col, outcome_dict, 0)



# %%
num_pipes = sum(1 for v in outcome_dict.values() if v == 'Pipe')
num_outside = sum(1 for v in outcome_dict.values() if v == 'Outside')
print(f"Num Pipes: {num_pipes}")
print(f"Num Outside: {num_outside}")
print(f"Num Inside: {140*140 - num_pipes - num_outside}")


# %%
### Unused below - was crashing

# %%
def check_for_pipes(row, col, direction):
    end = False
    outcome = "Inside"
    above = [row-1, col]
    below = [row+1, col]
    right = [row, col+1]
    left = [row, col-1]
    checked_list = []
    while end == False:
        if direction == "up":
            above[0] -= 1
            right[1] += 1
            left[1] -= 1

            if (outcome_dict[tuple(above)] == "Outside") | (outcome_dict[tuple(right)] == "Outside") | (outcome_dict[tuple(left)] == "Outside"):
                end = True
                outcome = "Outside"
            elif (outcome_dict[tuple(above)] in checked_list) & (outcome_dict[tuple(right)] in checked_list) & (outcome_dict[tuple(left)] in checked_list):
                end = True
            else:
                if (outcome_dict[tuple(above)] != "Pipe") & (outcome_dict[tuple(above)] not in checked_list):
                    outcome = check_for_pipes(above[0], above[1],"up")
                if (outcome_dict[tuple(left)] != "Pipe") & (outcome_dict[tuple(left)] not in checked_list):
                    outcome = check_for_pipes(left[0], left[1], "left")
                if (outcome_dict[tuple(right)] != "Pipe") & (outcome_dict[tuple(right)] not in checked_list):
                    outcome = check_for_pipes(right[0], right[1], "right")
                checked_list = checked_list + [tuple(above), tuple(right), tuple(left)]
        if direction == "down":
            below[0] -= 1
            right[1] += 1
            left[1] -= 1

            if (outcome_dict[tuple(below)] == "Outside") | (outcome_dict[tuple(right)] == "Outside") | (outcome_dict[tuple(left)] == "Outside"):
                end = True
                outcome = "Outside"
            elif (outcome_dict[tuple(below)] in checked_list) & (outcome_dict[tuple(right)] in checked_list) & (outcome_dict[tuple(left)] in checked_list):
                end = True
            else:
                if (outcome_dict[tuple(below)] != "Pipe") & (outcome_dict[tuple(below)] not in checked_list):
                    outcome = check_for_pipes(below[0], below[1], "down")
                if (outcome_dict[tuple(left)] != "Pipe") & (outcome_dict[tuple(left)] not in checked_list):
                    outcome = check_for_pipes(left[0],left[1],"left")
                if (outcome_dict[tuple(right)] != "Pipe") & (outcome_dict[tuple(right)] not in checked_list):
                    outcome = check_for_pipes(right[0], right[1], "right")
                checked_list = checked_list + [tuple(below), tuple(right), tuple(left)]
        if direction == "right":
            above[0] -= 1
            right[1] += 1
            below[0] += 1

            if (outcome_dict[tuple(above)] == "Outside") | (outcome_dict[tuple(right)] == "Outside") | (outcome_dict[tuple(below)] == "Outside"):
                end = True
                outcome = "Outside"
            elif (outcome_dict[tuple(above)] in checked_list) & (outcome_dict[tuple(right)] in checked_list) & (outcome_dict[tuple(below)] in checked_list):
                end = True
            else:
                if (outcome_dict[tuple(above)] != "Pipe") & (outcome_dict[tuple(above)] not in checked_list):
                    outcome = check_for_pipes(above[0], above[1],"up")
                if (outcome_dict[tuple(below)] != "Pipe") & (outcome_dict[tuple(below)] not in checked_list):
                    outcome = check_for_pipes(below[0], below[1], "down")
                if (outcome_dict[tuple(right)] != "Pipe") & (outcome_dict[tuple(right)] not in checked_list):
                    outcome = check_for_pipes(right[0], right[1], "right")
                checked_list = checked_list + [tuple(above), tuple(right), tuple(below)]
        if direction == "left":
            above[0] -= 1
            below[0] += 1
            left[1] -= 1

            if (outcome_dict[tuple(above)] == "Outside") | (outcome_dict[tuple(below)] == "Outside") | (outcome_dict[tuple(left)] == "Outside"):
                end = True
                outcome = "Outside"
            elif (outcome_dict[tuple(above)] in checked_list) & (outcome_dict[tuple(below)] in checked_list) & (outcome_dict[tuple(left)] in checked_list):
                end = True
            else:
                if (outcome_dict[tuple(above)] != "Pipe") & (outcome_dict[tuple(above)] not in checked_list):
                    outcome = check_for_pipes(above[0],above[1],"up")
                if (outcome_dict[tuple(below)] != "Pipe") & (outcome_dict[tuple(below)] not in checked_list):
                    outcome = check_for_pipes(below[0],below[1],"down")
                if (outcome_dict[tuple(left)] != "Pipe") & (outcome_dict[tuple(left)] not in checked_list):
                    outcome = check_for_pipes(left[0],left[1],"left")
                checked_list = checked_list + [tuple(above), tuple(below), tuple(left)]

    return outcome



# %%
"""for row, dict in enumerate(data_dict.values()):
    for col, list in enumerate(dict):
        if outcome_dict[(row, col)] == "Inside":
            above = [row-1, col]
            below = [row+1, col]
            right = [row, col+1]
            left = [row, col-1]

            if (outcome_dict[tuple(above)] == "Pipe") & (outcome_dict[tuple(left)] == "Pipe") & (outcome_dict[tuple(below)] == "Pipe") & (outcome_dict[tuple(right)] == "Pipe"):
                outcome = "Inside"
            else:
                up_outcome = check_for_pipes(row, col, "up")
                down_outcome = check_for_pipes(row, col, "down")
                right_outcome = check_for_pipes(row, col, "right")
                left_outcome = check_for_pipes(row, col, "left")

                if (up_outcome == "Outside") | (down_outcome == "Outside") | (right_outcome == "Outside") | (left_outcome == "Outside"):
                    outcome = "Outside"
                else:
                    outcome = "Inside"

            print(f"Space at row {row}, column {col} is defined as {outcome}")
            outcome_dict[(row, col)] = outcome"""


