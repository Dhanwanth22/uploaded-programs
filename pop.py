Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> MAX = 5  # Maximum size of the stack
stack = []  # Empty stack

def push():
    if len(stack) == MAX:
        print("Stack is full. Cannot add more books.")
    else:
        book = input("Enter book title to push: ")
        stack.append(book)
        print(f'"{book}" has been added to the stack.')

def pop():
    if not stack:
        print("Stack is empty. No book to pop.")
    else:
        book = stack.pop()
        print(f'"{book}" has been removed from the stack.')

def peek():
    if not stack:
        print("Stack is empty. No book to display.")
    else:
        print(f'Top book: "{stack[-1]}"')

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Books in the stack (Top to Bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(f"{i+1}. {stack[i]}")

# Menu-driven code
while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Push (Add Book)")
    print("2. Pop (Remove Book)")
    print("3. Peek (View Top Book)")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting stack program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
