from typing import List

# Check if there exists atleast one '1' in each row
sample_table = [ 
    [1,0,0,0],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,0,1],
]
result = []
for row in range(len(sample_table)):
    s =  False
    for col_val in sample_table[row] :
        # print("Row = ", row , "Col = ", col_val)
        if col_val == 1:
            result.append(1)
            s = True
            break
    if s == False:
        result.append(0)
print("Result = ", result)

# Compare Tables
table_1 = {
    "0":[1,0,0,0],
    "1":[1,1,0,0],
    "2":[1,1,1,0],
    "3":[1,0,1,0]
}

table_2 = {
    "0":[0,0,0,0],
    "1":[1,1,0,0],
    "2":[1,1,0,0],
    "3":[1,0,1,0]
}

intersection = []
for k,v in table_1.items():
    if table_1[k] == table_2[k]:
            intersection.append(True)
    else:
            intersection.append(False)

print("Intersection of Tables = ", intersection)