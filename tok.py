import re

class Tokenizer:
    def __init__(self):
        pass
        
    def Tokenize(self ,text):
        # Tokenize the corpus
        text = text.lower()
        # substitution
        text = self.Substitution(text)
        # divide into sentences
        sentences = self.SentenceTokeniser(text)
        output = []
        for sentence in sentences:
            # divide into words
            words = self.WordTokeniser(sentence)
            output.append(words)
        return output

    def Substitution(self, text):
        # URL substitution
        text = re.sub(r'(https?://|www\.|http?://)[\w.-]+\.[\w]+\w+', '<URL>', text)
        # hashtag substitution
        text = re.sub(r'#\w+', '<HASHTAG>', text)
        # Email substitution
        text = re.sub(r'\w+@\w+\.\w+', '<MAILID>', text)
        # @mention substitution
        text = re.sub(r'@\w+', '<MENTION>', text)
        # number substitution
        text = re.sub(r'\d+', '<NUMBER>', text)
        # percentage substitution
        text = re.sub(r'\d+%', '<PERCENT>', text)
        # date substitution
        text = re.sub(r'\d{1,2}[-/.]\d{1,2}[/.-]\d{2,4}', '<DATE>', text)
        # replacing [ digit ] to space
        text=re.sub(r'\[\s*(\d+)\s*\]',' ',text)
        # removing all white spaces
        text=re.sub(r'\s+',' ',text)
        # Decimal
        text=re.sub(r'\d+\.\d+','<DECIMAL>',text)
        # replace xn't with xnnot
        text = re.sub(r'n\'t', r'nnot', text)
        # replace x'm with x + am
        text = re.sub(r'\'m', r' am', text)
        # replace x're with x + are
        text = re.sub(r'\'re', r' are', text)
        # replace x'll to x + will
        text = re.sub(r'\'ll', r' will', text)
        # replace x'd to x + would
        text = re.sub(r'\'d', r' would', text)
        # replace x've to x + have
        text = re.sub(r'\'ve', r' have', text)
        # replacing double punctuations
        text =re.sub(r'([{*.,-/&^%!_+=?;><}])\1+',r'\1',text)
        #replacing words like _word_,_word,word_
        text=re.sub(r'_(\w+)_',r' \1',text)
        text=re.sub(r'_(\w+)',r' \1',text)
        text=re.sub(r'(\w+)_',r' \1',text)
        #replacing words like —word—,—word,word—
        text=re.sub(r'—\s+(\w+)\s+—',r' \1',text)
        text=re.sub(r'—(\w+)',r' \1',text)
        text=re.sub(r'(\w+)—',r' \1',text)
        #replacing words like -word-,-word,word-
        text=re.sub(r'-(\w+)-',r' \1',text)
        text=re.sub(r'-(\w+)',r' \1',text)
        text=re.sub(r'(\w+)-',r' \1',text)
        text=re.sub(r'mr\.','Mr',text)
        text=re.sub(r'mrs\.','Mrs',text)
        # # handle abbreviations
        # text = re.sub(r'(?:[A-Za-z]\.)+',r'<abb>',text)
        text=re.sub(r'r. w. (robert william)','robert william',text)
        return text
    
    def SentenceTokeniser(self, text):
        # Tokenize the text into sentences
        pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
        return re.split(pattern, text)

    def WordTokeniser(self, sentence):
        # Tokenize the sentence into words
        sentence=re.sub(r'\((\w+)\)',r' \1',sentence)
        # sentence=re.sub(r'([!-_.?^*\'{}\~/$`:"])',r' \1 ',sentence)
        sentence = re.sub(r'([!.?^_\'":,;(){}\~*$`-])', r' \1 ', sentence)
        return sentence.split()
        # pattern = r'\w+'
        # return re.findall(pattern, sentence)
