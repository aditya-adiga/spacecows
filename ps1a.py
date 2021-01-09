###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import csv

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    
    cows_dict = {}
    
    fin = open(filename, mode='r')
    for line in fin:
        cow_details = line.split(',')
        cows_dict[cow_details[0]] = int(cow_details[1].rstrip())
    fin.close() 
    
    return cows_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    values=[]
    
    cow_sorted={key: value for key, value in sorted(cows.items(), key=lambda item: item[1],reverse=True)}
    cow_list=[]
    total=0
    cow=[]
    for i in cow_sorted:
        
        if(cow_sorted[i]+total<10):
            cow.append(i)
            total+=cow_sorted[i]
        
        else:
            cow_list.append(cow)
            cow=[i]
            total=cows[i]
    cow_list.append(cow)
    return [x for x in cow_list if x != []]

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
   
    cow_dict={}
    for i in get_partitions(cows.keys()):
        total=0
        for j in i:
            total+=1
            lim=0
            for k in j:
                lim+=cows[k]
            if(lim>limit):
                total=-1
                break
        if(total!=-1):
            cow_dict[str(i)]=total
        
            
    cow_sorted={key: value for key, value in sorted(cow_dict.items(), key=lambda item: item[1])}  
    return list(cow_sorted)[0]
        
        
        
# Problem 4
def compare_cow_transport_algorithms(path):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows=load_cows(path)
    start_time=time.time()
    greedy=greedy_cow_transport(cows)
    print(greedy)
    print("no of trips: "+str(len(greedy)))
    end_time=time.time()
    print(end_time-start_time)
    start_time=time.time()
    brute_force=brute_force_cow_transport(cows)
    count=0
    print(brute_force)
    end_time=time.time()
    for i in brute_force:
        if(i=='['):
            count+=1
    print('no of trips: '+str(count-1))
    print(end_time-start_time)
compare_cow_transport_algorithms("E:\projects\ps1\ps1_cow_data.txt")