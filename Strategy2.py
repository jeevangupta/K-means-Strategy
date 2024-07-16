#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Precode2 import *
import numpy
import math

data = np.load('AllSamples.npy')


# In[2]:


k1,i_point1,k2,i_point2 = initial_S2('xxxx') # please replace xxxx with your last four digit of your ID


# In[3]:


print(k1)
print(i_point1)
print(k2)
print(i_point2)


# In[4]:


def euclidian_distance(p1,p2):
    return math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2) )


# In[6]:


def centroid_in_sample(array, point):
    for x,y in array:
        if(point[0] == x and point[1] == y):
            return True;
    return False;

def get_average_distances(centroid, sample):
    sum = 0
    for i in centroid:
        dist = euclidian_distance(i,sample)
        sum += dist
        
    average = sum*(1.0)/len(centroid)
    return average


def get_initial_centroids(k, centroid1, sample):
    initial_centroids = centroid1
    for i in range(k-1):
        average_distances = []
    
        for i,point in enumerate(sample):
            if(centroid_in_sample(centroid1, point)):
                continue
            avg_dists = get_average_distances(centroid1, point)
            average_distances.append((avg_dists,point))
                                     
        average_distances.sort(key=lambda point:point[0])
        
        centroid = average_distances[-1][1]
        initial_centroids.append(tuple(centroid)) 
    return initial_centroids


initial_centroids1 = get_initial_centroids(k1, [tuple(i_point1)], data)
print("\n initial_centroids1: ",initial_centroids1)

initial_centroids2 = get_initial_centroids(k2, [tuple(i_point2)], data)
print("\n initial_centroids2: ",initial_centroids2)


# In[7]:


def find_mean(dt):
    sum_x = 0;
    sum_y = 0;
    for x,y in dt:
        sum_x += x;
        sum_y += y;
    mean_x = sum_x*(1.0)/len(dt);
    mean_y = sum_y*(1.0)/len(dt);
    return [mean_x,mean_y];


# In[8]:


def get_centroids_and_clusters(initial_centroid, data_point):

    clusters = {}
    for x in initial_centroid:
        clusters[tuple(x)] = []  
    #print("\n",clusters)
    
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
    centroids = initial_centroids
    
    while True:
        clusters, new_centroids = get_centroids_and_clusters(centroids, data_point)
    
        if new_centroids == list(centroids):
            break
        centroids = new_centroids
        
    return centroids, clusters


centroids1, clusters1 = k_mean(initial_centroids1,data)
#print("\n clusters1: ",clusters1)
print("\n centroids1: ",centroids1)

centroids2, clusters2 = k_mean(initial_centroids2,data)
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


# In[ ]:


#k1 = 4
#i_point1 = [4.9511002  8.08344216]
#initial_centroids1 = [(4.95110019635643, 8.083442157717421), (3.852121462721742, -1.0871522588579658), (9.269988642319534, 9.62492868721418), (3.0410170219628694, -0.3613848735372547)]
#centeriod1 = [[3.2125746077046626, 2.496580865799525], [3.392621139896188, 6.892881496955304], [7.135607267157955, 7.916517263892731], [7.2270767273807826, 2.5223436136880415]] 
#cost1 = 797.9601840789951

#k2 = 6
#i_point2 = [7.80003043 1.90963115]
#initial_centroids2 = [(7.800030429218029, 1.9096311528449488), (2.952979239506114, 9.650738988423363), (3.852121462721742, -1.0871522588579658), (9.269988642319534, 9.62492868721418), (1.2016224757833955, 7.686397144324093), (3.0410170219628694, -0.3613848735372547)]
#centeriod2 = [[2.5633381461259046, 6.978224800606624], [3.145061482959145, 0.9077065486588153], [3.4955665791995627, 3.5661123157286907], [5.464277356727894, 6.837713536435891], [7.414192434680615, 2.3216911383868664], [7.756483249146484, 8.556689279063415]]
#cost2 = 476.11875167635293




