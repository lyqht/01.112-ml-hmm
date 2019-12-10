import numpy as np
import heapq 

"""
Retrieved from https://github.com/carthach/kBestViterbi
"""

def kViterbiParallel(nodes, obs, num_k):
    global transition
    global emission
    
    """
    scores = highest probability of any path that reaches point i
    phi(i, k) = kth lowest cost to reach node i at col t from node 1 at col 0.
    rank = The ranking of multiple paths through a state
    """
    num_nodes = len(nodes)
    num_words = len(obs)

    scores = np.zeros(num_words, num_nodes, num_k)
    phi = np.zeros((num_words, num_nodes, num_k),int)
    rank = np.zeros((num_words, num_nodes, num_k),int)

    # for k in range(K):
    for i in range(num_nodes):
        curr_emission = emission(obs[0], nodes[i])
        curr_transition = transition("START", nodes[i])
        scores[0, i, 0] = np.log(curr_emission) + np.log(curr_transition)
        phi[0, i, 0] = i

        # Set the other options  to 0 initially
        for k in range(1, num_k):
            scores[0, i, k] = 0.0
            phi[0, i, k] = i

    # Go forward calculating top k scoring paths
    # for each state s1 from previous state s2 at time step t
    for t in range(1, num_words):
        for s1 in range(num_nodes):
          
            h = []  # heap structure for priority queue 
          
            for s2 in range(num_nodes):
                for k in range(num_k):
                    curr_emission = emission(obs[t], nodes[s1])
                    curr_transition = transition(nodes[s1], nodes[s2])
                    prob = scores[t - 1, s2, k] * np.log(curr_transition) + np.log(curr_emission)

                    state = s2

                    # Push the probability and state that led to it
                    heapq.heappush(h, (prob, s2))

            #Get the sorted list
            h_sorted = [heapq.heappop(h) for i in range(len(h))]
            h_sorted.reverse()

            #We need to keep a ranking if a path crosses a state more than once
            rankDict = dict()

            #Retain the top k scoring paths and their phi and rankings
            for k in range(0, num_k):
                scores[t, s1, k] = h_sorted[k][0]
                phi[t, s1, k] = h_sorted[k][1]

                state = h_sorted[k][1]

                if state in rankDict:
                    rankDict[state] = rankDict[state] + 1
                else:
                    rankDict[state] = 0

                rank[t, s1, k] = rankDict[state]

    # Put all the last items on the stack
    h = []

    # Get all the num_k from all the states
    for s1 in range(num_nodes):
        for k in range(num_k):
            prob = scores[num_words - 1, s1, k]

            #Sort by the probability, but retain what state it came from and the k
            heapq.heappush(h, (prob, s1, k))

    # Then get sorted by the probability including its state and num_k
    h_sorted = [heapq.heappop(h) for i in range(len(h))]
    h_sorted.reverse()

    # init blank path
    path = np.zeros((num_k, num_words), int)
    path_probs = np.zeros(num_k, num_words)

    # Backpropagation
    for k in range(num_k):
        #The maximum probability and the state it came from
        max_prob = h_sorted[k][0]
        state = h_sorted[k][1]
        rankK = h_sorted[k][2]

        # Assign to output arrays
        path_probs[k][-1] = max_prob
        path[k][-1] = state

        #Then from t down to 0 store the correct sequence for t+1
        for t in range(num_words - 2, -1, -1):
            #The next state and its rank
            nextState = path[k][t+1]

            #Get the new state
            p = phi[t+1][nextState][rankK]

            #Pop into output array
            path[k][t] = p

            #Get the correct ranking for the next phi
            rankK = rank[t + 1][nextState][rankK]

    return path, path_probs, scores, phi