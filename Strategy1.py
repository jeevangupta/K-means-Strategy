#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Precode import *
import numpy
import math

data = np.load('AllSamples.npy')


# In[2]:


k1,i_point1,k2,i_point2 = initial_S1('xxxx') # please replace xxxx with your last four digit of your ID


# In[3]:


print(k1)
print(i_point1)
print(k2)
print(i_point2)
#print(data)


# In[5]:


def euclidian_distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2) )


# In[6]:


def find_mean(dt):
    sum_x = 0;
    sum_y = 0;
    for x,y in dt:
        sum_x += x;
        sum_y += y;
    mean_x = sum_x*(1.0)/len(dt);
    mean_y = sum_y*(1.0)/len(dt);
    return [mean_x,mean_y];


# In[7]:



def get_centroids_and_clusters(initial_centroid, data_point):
    
    clusters = {}
    for x in initial_centroid:
        clusters[tuple(x)] = [];
        
    centroid = []
    for i in data_point:
        distances = []
        for j in initial_centroid:
            dist = euclidian_distance(j,i)
            
            distances.append((dist,j))
        distances.sort(key=lambda j:j[0]);
        #print(distances[0][1])
        best_centroid = list(distances[0][1])
        clusters[tuple(best_centroid)].append(i)
        
        
    #print("\n clusters : ",clusters)
    
    new_centroids = []
    for i,j in clusters.items():
        if len(j) == 0:
            c = i
        else:
            c = find_mean(j)
        
        new_centroids.append(list(c))
        
    new_centroids.sort()
    return clusters, new_centroids
    
            


# In[9]:


def k_mean(initial_centroids, data_point):
    centroids = initial_centroids.tolist()
    while True:
        clusters, new_centroids = get_centroids_and_clusters(centroids, data_point)
    
        if new_centroids == list(centroids):
            break
        centroids = new_centroids
        
    return centroids, clusters


centroids1, clusters1 = k_mean(i_point1,data)
#print("\n clusters1: ",clusters1)
print("\n centroids1: ",centroids1)

centroids2, clusters2 = k_mean(i_point2,data)
#print("\n clusters2: ",clusters2)
print("\n centroids2: ",centroids2)


# In[10]:


def get_loss_using_objective_function(clusters):
    loss = 0
    for centroid, cluster in clusters.items():
        l = 0
        for c in cluster:
            dist = euclidian_distance(c,list(centroid))
            dist_square = dist*dist
            l += dist_square
            
        loss += l
        
    return loss

loss1 = get_loss_using_objective_function(clusters1)
print("\n loss1 : ",loss1)

loss2 = get_loss_using_objective_function(clusters2)
print("\n loss2 : ",loss2)



#k1 = 3
#i_point1 = [[5.07250754 7.89834048],[7.72715541 7.62018213],[5.02471033 8.23879873]]
#centeriod1 = [[3.2489, 2.5803], [4.8337, 7.3161], [7.2397, 2.4821]] 
#cost1 = 1338.1059

#k2 = 5
#i_point2 = [[3.02640736 5.74083968],[7.94375954 8.21165063],[3.89523379 0.70718356],[3.0226944  0.86402039],[6.8113456  0.99804859]]
#centeriod2 = [[2.6819, 2.0946], [3.0293, 7.0633], [5.2232, 4.2250], [6.9741, 8.1199], [7.5562, 2.2352]]
#cost2 = 597.3211

