#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 02:08:09 2018

Simplified, but functional, autograder to check your work for Bioinformatics pa04.

As you can see below, your program-related grade is computed as follows:
    proportion correct * 95
    + 5 if you implement the used learning algorithm from scratch

NOTE: 
I will pass in DIFFERENT train and test breakdowns from the same data,
for the real grading than are imported here.
This means your grade will likely differ sligtly from what this reports.

@author: taylor@mst.edu
"""

import Salings_Hanna
import numpy as np
import pandas as pd


learner = Salings_Hanna.my_class_learning_wrapper()
learner.train('GSE73002_breast_cancer_train.csv')
my_results = learner.test('GSE73002_breast_cancer_test.csv')

test_df = pd.read_csv('GSE73002_breast_cancer_test.csv')
correct_results = np.array(test_df['breast cancer'])

your_grade = list(correct_results == my_results).count(True) / len(correct_results)
your_grade *= 95
if learner.from_scratch():
    your_grade += 5
print('\nYour percentage of program-related points is: ', your_grade)
