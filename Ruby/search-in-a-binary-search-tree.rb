# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def search_bst(root, val)
  if root.nil?
    return nil
  end
  if root.val == val
    return root
  elsif val > root.val
    return search_bst(root.right, val)
  else
    return search_bst(root.left, val)
  end
end
