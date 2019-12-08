import numpy as np 
import heapq

def kViterbiParallel(pi, a, b, obs, topK):
  
    nStates = np.shape(b)[0]
    T = np.shape(obs)[0]

    assert (topK <= np.power(nStates, T)), "k < nStates ^ topK"

    # delta --> highest probability of any path that reaches point i
    delta = np.zeros((T, nStates, topK))

    # phi --> argmax
    phi = np.zeros((T, nStates, topK), int)

    #The ranking of multiple paths through a state
    rank = np.zeros((T, nStates, topK), int)

    for i in range(nStates):
        delta[0, i, 0] = pi[i] * b[i, obs[0]]
        phi[0, i, 0] = i

        #Set the other options to 0 initially
        for k in range(1, topK):
            delta[0, i, k] = 0.0
            phi[0, i, k] = i

    #Go forward calculating top k scoring paths
    # for each state s1 from previous state s2 at time step t
    for t in range(1, T):
        for s1 in range(nStates):

            h = []

            for s2 in range(nStates):
                # y = np.sort(delta[t-1, s2, :] * a[s2, s1] * b[s1, obs[t]])

                for k in range(topK):
                    prob = delta[t - 1, s2, k] * a[s2, s1] * b[s1, obs[t]]
                    # y_arg = phi[t-1, s2, k]

                    state = s2

                    # Push the probability and state that led to it
                    heapq.heappush(h, (prob, state))

            #Get the sorted list
            h_sorted = [heapq.heappop(h) for i in range(len(h))]
            h_sorted.reverse()

            #We need to keep a ranking if a path crosses a state more than once
            rankDict = dict()

            #Retain the top k scoring paths and their phi and rankings
            for k in range(0, topK):
                delta[t, s1, k] = h_sorted[k][0]
                phi[t, s1, k] = h_sorted[k][1]

                state = h_sorted[k][1]

                if state in rankDict:
                    rankDict[state] = rankDict[state] + 1
                else:
                    rankDict[state] = 0

                rank[t, s1, k] = rankDict[state]

    # Put all the last items on the stack
    h = []

    #Get all the topK from all the states
    for s1 in range(nStates):
        for k in range(topK):
            prob = delta[T - 1, s1, k]

            #Sort by the probability, but retain what state it came from and the k
            heapq.heappush(h, (prob, s1, k))

    #Then get sorted by the probability including its state and topK
    h_sorted = [heapq.heappop(h) for i in range(len(h))]
    h_sorted.reverse()

    # init blank path
    path = np.zeros((topK, T), int)
    path_probs = np.zeros((topK, T), float)

    #Now backtrace for k and each time step
    for k in range(topK):
        #The maximum probability and the state it came from
        max_prob = h_sorted[k][0]
        state = h_sorted[k][1]
        rankK = h_sorted[k][2]

        #Assign to output arrays
        path_probs[k][-1] = max_prob
        path[k][-1] = state

        #Then from t down to 0 store the correct sequence for t+1
        for t in range(T - 2, -1, -1):
            #The next state and its rank
            nextState = path[k][t+1]

            #Get the new state
            p = phi[t+1][nextState][rankK]

            #Pop into output array
            path[k][t] = p

            #Get the correct ranking for the next phi
            rankK = rank[t + 1][nextState][rankK]

    return path, path_probs, delta, phi
  
  

obs_map = {"normal" : 0, "cold" : 1, "dizzy" : 2}
obs = [obs_map["normal"], obs_map["cold"], obs_map["dizzy"]]
state_map = {"healthy" : 0, "fever" : 1}

pi = np.array([0.6, 0.4])

a = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

b = np.array([
    [0.5, 0.4, 0.1],
    [0.1, 0.3, 0.6]
])

# obs = [obs_map["normal"], obs_map["cold"]]

path, delta, phi, max_prob = kViterbiParallel(pi, a, b, obs, 8)
print("Path")
print(path)
print("Delta")
print(delta)
print("Phi")
print(phi)
print("Max Prob")
print(max_prob)
