class PatternNode:
    def __init__(self, pattern, index):
        self.pattern = pattern
        self.index = index
        self.next = None

class PatternList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_pattern(self, pattern):
        new_node = PatternNode(pattern, self.count + 1)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1
        return new_node.index

    def find_pattern(self, pattern):
        current = self.head
        while current:
            if current.pattern == pattern:
                return current.index
            current = current.next
        return None