# 01.112 ML Design Project

This repository contains the code for a school Design Project done for 01.112 Machine Learning course in SUTD, Fall 2019. 

The compiled code for our project lies in `compiled.ipynb`
Refer to the [Project Description](Project.pdf) for more details on the project.

### Examples 
There are some useful examples in this repository for testing small Viterbi implementations. The numpy version is significantly faster when we applied it to the actual datasets.
- **Example 1**: Given sentence "the dog the", and its corresponding transition and emission probabilities
  - [List version](vb_example1_list.py)
  - [Numpy version](vb_example1_np.py)
- **Example 2**: from Borodovsky & Ekisheva (2006), pg. 80-81.
  - [List version](vb_example2_list.py)
  - [Numpy version](vb_example2_np.py)
- [Basic demo of numpy array initialization and functions](numpy_demo.py)

Unfortunately, for k-best paths, we did not have any examples. 

## Part 4 - K Best Path Viterbi

We implemented a modified version of Viterbi Algorithm to find the k best paths, known as k best parallel Viterbi as shown in the report document.
 
The best path found using this algorithm obtains the same result at the standard Viterbi, and the other 6 best paths found scored slightly lower in terms of recall score and precision, but still relatively reasonable.

## Part 5 - 2nd Order HMM

For the initial implementation of Hidden Markov Model (HMM) in this project from part 2 to 4, we have been using first order HMM, where emission parameters $b_u (x_j)$ is dependent on the current tag to match the word, and the transition parameter $a_(i,j)$ is dependent on the transition from previous $\text{tag}_i$ to current $\text{tag}_j$. This might not give a good estimation for predicting the overall tags of a sentence.  Thus, to improve the performance in our code, we will be implementing a second order HMM. 

The difference between the first order and second order HMM lies in its transition parameters. The second order HMMs’ transition parameter $a_(i,j,k)$  considers the transition from two previous $\text{tag}_i$ and $\text{tag}_j$ to current $\text{tag}_k$.  This should give us more thorough predicted labels. 

However, second order HMM requires a greater amount of training dataset in order to produce good result as it requires three tags to be used for estimating transition parameters, which in some cases do not appear in the training set. To solve this problem, instead of calculating the transition parameter as $P(i|j,k) = P(i|j,k)$, we need to consider the transition parameter from previous $\text{tag}_j$ to current $\text{tag}_i$ and  transition parameter at current $\text{tag}_i$. Hence, 
$$
\begin{aligned}
&P(i|j,k) = λ_1 P(i|j,k) +λ_2 P(i|j) + λ_3 P(i) \\
&k_3=  ( \log⁡(\text{Count}(i,j,k)+1)+1)/(\log⁡(\text{Count}(i,j,k)+1)+2)\\
&k_2=  ( \log⁡(\text{Count}(j,k)+1)+1)/(\log⁡(\text{Count}(j,k)+1)+2)\\
&λ_1= k_3\\
&λ_2=(1-k_3 )\cdot k_2\\
&λ_3=(1-k_3 )\cdot (1-k_2)\\
&λ_1+ λ_2+ λ_3=1
\end{aligned}
$$