from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tqdm.auto import tqdm
def build_features(df_reviews):
    df_reviews=df_reviews.drop_duplicates(subset=set(df_reviews).remove('tconst'))
    df_reviews=df_reviews.dropna()

    lemmatizer  = WordNetLemmatizer()

    def lematizer(text):
        tokens = word_tokenize(text.lower())

        lemmas = [lemmatizer.lemmatize(token) for token in tokens] 
        
        return " ".join(lemmas)
    texts=df_reviews['review']
    lematized=[]
    for text in tqdm(texts):
        lematized.append(lematizer(text))
    df_reviews['review_norm'] = lematized
    return df_reviews