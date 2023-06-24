Spam classifier created to fix the knowledge using the text processing methods: stemming and BoW.

The dataset used can be downloaded at https://archive.ics.uci.edu/dataset/228/sms+spam+collection. It was used a Naive Bayes model for training. After running [setup.sh](/spam_classifier/setup.sh) with bash, use the following code to finish the environment settings.

```bash
conda activate spam_classifier
pipenv install .
pipenv shell
```