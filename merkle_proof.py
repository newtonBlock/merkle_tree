from utils import *
import math
from node import Node
from merkle_tree import MerkleTree
from hash_data_structures import *


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE

    # height == the number of hash partner needed to reach block header
    tree_h = merkle_tree.height
    #print(tree_h)
    leaves = list(merkle_tree.leaves)
    #print(leaves)
    num_leaves = len(leaves)
    num_of_verify_nodes = tree_h

    #one leave
    if num_leaves == 1:
        return []

    #the return nodes
    valid_nodes = []

    #deal with leaves
    #two conditions: tx 
    tx_index = leaves.index(tx)

    #postion is even or odd
    if tx_index % 2 == 0:
        #even, so the nearest hash neighor is front: less 1
        #first_hash_partner = tx_index + 1
        first_partner_node = Node('r', leaves[tx_index + 1])

    else:
        #odd, so the nearest hash neighor is back: plus 1
        #first_hash_partner = tx_index - 1
        first_partner_node = Node('l', leaves[tx_index - 1])

    valid_nodes.append(first_partner_node)

    if(num_leaves >= 4):
    #from leaves to the first hashnodes
        nodes = []
        for tx in range(0, num_leaves, 2):
            nodes.append(HashLeaf(leaves[tx],leaves[tx+1], 'sha256'))
        
        index = tx_index // 2
        if index % 2 == 0:
            #valid_nodes.append(nodes[index + 1])
            parnter_node = Node('r', nodes[index + 1].data)
        else:
            #valid_nodes.append(nodes[index - 1])
            parnter_node = Node('l', nodes[index - 1].data)

        valid_nodes.append(parnter_node)
    

    if(num_leaves >= 8):   
        #hierarchy hash nodes to upper level       
        k = 0
        num = int(num_leaves / 2)
        index = index // 2
        while k < num_of_verify_nodes - 2:
            #hash to upper level
            for tx in range(0, num, 2):
                nodes.append(HashNode(nodes.pop(0), nodes.pop(0), 'sha256'))

            if index % 2 == 0:
                parnter_node = Node('r', nodes[index + 1].data)
            else:
                parnter_node = Node('l', nodes[index - 1].data)    

            valid_nodes.append(parnter_node)
                    
            k += 1        
            num = int(num / 2)
            index = index // 2    
    


    return valid_nodes


def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE
    
    valid_nodes = merkle_proof
    
    for vnode in valid_nodes:
        if vnode.direction == 'l':
            tx = hash_data(vnode.tx + tx, 'sha256')
        else:
            tx = hash_data(tx + vnode.tx, 'sha256')
            
    return tx

    
if __name__ == "__main__":

    tx_list1 = ['5','3','11','9']
    mk_test = MerkleTree(tx_list1)
    root = mk_test.block_header
    #nodes = merkle_proof('11',mk_test)
    #node = nodes.pop(2)
    print(root)

    head = verify_proof('5', merkle_proof('5', MerkleTree(tx_list1)))
    print(head)
    """
    txs1 = tx_list1[0] + tx_list1[1]
    hashend1 = hash_data(txs1, 'sha256')

    txs2 = tx_list1[2] + tx_list1[3]
    hashend2 = hash_data(txs2, 'sha256')

    txs3 = tx_list1[4] + tx_list1[5]
    hashend3 = hash_data(txs3, 'sha256')

    txs4 = tx_list1[6] + tx_list1[7]
    hashend4 = hash_data(txs4, 'sha256')

    hashend = hash_data( hashend1 + hashend2, 'sha256')
    print(hashend)  
    """
