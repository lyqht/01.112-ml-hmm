def viterbi(n,unique_word_list):
    #This is for the starting for viterbi
    store=[]   #store = the storage for scores for all the nodes. 
    scorelist=[]
    for i in range(unique_word_list):
        score_at_start = (emission(unique_word_list[i]))*(transmission("start",unique_word_list[i]))
        store.append(score_at_start)    #not too sure about the data structure/architechture. Dictionary or array or list?

    scorelist.append(store)
    store=[]
    #This is for the middle portion for viterbi
    for j in range(n): #for the whole length in sentence
        for k in range(unique_word_list): #for each unique word
            #im assuming that the scores are added in columns and the rows represent the iteration no.
            
            # row(0) [word1 = 0.3, word2 = 0.2, word3 = 0.3, word4 = 0.2]   #based on the start above
            # row(1) [word1 = 0.3, word2 = 0.2, word3 = 0.3, word4 = 0.2]   #next on list to calculate
            # row(2) [word1 = 0.3, word2 = 0.2, word3 = 0.3, word4 = 0.2]
            # row(3) [word1 = 0.3, word2 = 0.2, word3 = 0.3, word4 = 0.2]
            # row(4) [word1 = 0.3, word2 = 0.2, word3 = 0.3, word4 = 0.2]
            # the rows are added per iteration j
            # the word score is added per iteration k
            
            # At k=0, calculate 2nd node onwards
            for l in range(scorelist):
                score_per_node = (scorelist[l])*(emission(unique_word_list[k]))*(transmission(unique_word_list[l],unique_word_list)[k])
                store.append(score_per_node)
                #this calculates the 
                
            scorelist.append(max(store))
            store=[]
    return scorelist

    
def emission(word):
    # Will use this to search the emission score for the given word
    emission_dict={"start":1,"something":0.34}   # takes out from dictionary
    score = emission_dict[word]
    return score

def transmission(x1,x2):
    #will use this to search the transmission from x1 to x2
    transmission_dict = {"x1x2":0.032, "x2x1":0.064}
    score = transmission_dict[x1+x2]
    return score
