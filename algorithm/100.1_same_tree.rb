#-------------------------------------------------------------------------------
#    Same Tree
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/same-tree/
# Completed 6/25/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(tree1, tree2)
  if not tree1 and not tree2
    true
  elsif not tree1 or not tree2
    false
  else
    left = is_same_tree(tree1.left, tree2.left)
    right = is_same_tree(tree1.right, tree2.right)
    left and right and tree1.val == tree2.val
  end
end

