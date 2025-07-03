def add_note():
    note = input("Enter a new note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added!")

def list_notes():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
    for i, note in enumerate(notes):
        print(f"{i+1}: {note.strip()}")

if __name__ == "__main__":
    print("1. Add Note")
    print("2. List Notes")
    choice = input("Choose an option: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
