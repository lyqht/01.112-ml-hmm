def viterbi(unique_word_list):
    #This is for the starting for viterbi
    store=[]   #store = the storage for scores for all the nodes. 
    scorelist=[]
    path=[]
    #nodes=["A","B"]
    for i in range(len(nodes())):
        score_at_start = (emission(nodes()[i],unique_word_list[0]))*(transmission("start",nodes()[i]))
        store.append(score_at_start)    #not too sure about the data structure/architechture. Dictionary or array or list?

    scorelist.append(store)
    store=[]
    score_per_node=[]
    #This is for the middle portion for viterbi
    if len(unique_word_list)>1:

        for j in range(len(unique_word_list)-1): #for the whole length in sentence
            for k in range(len(nodes())): #for each node
                #score per node = prevnode*emission*transition
                for l in range(len(nodes())): #for 1 node, transition from prev node to current node

                    score_per_node.append((scorelist[j][l])*(emission(nodes()[k],unique_word_list[j+1]))*(transmission(nodes()[l],nodes()[k])))
                    #print
                store.append(max(score_per_node)) #found max path

                path.append(nodes()[score_per_node.index(max(score_per_node))]) # able to give you best paths, up to before stop.
                score_per_node=[]
            
            #print(store)
            scorelist.append(store)
            store=[]

                      
        score_at_stop=[]
        #This is for the stop for viterbi
        for m in range(len(nodes())):

            #print(j)
            #print(l)
            score_at_stop.append((transmission(nodes()[m],"stop"))*scorelist[len(unique_word_list)-1][m]) #
        scorelist.append(max(score_at_stop))
        path.append(nodes()[score_at_stop.index(max(score_at_stop))])
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
#viterbi(unl)