class LinkedList:
    def __init__(self):
        self.head = None   # shuru me list khali hai

    # 1. End me add karo
    def append(self, data):
        new_node = Node(data)
        if self.head is None:          # list khali hai
            self.head = new_node
            return
        current = self.head
        while current.next:            # last node tak jao
            current = current.next
        current.next = new_node

    # 2. Shuru me add karo
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Print karo
    def display(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items) + " -> None")

    # 4. Search karo
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 5. Delete karo (value se)
    def delete(self, key):
        current = self.head

        # Case 1: head hi delete karna hai
        if current and current.data == key:
            self.head = current.next
            return

        # Case 2: beech ya end me
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:            # mila hi nahi
            print(f"{key} list me nahi hai")
            return

        prev.next = current.next       # current ko skip kar do

    # 6. Length
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 7. Reverse
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next    # agla node yaad rakho
            current.next = prev   # link ulta karo
            prev = current        # prev aage badhao
            current = nxt         # current aage badhao
        self.head = prev
