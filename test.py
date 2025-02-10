import re
import nltk # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
nltk.download("punkt_tab")
from nltk.corpus import stopwords # type: ignore
nltk.download('stopwords')
from nltk.stem import PorterStemmer # type: ignore


class TextToNum:
    def _init_(self,text):
        self.text=text

    def cleaner(self):
        text = re.sub(r',','',self.text)
        cleaned_text = re.sub(r'[^\w\s]', '', text)  # Removes everything except word characters and spaces
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replaces multiple spaces with a single space
        cleaned_data = cleaned_text.strip()  # Removes leading/trailing whitespace
        self.cleaned=cleaned_data

    def token(self):
        self.tkns=word_tokenize(self.cleaned)

    def removeStop(self):
        stop=stopwords.words('english')
        self.cl = [i for i in self.tkns if i not in stop]

    def stemme(self):
        ps=PorterStemmer()
        self.st = [ps.stem(word) for word in self.cl]
        return self.st
