#=== TOY EXAMPLE ===#
"""
ASSUME NUM_K < NUM_NODES
"""
num_rows = 7 # num_nodes
num_cols = 4 # num_words
num_k = 7 # k_best_paths

score = np.zeros((num_rows, num_cols, num_rows))
ranking = np.zeros((num_rows, num_cols, num_k))

# nodes in first column all come from start
# ranking[:,0,:] = np.Infinity 
ranking.fill(np.Infinity)

# randomly initialize emission_probs, this are calculated during start phase
score[:,0,:] = np.random.rand(num_rows,1) 

# start from 1 since start emission prob already calculated
for i in range(1,num_cols):
    for j in range(num_rows):
        print(f"For node in row {j}, col {i}")
        
        fake_transition = np.random.random() # can be deleted ltr
        fake_emission = np.random.random() # can be deleted ltr
        curr_node_scorelist=np.zeros(num_rows)
        
        if ranking[j][i-1][-1] == np.Infinity:
            for l in range(num_rows):
                curr_node_scorelist[l] = score[l][i-1][0] + fake_transition + fake_emission
        else:
            for l in range(num_k):
                curr_node_scorelist[l] = score[j][i-1][l] + fake_transition + fake_emission
                
        print("Curr node scorelist", curr_node_scorelist)
        max_indexes= np.zeros(num_k)
        max_indexes = (-curr_node_scorelist).argsort()[:num_k]
        
        ranking[j][i] = max_indexes
        score[j][i] = curr_node_scorelist
print("Ranking")
print(ranking)
print("Scores")
print(score)