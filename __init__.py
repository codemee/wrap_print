import unicodedata

class WrapPrint:
    def __init__(self, width=80):
        self.width = width
        self.pos = 0

    def print(self, text, end='\n'):
        while True:
            if text == '': # no text left
                break
            next_pos = text.find('\n') # find the next newline
            next_pos = next_pos if next_pos != -1 else len(text) # split text
            next_pos += 1 # include the newline
            part = text[:next_pos]
            text = text[next_pos:]
            for ch in part:
                print(ch, end='')
                if ch == '\n':
                    self.pos = 0
                    continue
                self.pos = self.pos + 1 + (1 if unicodedata.east_asian_width(ch) in 'WF' else 0)
                if self.pos >= self.width:
                    print('')
                    self.pos = 0
        print(end, end='')                    
