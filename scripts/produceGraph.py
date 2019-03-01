#input HF.txt, SF.txt
#output something.graph

import networkx as nx

# computes the edit distance of two strings.
def editDistance(v, w):

    return 1

# parses the data into a list.
def readData(filename):

    sequences = {}
    file = open(filename, 'r')

    # append all lines without the newline to the sequences list.
    for line in file:

        seq, tag = line[:-1].split(", ")
        sequences[seq] = tag

    return sequences


# takes the data and creates a graph
def createGraph(sequences, K):

    seqGraph = nx.Graph()
    seqGraph.add_nodes_from(sequences.keys())

    # go through all sequences and find the pairwise distance.
    for seq in sequences:
        
        for pair in sequences:

            # skip itself
            if seq == pair:
                continue

            # otherwise determine if it's pairwise distance is less than K
            else:
                dist = editDistance(seq, pair)
                if dist < K:
                    seqGraph.add_edge(seq, pair, weight=dist)
                else:
                    continue

    return seqGraph

# takes a graph and prints out a text file of the .graph format
# nodes first followed by their tag then the edges in start, end, weight format.
def printGraph(seqGraph):

    return
    
            
