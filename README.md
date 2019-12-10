This repository contains the code for a Machine Learning project. 
The compiled code for our project lies in `compiled.ipynb`
Refer to the [Project Description](Project.pdf) for more details on the project.

There are some useful examples in this repository for Viterbi implementations.
- **Example 1**: Given sentence "the dog the", and its corresponding transition and emission probabilities
  - [List version](vb_example1_list.py)
  - [Numpy version](vb_example1_np.py)
- **Example 2**: from Borodovsky & Ekisheva (2006), pg. 80-81.
  - [List version](vb_example2_list.py)
  - [Numpy version](vb_example2_np.py)
- [Basic demo of numpy array initialization and functions](numpy_demo.py)


**Part 4**

We implemented a modified version of Viterbi Algorithm to find the k best paths, known as k best parallel Viterbi as shown in the report document
 
 
The best path found using this algorithm obtains the same result at the standard Viterbi, and the other 6 best paths found scored slightly lower in terms of recall score and precision, but still relatively reasonable.

**Part 5**

For the initial implementation of Hidden Markov Model (HMM) in this project from part 2 to 4, we have been using first order HMM, where emission parameters b_u (x_j) is dependent on the current tag to match the word, and the transition parameter a_(i,j) is dependent on the transition from previous 〖tag〗_i to current 〖tag〗_j. This might not give a good estimation for predicting the overall tags of a sentence.  Thus, to improve the performance in our code, we will be implementing a second order HMM. The difference between the first order and second order HMM lies in its transition parameters. The second order HMMs’ transition parameter a_(i,j,k)  considers the transition from two previous tags i and j to current tag k.  This should give us more thorough predicted labels. 
However, second order HMM requires a greater amount of training dataset in order to produce good result as it requires three tags to be used for estimating transition parameters, which in some cases do not appear in the training set. To solve this problem, instead of calculating the transition parameter as P(i|j,k) = P(i|j,k), we need to consider the transition parameter from previous tag j to current tag i and  transition parameter at current tag i. Hence, P(i|j,k) = λ_1 P(i|j,k) +λ_2 P(i|j) + λ_3 P(i) 
k_3=  ( log⁡(Count(i,j,k)+1)+1)/(log⁡(Count(i,j,k)+1)+2)
k_2=  ( log⁡(Count(j,k)+1)+1)/(log⁡(Count(j,k)+1)+2)
λ_1= k_3
λ_2=(1-k_3 ).k_2
λ_3=(1-k_3 ).〖(1-k〗_2)
The sum of λ_1+ λ_2+ λ_3=1


Result
EN
	
#Entity in gold data	13179
#Entity in prediction	14617
	
#Correct Entity	10951
Entity  precision	0.7492
Entity  recall	0.8309
Entity  F	0.7880
	
#Correct Sentiment	10337
Sentiment  precision	0.7072
Sentiment  recall	0.7844
Sentiment  F	0.7438


AL
	
#Entity in gold data	8408
#Entity in prediction	8635
	
#Correct Entity	3278
Entity  precision	0.3796
Entity  recall	0.3899
Entity  F	0.3847
	
#Correct Sentiment	2393
Sentiment  precision	0.2771
Sentiment  recall	0.2846
Sentiment  F	0.2808
