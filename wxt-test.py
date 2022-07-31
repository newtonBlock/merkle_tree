from hash_data_structures import HashLeaf, HashNode
from utils import hash_data
from merkle_tree import MerkleTree
from node import Node

"""
tx1 = 'wxt'
tx2 = 'dlp'
tx3 = 'wjs'
tx4 = 'wrl'

data = tx1 + tx2
data = hash_data(data)
#print(data) 

data2 = tx3 + tx4
data2 = hash_data(data2)
#print(data)

data3 = hash_data(data + data2)
print(data3)

left_node = HashLeaf(tx1,tx2,'sha256')
right_node = HashLeaf(tx3,tx4, 'sha256')
node = HashNode(left_node, right_node, 'sha256')

print(node.data)
print(node.height)
"""

"""
//
tx1 = 'wxt'
tx2 = 'dlp'
tx3 = 'wjs'
tx4 = 'wrl'

tx_list = [tx1, tx2, tx3, tx4]
print(tx_list)

mt = MerkleTree(tx_list,)
print(mt.height)
print(mt.block_header)
print(mt.leaves)
print(mt.hash_function)
"""

tx1 = 'wxt'
tx2 = 'dlp'
tx_list = [tx1, tx2]
mt = MerkleTree(tx_list)

node1 = Node('l',tx1)
#print(node1.direction)
#print(node1.tx)
print([Node('l', tx1)])
print(mt.height)