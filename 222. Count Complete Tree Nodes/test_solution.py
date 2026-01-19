from solution import Solution, TreeNode

def test_solution():
    sol = Solution()
    
    # Helper to build tree from list (level order)
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Example 1
    root1 = build_tree([1,2,3,4,5,6])
    expected1 = 6
    assert sol.countNodes(root1) == expected1, f"Test 1 Failed: {sol.countNodes(root1)}"
    print("Test 1 Passed")

    # Example 2
    root2 = build_tree([])
    expected2 = 0
    assert sol.countNodes(root2) == expected2, f"Test 2 Failed: {sol.countNodes(root2)}"
    print("Test 2 Passed")

    # Example 3
    root3 = build_tree([1])
    expected3 = 1
    assert sol.countNodes(root3) == expected3, f"Test 3 Failed: {sol.countNodes(root3)}"
    print("Test 3 Passed")

    # Edge case: Perfect tree
    root4 = build_tree([1,2,3,4,5,6,7])
    expected4 = 7
    assert sol.countNodes(root4) == expected4, f"Test 4 Failed: {sol.countNodes(root4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
