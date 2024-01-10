book_name = input()
count_books = 0

while True:
    current_name = input()

    if book_name == current_name:
        print(f"You checked {count_books} books and found it.")
        break
    if current_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
        break
    count_books += 1
