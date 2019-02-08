import sys
from notebook import Note, NoteBook


class Menu(object):

    '''Menu details for user to select choices.'''

    def __init__(self):
        '''Choices initialization for users.'''
        self.notebook = NoteBook()
        self.choices = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit}

    def display_menu(self):
        '''Display menu list for users.'''
        print("""Note book menu
              1 Show all notes
              2 Search notes
              3 Add note
              4 Modify note
              5 Quit""")

    def run(self):
        '''Display the main menu option user to enter.'''
        while True:
            self.display_menu()
            choice = input("Enter a choice: ")
            action = self.choices.get(choice, None)
            if action is None:
                raise ValueError("Invalid choice entered, check the display the menu.")
            action()
            
    def show_notes(self, notes=None):
        '''Listing all the existing notes.'''
        if notes is None:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id} {note.memo} {note.tags}")
        
    def search_notes(self):
        '''Search notes as per the user input.'''
        search = input("Enter the notes: ")
        notes = self.notebook.search(search)
        self.show_notes(notes)

    def add_note(self):
        '''Add memo to notebook.'''
        memo = input("Enter the memo to add: ")
        self.notebook.new_note(memo)
        print("Note has been added.")

    def modify_note(self):
        '''Modify the note based on note id.'''
        id = input("Enter the note_id: ")
        memo = input("Enter the memo details: ")
        tags = input("Enter the tags details: ")
        if memo:
            self.notebook.edit_memo(id, memo)
        if tags:
            self.notebook.edit_tags(id, tags)

    def quit(self):
        '''Exit the display option,'''
        print("Thank you for using notebook today.")
        sys.exit(0)

if __name__ == '__main__':
    menu = Menu()
    menu.run()

