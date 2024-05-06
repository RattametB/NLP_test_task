import pdf2image
from PIL import Image
import pytesseract
from razdel import tokenize
from langdetect import detect
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pymorphy2

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def text_extracter(file_path,n_page = None):
    image = pdf2image.convert_from_path(file_path)
    detected_text = ''
    for pagenumber, page in enumerate(image):
        detected_text += pytesseract.image_to_string(page, lang="rus+eng")
        if n_page != None:
            if pagenumber == n_page:
                break
    return detected_text

def clean_text(text):
    cleaned_text = ' '.join(word for word in text.split() if word.isalnum())
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def language_detecor(token):
    try:
        lang = detect(token)
        if lang == 'ru':
            return 'russian'
        elif lang == 'en':
            return 'english'
    except:
        return 'num'
    
def language_saperator(text):
    rus_text = ''
    eng_text = ''
    current_lang = None
    text_list = text.split()
    for text in text_list:
        lang = language_detecor(text)
        if lang == 'russian':
            rus_text += text+' '
            current_lang = 'russian'
        elif lang == 'english':
            eng_text += text+' '
            current_lang = 'english'
        else:
            if current_lang == 'russian':
                rus_text += text+' '
            else:
                eng_text += text+' '
    return rus_text,eng_text

def tokenize_text(text, language):
    if language == 'russian':
        tokens = [element.text for element in list(tokenize(text))]
    elif language == 'english':
        tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens, language):
    stopwords_list = stopwords.words(language)
    return [token for token in tokens if token not in stopwords_list]

def lemmatize_text(text, language):
    if language == 'russian':
        lemmatizer = pymorphy2.MorphAnalyzer()
        tokens = [lemmatizer.parse(token)[0].normal_form for token in text]   
    elif language == 'english':
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in text]
    return tokens
