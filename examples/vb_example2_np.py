import numpy as np

def viterbi(unique_word_list):
    #This is for the starting for viterbi
    global nodes
    num_nodes_per_col = len(nodes)
    store=np.zeros(num_nodes_per_col)   #store = the storage for scores for all the nodes. 
    scorelist=np.zeros((num_nodes_per_col, len(unique_word_list) + 1))
    
    for i in range(num_nodes_per_col):
        emission_score = emission(nodes[i],unique_word_list[0])
        transition_score = transition("START",nodes[i])
        store[i] = np.log(emission_score)+np.log(transition_score)  
    scorelist[:,0] = store
    store = np.zeros(num_nodes_per_col)
    score_per_node=np.zeros(num_nodes_per_col)
    
    #This is for the middle portion for viterbi
    #score per node = prevnode*emission*transition

    if len(unique_word_list)>1:
        for j in range(len(unique_word_list)-1): #for the whole length in sentence
            for k in range(num_nodes_per_col): #for each node
                for l in range(num_nodes_per_col): #for 1 node, transition from prev node to current node
                    prev_node = scorelist[l][j]
                    curr_emission = emission(nodes[k],unique_word_list[j+1])
                    curr_transition = transition(nodes[l],nodes[k])
                    score_per_node[l] = prev_node+np.log(curr_emission)+np.log(curr_transition) 
                
                store[k] = np.max(score_per_node) # max path
                score_per_node=np.zeros(num_nodes_per_col)
            
            scorelist[:,j+1] = store
            store = np.zeros(num_nodes_per_col)
                      
        score_at_stop=np.zeros(num_nodes_per_col)
        
        #This is for the STOP for viterbi
        for m in range(num_nodes_per_col):
            score_at_stop[m] = np.log(transition(nodes[m],"END")) + scorelist[m][len(unique_word_list)-1]
        scorelist[:,-1] = np.full(num_nodes_per_col,np.max(score_at_stop))
        
    return scorelist
  
def viterbi_backtrack(scorelist):
    """
    back tracking for viterbi
    node value*transition = array, then find max, then find position. use position for next step.
    np.argmax returns index of max in the element.
    The final score on the score list is for end
    """ 
    global nodes
    
    scorelist = np.flip(scorelist,axis=1) #reverse the score list so easier to calculate.
    
    print("After flipping")
    max_node_index = 0 
    num_obs = scorelist.shape[1]
    num_nodes = scorelist.shape[0]
    node_holder = np.zeros(num_nodes)
    path = []
    print("num obs", num_obs)
    print("num nodes", num_nodes)

    if (num_obs == 1):
        for k in range (num_nodes):
            calculate_max_node = scorelist[0][k] + np.log(transition(nodes[k],"END"))
            node_holder[i] = calculate_max_node
        path.append(nodes[np.argmax(node_holder)])
        return(path[::-1])

    for i in range (1,num_obs): # for length of sentence
        for j in range(num_nodes): #for each node
            if (i==1):
                calculate_max_node = scorelist[j][i] + np.log(transition(nodes[j],"END"))
                node_holder[j] = calculate_max_node
            else:
                calculate_max_node = scorelist[j][i] + np.log(transition(nodes[j],nodes[max_node_index]))
                node_holder[j] = calculate_max_node
        
        max_node_index=np.argmax(node_holder)
        path.append(nodes[np.argmax(node_holder)])
        node_holder=np.zeros(num_nodes)

    return(path[::-1])

def emission(node,word):
    global emission_dict
    global nodes
    pair = node+word
    detector = 0 # this is used to find if word exist in the dictionary
    if pair not in emission_dict.keys(): #if the combination cannot be found in the dictionary
                                         #Either the word exists, or word is new. 
        for o in nodes:
            missing_pair = node+word
            if missing_pair in emission_dict.keys(): #
              score=0   #this means that this node is not the correct node.
        else:
            replaced_text = "#UNK#",node
            if replaced_text in emission_dict.keys():
                score = emission_dict[replaced_text] #if label have #unk#
                
            else:
                score = 0   #if label does not have #unk#, then set to 0.
    else:
        score = emission_dict[pair]
    return score

def transition(x1,x2):
    global transition_dic
    #will use this to search the transition from x1 to x2
    pair = x1,x2
    if pair not in transition_dic.keys():
        score = 0
    else:
        score = transition_dic[x1,x2]
    return score
  
"""
Example from Borodovsky & Ekisheva (2006), pg. 80-81
"""
transition_dic = {("START","H"):0.5,("START","L"):0.5,
                    ("H","H"):0.5,("H","L"):0.5,("L","H"):0.4,("L","L"):0.6,
                    ("H","END"):0.1,("L","END"):1}

emission_dict={"HA":0.2,"HC":0.3,"HG":0.3,"HT":0.2,
                "LA":0.3,"LC":0.2,"LG":0.2,"LT":0.3}

nodes = ["H","L"]


unl=["G","G","C","A","C","T","G","A","A"]
log_scores = viterbi(unl)

print(viterbi_backtrack(log_scores))   #scores are in log to prevent underflow

for v in log_scores:
    print(np.exp(v))