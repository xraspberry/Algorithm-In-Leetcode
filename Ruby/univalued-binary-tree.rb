# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

def traverse(node, values)
  if node.nil?
    return true
  end
  if !values.include?(node.val)
    return false
  end
  values.push(node.val)
  if !traverse(node.left, values)
    return false
  end
  if !traverse(node.right, values)
    return false
  end
  return true
end


# @param {TreeNode} root
# @return {Boolean}
def is_unival_tree(root)
  values = []
  values.push(root.val)
  traverse(root, values)
end
