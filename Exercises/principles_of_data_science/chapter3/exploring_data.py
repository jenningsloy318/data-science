#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Jennings Liu@ 2017-06-10 22:14:17

import pandas as pd

yelp_raw_data = pd.read_csv("yelp.csv")
print(yelp_raw_data.head())
print(yelp_raw_data.shape)
print("Missing data pionts: \n%s"%yelp_raw_data.isnull().sum())
print("Features of business_id: \n%s"%yelp_raw_data['business_id'].describe())
duplicate_text = yelp_raw_data['text'].describe()['top']
text_is_the_duplicate = yelp_raw_data['text'] == duplicate_text
print(text_is_the_duplicate)
print(text_is_the_duplicate.head())
print(yelp_raw_data[text_is_the_duplicate])
print(yelp_raw_data['stars'].describe())
print(yelp_raw_data['stars'].value_counts())
dates = yelp_raw_data['stars'].value_counts()
#dates.sort()
dates.plot(kind='bar')
