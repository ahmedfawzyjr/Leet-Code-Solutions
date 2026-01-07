class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Use a stack to process directory names.
        
        - '..' means go up one directory (pop from stack)
        - '.' means current directory (ignore)
        - empty string (from consecutive slashes) is ignored
        - everything else is a valid directory name
        
        Time: O(n)
        Space: O(n)
        """
        stack = []
        
        # Split by '/' and process each component
        components = path.split('/')
        
        for component in components:
            if component == '' or component == '.':
                # Empty (consecutive slashes) or current directory - skip
                continue
            elif component == '..':
                # Go up one directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(component)
        
        # Build the simplified path
        return '/' + '/'.join(stack)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    print(f"Test 1: {sol.simplifyPath('/home/')}")  # Expected: /home
    
    # Test case 2
    print(f"Test 2: {sol.simplifyPath('/home//foo/')}")  # Expected: /home/foo
    
    # Test case 3
    print(f"Test 3: {sol.simplifyPath('/home/user/Documents/../Pictures')}")  # Expected: /home/user/Pictures
    
    # Test case 4
    print(f"Test 4: {sol.simplifyPath('/../')}")  # Expected: /
    
    # Test case 5
    print(f"Test 5: {sol.simplifyPath('/.../a/../b/c/../d/./')}")  # Expected: /.../b/d
