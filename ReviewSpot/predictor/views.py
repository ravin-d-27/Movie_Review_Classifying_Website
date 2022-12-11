from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, 'predictor/home.html')

def pred(request):
    return render(request, 'predictor/preds.html')

def find(request):
    import re
    import pickle
    import tensorflow as tf
    import nltk
    import numpy as np
    nltk.download("stopwords")
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer 

    corpus = []
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    if request.method == 'POST':
        review = request.POST['review']
        reviews = re.sub("[^a-zA-Z]", " ", review)
        reviews = reviews.lower()
        reviews = reviews.split()
        ps = PorterStemmer()
        reviews = [ps.stem(word) for word in reviews if not word in set(all_stopwords)]
        reviews = ' '.join(reviews)
        corpus.append(reviews)

        file_open = open("predictor/vectorise.dat", "rb+")
        vect = pickle.load(file_open)

        md = tf.keras.models.load_model("predictor/Trained_Model.h5")
        a = vect.transform(corpus).toarray()
        p = md.predict(a)

        predict = np.argmax(p)

        st = ""
        if (predict==1):
            st = "The Given review is a Positive Review"
        else:
            st = "The Given review is a Positive Review"
        
        print(st)

    return render(request, 'predictor/finder.html', {"msg":st, "rev":review})