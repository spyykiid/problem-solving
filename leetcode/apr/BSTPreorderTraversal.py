from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
      head = None
      for pre in preorder:
        if head is None:
          head = TreeNode(pre)
        if pre < head.val:
          head.left = TreeNode(pre)
          head = head.left 
        elif pre > head.val:
          head.right = TreeNode(pre)
          head = head.right

        print(pre, head.val)


    def bst_preorder(self, preorder):
      def helper(low= float('-inf'), high=float('inf')):    
        nonlocal i

        if i==n:
          return None
        
        val = preorder[i]

        if val < low or val > high:
          return None
        
        i += 1
        root = TreeNode(val)
        root.left = helper(low, val)
        root.right = helper(val, high)
        return root
      
      i=0
      n = len(preorder)
      return helper()

    


def main():
  s = Solution()
  s.bst_preorder([8,5,1,7,10,12])


if __name__ == '__main__':
  main()