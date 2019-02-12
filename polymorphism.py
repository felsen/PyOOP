

class AudioFile(object):

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise ValueError("Invalid file extension.")


class MP3file(AudioFile):

    ext = ".mp3"

    def play(self):
        return f"Playing {self.ext} file."


class WavFile(AudioFile):

    ext = ".wav"

    def play(self):
        return f"Playing {self.ext} file."


class OggFile(AudioFile):

    ext = ".ogg"

    def play(self):
        return f"Playing {self.ext} file."


class FlacFile(object):

    ext = ".flac"

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise ValueError("Invalid file extension.")
        self.filename = filename

    def play(self):
        return f"Playing {self.ext} file."
