# Leetcode 297. Serialize and Deserialize Binary Tree
# Hard 1/14/21

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [1]
# Output: [1]

# Example 4:

# Input: root = [1,2]
# Output: [1,2]

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 104].
#     -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# T: O(a) visit each node exactly once. a is number of nodes.
# S: O(a), we keep the entire tree, either at the beginning or at the end. 


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Complexity Analysis

#     Time complexity : in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is O(N)O(N)O(N), where NNN is the number of nodes, i.e. the size of tree.

#     Space complexity : in both serialization and deserialization functions, we keep the entire tree, either at the beginning or at the end, therefore, the space complexity is O(N)O(N)O(N).

# The solutions with BFS or other DFS strategies normally will have the same time and space complexity.




# Solution 2
# Super fast



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = [root.val]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            res.append("null")
            if front.left:
                q.append(front.left)
                res[-1] = front.left.val
            res.append("null")
            if front.right:
                q.append(front.right)
                res[-1] = front.right.val
        while res and res[-1] == 'null':
            res.pop()
  
        return ','.join(map(str,res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == '[]':
            return None
        vals = data.split()
        root = TreeNode(vals[0])
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# Solution 3 
# 108 ms



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = [root.val]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            res.append("null")
            if front.left:
                q.append(front.left)
                res[-1] = front.left.val
            res.append("null")
            if front.right:
                q.append(front.right)
                res[-1] = front.right.val
        while res and res[-1] == 'null':
            res.pop()
  
        return ','.join(map(str,res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == '[]':
            return None
        vals = data.split()
        root = TreeNode(vals[0])
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

