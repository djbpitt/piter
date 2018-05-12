import text_from_word
import re
import nltk
from textblob import TextBlob
text = text_from_word.get_docx_text('брат_кинопоиск_рецензии.docx') # extract text from Word file
# replace non-breaking space characters with spaces, remove asterisks, and convert to lower case
text = text.replace(chr(160),' ').replace('*','').lower() 
tmp = re.split('\s{2,}',text) # split into paragraphs on empty lines
piter_paragraphs = [paragraph for paragraph in tmp if re.search('питер|петербург|ленинград', paragraph)] # keep only relevant paragraphs
full_text = ' '.join(piter_paragraphs)
c = nltk.Text(full_text.split())
targets = sorted(set([word for word in c if re.search('питер|петербург|ленинград', word)]))
for item in targets:
    c.concordance(item)
