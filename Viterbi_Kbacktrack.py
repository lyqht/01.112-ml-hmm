import numpy as np

def viterbi(unique_word_list):
    #This is for the starting for viterbi
    store=[]   #store = the storage for scores for all the nodes. 
    scorelist=[]
    all_scores=[]
    path=[] #in the book this is E
    pathpn=[]


    #This is for the start
    for i in range(len(nodes)):
        score_at_start = np.log(emission(nodes[i],unique_word_list[0]))+np.log(transition("START",nodes[i]))
        store.append(score_at_start)
    path.append(1)    

    scorelist.append(store)
    store=[]
    score_per_node=[]
    #This is for the middle portion for viterbi
    if len(unique_word_list)>1:

        for j in range(len(unique_word_list)-1): #for the whole length in sentence
            for k in range(len(nodes)): #for each node
                #score per node = prevnode*emission*transition
                for l in range(len(nodes)): # l = iterate thru previous node, k= iterate thru current node, j= iterate thru sentence
                    # This is to calculate the current node scores.
                    score_per_node.append((scorelist[j][l])+np.log(emission(nodes[k],unique_word_list[j+1]))+np.log(transition(nodes[l],nodes[k])))
                    

                store.append(max(score_per_node)) #found max path
                pathpn.append(np.argmax(score_per_node))
                all_scores.append(score_per_node)
                score_per_node=[]
            
            #print(store)
            path.append(pathpn)
            scorelist.append(store) # store the scores for nodes
            store=[]
            pathpn=[]

                      
        score_at_stop=[]
        #This is for the stop for viterbi
        for m in range(len(nodes)):
            score_at_stop.append(np.log(transition(nodes[m],"END"))+ (scorelist[len(unique_word_list)-1][m])) #at stop.
        path.append(np.argmax(score_at_stop))
        scorelist.append(max(score_at_stop))
     


    return scorelist,all_scores,path

def viterbi_backtrack(scorelist):
    ####### back tracking for viterbi
    # node value*transition = array, then find max, then find position. use position for next step.
    #np.argmax returns index of max in the element.
    # The final score on the score list is for end
    scorelist = scorelist[::-1] #reverse the score list so easier to calculate.
    node_holder=[]
    path = []
    max_node_index=0
    length_of_scorelist=len(scorelist)
    length_of_nodes=len(nodes)

    if (length_of_scorelist == 1):  
        for k in range (length_of_nodes):
            calculate_max_node = (scorelist[0][k]) + np.log(transition(nodes[k],"END"))
            node_holder.append(calculate_max_node)
        path.append(nodes[np.argmax(node_holder)])
        node_holder=[]
        return(path[::-1])

    for i in range (1,length_of_scorelist): # for length of sentence

        for j in range(length_of_nodes): #for each node
            #each node*own path, find max
            if (i==1):
                calculate_max_node = (scorelist[i][j]) + np.log(transition(nodes[j],"END"))
                node_holder.append(calculate_max_node)
                #print(np.exp(calculate_max_node))
            else:
                
                calculate_max_node = (scorelist[i][j]) + np.log(transition(nodes[j],nodes[max_node_index]))#
                node_holder.append(calculate_max_node)
        
        max_node_index=(np.argmax(node_holder))
        path.append(nodes[np.argmax(node_holder)])
        node_holder=[]
        

    return(path[::-1])


    
def emission(node,word=""):
    # Will use this to search the emission score for the given word
    #emission_dict={"Athe":0.9,"Bthe":0.1,"Adog":0.1,"Bdog":0.9,"Astop":0}   # takes out from dictionary

    score = emission_dict[node+word]
    return score

def transition(x1,x2):
    #will use this to search the transition from x1 to x2
    score = transition_dic[x1,x2]
    return score


def k_backtrack(path_list,nodes):
    path_back = path_list[::-1]  #make an inverted list thingy
    path=[path_back[0]]
    nodepath=[]
    #print(path[0])
    
    for p in range(len(path_back)-2):
        print(path_back[p+1][1])
        path.append(path_back[p+1][path[p]])

    for i in path[::-1]:
        nodepath.append(nodes[i])

    return nodepath

transition_dic = {("START","H"):0.5,("START","L"):0.5,
                    ("H","H"):0.5,("H","L"):0.5,("L","H"):0.4,("L","L"):0.6,
                    ("H","END"):0.1,("L","END"):1}

emission_dict={"HA":0.2,"HC":0.3,"HG":0.3,"HT":0.2,
                "LA":0.3,"LC":0.2,"LG":0.2,"LT":0.3}

nodes = ["H","L"]


unl=["G","G","C","A","C","T","G","A","A"]
log_scores = viterbi(unl)


#print(len(log_scores))
print(viterbi_backtrack(log_scores[0]))   #scores are in log to prevent underflow

# print(node_list[np.argmax(log_scores[2])])
for v in log_scores[0]:
    print(np.exp(v))

# print(log_scores[1])

print(log_scores[2])

print((k_backtrack(log_scores[2],nodes)))
# viterbi(unl)


# def nodes():
    
#     return node_list


# Running the code: required transition, emission dictionaries, nodes and word input.
# transition_dic = {("START","A"):1,("START","B"):0,("START","END"):0,("A","A"):0.5,("A","B"):0.5,("A","END"):0,("B","A"):0,("B","B"):0.8,("B","END"):0.2}
# emission_dict={"Athe":0.9,"Bthe":0.1,"Adog":0.1,"Bdog":0.9}
# node_list = ["A","B"]
# unl=["the","dog","the"]

# transition_dic = {("START","x"):0.4,("START","y"):0,("START","z"):0.6,("START","END"):0,
#                     ("x","x"):0,("x","y"):0.5,("x","z"):1/3,("x","END"):1/6,
#                     ("y","x"):1/6,("y","y"):0,("y","z"):1/6,("y","END"):2/3,
#                     ("z","x"):0.5,("z","y"):0.5,("z","z"):0,("z","END"):0}
                    
# emission_dict={"xa":1/6,"xb":0.5,"xc":1/3,
#                 "ya":1/3,"yb":0,"yc":2/3,
#                 "za":1/6,"zb":1/3,"zc":1/2}

# unl=["b","b"]

# nodes = ["x","y","z"]
