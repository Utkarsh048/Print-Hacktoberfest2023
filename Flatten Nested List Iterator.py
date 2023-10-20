class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Initialize a stack to help with iteration
        self.stack = []
        
        # Add the nestedList to the stack in reverse order
        # so that we can pop the elements in the correct order
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        # Ensure the stack is not empty
        if self.hasNext():
            # Pop the next element from the stack
            return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # While the stack is not empty
        while self.stack:
            # Get the top element from the stack
            top = self.stack[-1]
            
            # If the top element is an integer, return True
            if top.isInteger():
                return True
            
            # If the top element is a list, pop it and add its elements to the stack in reverse order
            self.stack.pop()
            for item in reversed(top.getList()):
                self.stack.append(item)
        
        return False
