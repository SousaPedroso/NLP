#! /bin/bash

mkdir data
cd data
wget https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip -O sms_spam_collection.zip
unzip sms_spam_collection.zip
rm -rf sms_spam_collection.zip

conda create -n spam_classifier python=3.10 pipenv -y