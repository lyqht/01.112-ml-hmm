import numpy as np

num_rows = 5
num_columns = 4

mini_graph = np.zeros((num_rows,num_columns)) # num_rows , num_columns 
score_list = np.zeros((1,num_columns)) # store max of each column
store = np.zeros(num_rows) # store all the scores for one node
 
# fake data
for i in range(num_rows):
  for k in range(num_columns):
    mini_graph[i][k] = np.random.random_sample() # random float from 0 to 1
print("Mini graph example")
print(mini_graph)

# example of getting the max for each col at this point
# without any calculation

max_for_each_col = np.amax(mini_graph, axis=0) # axis = 0 is column, axis = 1 is row
print("Max for each column")
print(max_for_each_col)