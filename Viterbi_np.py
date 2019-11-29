import numpy as np 
def viterbi(unique_word_list):
    #This is for the starting for viterbi
    num_nodes_per_col = len(nodes())
    store=np.zeros(num_nodes_per_col)   #store = the storage for scores for all the nodes. 
    scorelist=np.zeros((num_nodes_per_col, len(unique_word_list) + 1))
    path=[]
    
    for i in range(num_nodes_per_col):
        score_at_start = emission(nodes()[i],unique_word_list[0])*(transmission("start",nodes()[i]))
        store[i] = score_at_start   #not too sure about the data structure/architechture. Dictionary or array or list?

    scorelist[:,0] = store
    store = np.zeros(num_nodes_per_col)
    score_per_node=np.zeros(num_nodes_per_col)
    
    #This is for the middle portion for viterbi
    if len(unique_word_list)>1:
        for j in range(len(unique_word_list)-1): #for the whole length in sentence
            for k in range(num_nodes_per_col): #for each node
                #score per node = prevnode*emission*transition
                for l in range(num_nodes_per_col): #for 1 node, transition from prev node to current node
                    prev_node = scorelist[l][j]
                    curr_emission = emission(nodes()[k],unique_word_list[j+1])
                    curr_transition = transmission(nodes()[l],nodes()[k])
                    score_per_node[l] = prev_node*curr_emission*curr_transition
                
                store[k] = np.max(score_per_node) # max path

                path.append(nodes()[np.argmax(score_per_node)]) # able to give you best paths, up to before stop.
                score_per_node=np.zeros(num_nodes_per_col)
            
            scorelist[:,j+1] = store
            store = np.zeros(num_nodes_per_col)
                      
        score_at_stop=np.zeros(num_nodes_per_col)
        
        #This is for the STOP for viterbi
        for m in range(len(nodes())):
            score_at_stop[m] = transmission(nodes()[m],"stop")*scorelist[m][len(unique_word_list)-1] #
        scorelist[:, -1] = np.full(num_nodes_per_col,np.max(score_at_stop))
        path.append(nodes()[np.argmax(score_at_stop)])
        print(path)
    return scorelist

    
def emission(word,set=""):
    # Will use this to search the emission score for the given word
    #emission_dict={"Athe":0.9,"Bthe":0.1,"Adog":0.1,"Bdog":0.9,"Astop":0}   # takes out from dictionary
    emission_dict={"Athe":0.9,"Bthe":0.1,"Adog":0.1,"Bdog":0.9,"Astop":0}
    score = emission_dict[word+set]
    return score

def transmission(x1,x2):
    #will use this to search the transmission from x1 to x2
    transmission_dict = {"startA":1,"startB":0,"startstop":0,"AA":0.5,"AB":0.5,"Astop":0,"BA":0,"BB":0.8,"Bstop":0.2}
    score = transmission_dict[x1+x2]
    return score

def nodes():
    return ["A","B"]
    #return ["x","y","Z"]

unl=["the","dog","the"]
print(viterbi(unl))