# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def traverse_sum(node, l, r)
  if node.nil?
    return 0
  end
  if node.val < l
    sub_left_sum = 0
    sub_right_sum = traverse_sum(node.right, l, r)
    node_val = 0
  elsif node.val > r
    sub_left_sum = traverse_sum(node.left, l, r)
    sub_right_sum = 0
    node_val = 0
  else
    sub_left_sum = traverse_sum(node.left, l, r)
    sub_right_sum = traverse_sum(node.right, l, r)
    node_val = node.val
  end
  return sub_left_sum + sub_right_sum + node_val
end

def range_sum_bst(root, l, r)
  if root.nil?
    return 0
  end
  return traverse_sum(root, l, r)
end
