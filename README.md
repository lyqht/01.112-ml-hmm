# 01.112 ML Design Project

This repository contains the code for a school Design Project done for 01.112 Machine Learning course in SUTD, Fall 2019. 

Refer to the [Project Description](Project.pdf) for more details on the project.
Refer to the [Report](./final/Report.docx) for more details on our implementation of Part 4 and 5.
The compiled code for our project lies in `final/Part2to4.ipynb` and `final/Part5.ipynb`


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