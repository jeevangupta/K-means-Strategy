# K-means-Strategy

   **In this project, you are required to implement the K-means algorithm and apply your implementation on the given dataset (AllSamples.npy), which contains a set of 2-D points. You are required to implement two different strategies for choosing the initial cluster centers.**

## K-mean-Strategy - 1 

   **K-means_algortihm_Strategy Part 1 (K-mean) Overview:**

   You are required to implement the following strategy for choosing the initial cluster centers. Part 1 is to randomly pick the initial centers from the given samples.

   You need to test your implementation on the given data, with the number k of clusters ranging from 2-10, output the final coordinate of the centroids and compute the loss based on the objective function.


## K-mean-Strategy - 2 

   **K-means_algortihm_Strategy2 (K-mean ++) Overview:**

   You are required to implement the following strategy for choosing the initial cluster centers.
    
   Part 2 is to pick the first center randomly; for the i-th center (i >1), choose a sample (among all possible samples) such that the average distance of this chosen one to all previous (i -1) centers is maximal.
    
   You need to test your implementation on the given data, with the number k of clusters ranging from 2-10, output the final coordinate of the centroids and compute the loss based on the objective function.


## Required Tasks:
1. Write code to implement the k-means algorithm with Strategy 1.
2. Use your code to do clustering on the given data; compute the objective function as a function of k (k = 2, 3, ..., 10).
3. Repeat the above step with another initialization.
4. Write code to implement the k-means algorithm with Strategy 2.
5. Use your code to do clustering on the given data; compute the objective function as a function of k (k = 2, 3, ..., 10).
6. Repeat the above step with another initialization.
