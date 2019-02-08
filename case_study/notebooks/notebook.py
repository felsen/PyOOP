import datetime


last_id = 0


class Note(object):

    '''Represents the note in notebook, search, and storing notes for notebook.'''

    def __init__(self, memo, tags=''):
        '''Initialization of memo and optional arguments.'''
        self.memo = memo
        self.tags = tags
        global last_id
        self.id = (last_id + 1)
        last_id = self.id
        self.creation_date = datetime.datetime.today()

    def match(self, name):
        '''Match any name memo or tags'''
        return name in self.memo or name in self.tags


class NoteBook(object):
    
    '''Collection of Notebook that can be tagged, modified, or searched.'''

    def __init__(self):
         '''Initialize the notebook with empty list.'''
         self.notes = []

    def new_note(self, memo, tags=''):
         '''Adding notes from notebook'''
         self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
         '''Find the note based on note id'''
         for note in self.notes:
             if str(note.id) == str(note_id):
                 return note
         return None

    def edit_memo(self, note_id, memo):
         '''Editing memo from notebook'''
         note = self._find_note(note_id)
         if note is not None:
             note.memo = memo
             return
         raise ValueError("Invalid note id provided.")

    def edit_tags(self, note_id, tags=''):
         '''Editing tags from notebook'''
         note = self._find_note(note_id)
         if note is not None:
             note.tags = tags
             return
         raise ValueError("Invalid note id provided.")

    def search(self, memo_or_tags):
        '''Searching memo or tags from notebook'''
        return [note for note in self.notes if note.match(memo_or_tags)]

