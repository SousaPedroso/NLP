This repository contains explanations, pieces of code and projects that I considered important for my understading of the main aspects of NLP

## Data Preprocessing

This section presents the definitions and examples of the main techniques to text processing.

### Stemming and lemmatisation

I like these definition from the wikipedia to distinguish between [stemming](https://en.wikipedia.org/wiki/Stemming) and [lemmatisation](https://en.wikipedia.org/wiki/Lemmatisation):

```
In linguistic morphology and information retrieval, stemming is the process for reducing inflected (or sometimes derived) words to their stem, base or root form—generally a written word form. The stem need not be identical to the morphological root of the word; it is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root.
```

```
Lemmatisation (or lemmatisation) in linguistics is the process of grouping together the inflected forms of a word so they can be analysed as a single item, identified by the word's lemma, or dictionary form.

In computational linguistics, lemmatisation is the algorithmic process of determining the lemma of a word based on its intended meaning. Unlike stemming, lemmatisation depends on correctly identifying the intended part of speech and meaning of a word in a sentence, as well as within the larger context surrounding that sentence, such as neighboring sentences or even an entire document. As a result, developing efficient lemmatisation algorithms is an open area of research.
```

That means, since stemming does not necessarily return a valid word, you should use a stemming algorithm when you are not worried about the context of it (e.g. if it's a noun or verb).

The two tables below from Siva Pokala's answer on [stackoverflow](https://stackoverflow.com/questions/1787110/what-is-the-difference-between-lemmatization-vs-stemming) demonstrate this.

![Stem](https://i.stack.imgur.com/q2zMp.png)

![Lemma](https://i.stack.imgur.com/0ESAC.png)

### Bag of Words

After obtaining the stem or lemma of a word, we can demark them as _tokens_, as a unit of data for which a machine learning model will be fitted. Considering all _tokens_ we have in our dataset, we can use a small fragment of phrase (sentence) of a text to represent an input to be analised and classified, which is generally refered as a document. To represent this sentence, we can indicate for each sentence the presence or absence of a word in the sentence (binary) or the frequency of each word. The [image](https://www.ronaldjamesgroup.com/blog/grab-your-wine-its-time-to-demystify-ml-and-nlp) below shows an example:

![Bag Of Words](https://res.cloudinary.com/practicaldev/image/fetch/s--qveZ_g7d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/cassieview/intro-nlp-wine-reviews/master/imgs/vectorchart.PNG)

### Term Frequency x Inverse Document Frequency (TF x IDF)

Instead of word counting, we can process _tokens_ of a document with respect to give a balance between words that occurs in many words (which is not a differential) and that occurs a few times. The idea of TF*IDF is to increase the significance of words that have many occurrences and are present in several documents. TF is the frequency of occurrences of a word in a document. According to the wikipedia, The inverse document frequency (idf) is a measure of how much information the word provides, i.e., if it is common or rare across all documents. It is the logarithmically scaled inverse fraction of the documents that contain the word (obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient). The equations below show how compute each formula.

![TF formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd4f8a91dd0d28a11c00c94a13a315a5b49a8070)

![IDF formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/ac67bc0f76b5b8e31e842d6b7d28f8949dab7937)