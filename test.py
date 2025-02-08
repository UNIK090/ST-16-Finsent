import re
class TextToNum:
    def __init__(self):
        self.text=text
    def cleaner(self):
        text = re.sub(r',','',self.text)
        cleaned_text = re.sub(r'[\w\s]', '',text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_data = cleaned_text.strip()
        self.cleaned=cleaned_data
    def tokenize(x) for x in 

