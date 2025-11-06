class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Display the circular list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
        self.display()

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
        self.display()

    
    # Insert at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position <= 1 or not self.head:
            self.insert_at_beginning(data)
            return

        current = self.head
        count = 1

        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node
        self.display()
    def del_firstnode(self):
        if not self.head:
            print("Empty LL")
            return
        temp = self.head
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = temp.next
        self.head = temp.next

    def del_lastNode(self):
        if not self.head:
            print("Empty LL")
            return
        last = self.head
        while last.next.next != self.head:
            last = last.next

        last.next = self.head

    def delete_at_position(self):
        position = int(input("Enter the postion: "))
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        if position == 1:
            # Only one node
            if self.head.next == self.head:
                self.head = None
                print("Deleted the only node in the list.")
                return

            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted node with value: {deleted_value}")
            return

        current = self.head
        count = 1
        prev = None

        while count < position and current.next != self.head:
            prev = current
            current = current.next
            count += 1

        if count != position:
            print(f"Position {position} is out of range.")
            return

        prev.next = current.next
        print(f"Deleted node with value: {current.data}")

      
    



# Example Menu for User
if __name__ == "__main__":
    cll = CircularLinkedList()

    while True:
        print("\n--- Circular Linked List Menu ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at specific position")
        print("4. Display list")
        print("5. Delete First Node")
        print("6. Delete Last Node")
        print("7. Delete  Node at a given position")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            val = input("Enter value to insert: ")
            cll.insert_at_beginning(val)

        elif choice == '2':
            val = input("Enter value to insert: ")
            cll.insert_at_end(val)

        elif choice == '3':
            val = input("Enter value to insert: ")
            pos = int(input("Enter position: "))
            cll.insert_at_position(val, pos)

        elif choice == '4':
            cll.display()


        elif choice == '5':
            cll.del_firstnode()
            cll.display()

        elif choice == '6':
            cll.del_lastNode()
            cll.display()
        elif choice == '7':
            cll.delete_at_position()
            cll.display()

        elif choice == '8':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter 1–5.")
