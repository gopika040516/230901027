#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_s_algorithm(examples):
    hypothesis = [None] * (len(examples[0]) - 1)  # Initialize the hypothesis to the most specific hypothesis
    
    for example in examples:
        if example[-1] == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] is None:
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'
    
    return hypothesis

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

hypothesis = find_s_algorithm(training_data)

print("The most specific hypothesis is:", hypothesis)


# In[ ]:




