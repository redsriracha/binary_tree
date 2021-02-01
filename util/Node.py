class Node:
    def __init__(self, value=None):
        super().__init__()
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value == None:
            self.value = value
        # Check Left
        elif value < self.value:
            # Assign to Left if None
            if self.left == None:
                self.left = Node(value)
            # Move Left
            else:
                self.left.add(value)
        # Check Right
        elif value > self.value:
            # Assign to Right if None
            if self.right == None:
                self.right = Node(value)
            # Move Right
            else:
                self.right.add(value)
        # Do not duplicate
        else:
            pass

    def __str__(self):
        return str(self.value)
