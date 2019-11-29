############### NEW   ############
def emission(node,word,x_dict):
    global emission_dict
    pair = word,node
    detector = 0 # this is used to find if word exist in the dictionary
    if pair not in emission_dict.keys(): #if the combination cannot be found in the dictionary
                                         #Either the word exists, or word is new. 
        if word in x_dict:
            score=0   #this means that this node is not the correct node.
        else:
            replaced_text = ("#UNK#", node)
            if replaced_text in emission_dict.keys():
                score = emission_dict[replaced_text] #if label have #unk#
            else:
                score = 0   #if label does not have #unk#, then set to 0.
    else:
        score = emission_dict[pair]
    return score

############### OLD ############
def emission(node,word,x_dict):
    global emission_dict
    global nodes
    pair = word,node
    detector = 0 # this is used to find if word exist in the dictionary
    if pair not in emission_dict.keys(): #if the combination cannot be found in the dictionary
                                         #Either the word exists, or word is new. 
        for o in nodes:
            missing_pair = word,o
            if missing_pair in emission_dict.keys(): #
                detector = 1 # to detect if word exist in dictionary.
        if detector == 1:
            score=0   #this means that this node is not the correct node.
        else:
            replaced_text = ("#UNK# ",node)
            if replaced_text in emission_dict.keys():
                score = emission_dict[replaced_text] #if label have #unk#
            else:
                score = 0   #if label does not have #unk#, then set to 0.
    else:
        score = emission_dict[pair]
    return score
