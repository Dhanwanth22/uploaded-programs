# Stack size
MAX_SIZE = 5

# Initialize stack
stack = [None] * MAX_SIZE
top = -1

# Push operation
def push(book_title):
    global top
    if top == MAX_SIZE - 1:
        print("Error: Stack is full (Overflow). Cannot push.")
    else:
        top += 1
        stack[top] = book_title
        print(f"'{book_title}' pushed onto the stack.")

# Pop operation
def pop():
    global top
    if top == -1:
        print("Error: Stack is empty (Underflow). Cannot pop.")
    else:
        removed_book = stack[top]
        stack[top] = None
        top -= 1
        print(f"'{removed_book}' popped from the stack.")

# Peek operation
def peek():
    if top == -1:
        print("Error: Stack is empty. Nothing to peek.")
    else:
        print(f"Top of stack: '{stack[top]}'")

# Display stack contents
def display():
    if top == -1:
        print("Stack is empty.")
    else:
        print("\nStack contents (Top to Bottom):")
        for i in range(top, -1, -1):
            print(f"  {stack[i]}")

# Main menu
if __name__ == "__main__":
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push (Add Book Title)")
        print("2. Pop (Remove Book Title)")
        print("3. Peek (Top Book Title)")
        print("4. Display Stack")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book = input("Enter book title to push: ")
            push(book)
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
