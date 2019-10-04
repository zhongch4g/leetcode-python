#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 4:58 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : synonymous_queries.py
# @Software: IntelliJ IDEA

"""
Can words have multiple synonyms?
Does word order matter?
Are synonym relationships transitive,
meaning if A is synonymous with B,
and B is synonymous with C,
does that mean A is synonymous with C?
Can synonyms span multiple words,
such as how “USA” is synonymous with “United States of America” or “United States”?
"""
from collections import defaultdict
def synonym_queries(synonym_words, queries):
    '''
    synonym_words: iterable of pairs of strings representing synonymous words
    queries: iterable of pairs of strings representing queries to be tested for
             synonymous-ness
    '''
    synonyms = defaultdict(set)
    for w1, w2 in synonym_words:
        synonyms[w1].add(w2)

    output = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            output.append(False)
            continue
        result = True
        for i in range(len(q1)):
            w1, w2 = q1[i], q2[i]
            if w1 == w2:
                continue
            elif ((w1 in synonyms and w2 in synonyms[w1])
                  or (w2 in synonyms and w1 in synonyms[w2])):
                continue
            result = False
            break
        output.append(result)
    return output