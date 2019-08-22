#!/usr/bin/env python
# coding: utf-8

# # Library for importing a json file

# In[1]:


import json


# In[2]:


def quiz():
    with open('quiz.json') as json_file:
        data = json.load(json_file)
    print("Select Category")
    print("Press 1 for Sport.")
    print("Press 2 for Maths.")
    user=input()
    answer = []
    if user=='1':
        temp_dict = data['quiz']['sport']
        for k,v in temp_dict.items():
            z = dict(v)
            print(z['question'])
            for i in z['options']:
                print(i,"\n")
            answer.append(input("\nEnter the answer:"))
    if user=='2':
        temp_dict = data['quiz']['maths']
        for k,v in temp_dict.items():
            z = dict(v)
            print(z['question'])
            for i in z['options']:
                print(i)
            answer.append(input("\nEnter the answer:"))
    #         print(k,v)
    return answer


# # Result

# In[3]:


print(quiz())


# In[ ]:




