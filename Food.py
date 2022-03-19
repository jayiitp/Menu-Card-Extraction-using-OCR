#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytesseract import Output
import pytesseract
import argparse
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[2]:


image = cv2.imread('food_menu_card.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)


# In[3]:


mylist=[]
for i in range(0, len(results["text"])):
    # extract the bounding box coordinates of the text region from
    # the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    # extract the OCR text itself along with the confidence of the
    # text localization
    text = results["text"][i]
    conf = int(float(results["conf"][i]))
    if conf > 0:
        #print("Confidence: {}".format(conf))
        #print("Text: {}".format(text))
        #print("")
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        mylist.append(text)


# In[4]:


#print(mylist)


# In[5]:


stopwords = ["SLY","","GRANNY","satars","9","\\DD",'He', 'vegetation', 'Henan', 'vageuin', 'ghten', 'ee', 'Al', 'prices', 'are', 'in', 'INR', '=', 'We', 'ley', '10%', 'sevice', 'charg', 'Prices', 'oot', 'ince', 'gover', 'the', 'al', 'of', 'nyo', 'tht', 'maybe', 'wowed']
text0 = [word for word in mylist if word not in stopwords]


# In[6]:


text0=['end' if x=='%' else x for x in text0]


# In[7]:


#print(text0)


# In[8]:


text0=['@%' if x=='#' else x for x in text0]


# In[9]:


text0=['@%' if x=='4%' else x for x in text0]


# In[10]:


text0=['399' if x=='399)' else x for x in text0]


# In[11]:


text0=['@%' if x=='*' else x for x in text0]


# In[12]:


text0=['@%' if x=='%*' else x for x in text0]


# In[13]:


number=[]
string=[]
for i in text0:
    if(i.isdigit()):
        number.append(i)
    else:
        string.append(i)


# In[14]:


#print(number)
#print(len(number))


# In[15]:


price=[]
for i in number:
    if(len(i)==3):
        price.append(i)
#print(price)    
#print(len(price))


# In[16]:


#string=[x.replace('%', '@') for x in string]


# In[17]:


#string=[x.replace('#', '@') for x in string]


# In[18]:


#string=[x.replace(' @', '@') for x in string]


# In[19]:


#string=[x.replace('8@', '@') for x in string]


# In[20]:


#string=[x.replace('4@', '@') for x in string]


# In[21]:


#string=[x.replace('*', '@') for x in string]


# In[22]:


#string=[x.replace('@*', '@') for x in string]


# In[23]:


#string=[x.replace('4:', '@') for x in string]


# In[24]:


#string=[x.replace('@@', '@') for x in string]


# In[25]:


#string=[x.replace('end', '@') for x in string]


# In[28]:


Originals = string
To_remove = ["end", " @@","4:","@*","*",'4@','8@',' @','#','%','@@']
result = []

for t in To_remove:
    for i in range(len(Originals)):
        Originals[i] = Originals[i].replace(t, "@")
#print (Originals)


# In[29]:


#print(string)


# In[30]:


import itertools

def predicate_grouper(li, predicate='@'):
    indices = [i for i,x in enumerate(li) if x.startswith(predicate)]
    slices = [slice(*x) for x in itertools.zip_longest(indices,indices[1:])]
    for sli in slices:
        yield ' '.join(li[sli])


# In[31]:


food=list(predicate_grouper(string))
food=list(predicate_grouper(food))


# In[32]:


for i in range(len(food)):
    food[i] = food[i].replace("@", "")


# In[33]:


item = None
price1 = None


# In[37]:


for i in range(len(price)):
    print('item: '+ food[i])
    print('price:'+ price[i])
    print("\n")


# In[ ]:





# In[ ]:




