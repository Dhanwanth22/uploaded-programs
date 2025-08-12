class BookStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, title):
        if len(self.stack) < self.size:
            self.stack.append(title)
            print(f'"{title}" added.')
        else:
            print("Stack is full.")

    def pop(self):
        if self.stack:
            print(f'"{self.stack.pop()}" removed.')
        else:
            print("Stack is empty.")

    def peek(self):
        if self.stack:
            print(f'Top book: "{self.stack[-1]}"')
        else:
            print("Stack is empty.")

    def display(self):
        print("Stack:", list(reversed(self.stack)) or "Empty")

s = BookStack(int(input("Enter stack size: ")))
while True:
    print("\n1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    c = input("Enter choice: ")
    if c == '1':
        s.push(input("Enter book title: "))
    elif c == '2':
        s.pop()
    elif c == '3':
        s.peek()
    elif c == '4':
        s.display()
    elif c == '5':
        break
    else:
        print("Invalid choice.")
