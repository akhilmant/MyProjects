#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imaplib


# In[2]:


M=imaplib.IMAP4_SSL("imap.gmail.com")


# In[3]:


import getpass


# In[4]:


email=getpass.getpass("email : ")
password=getpass.getpass("passwrpd: ")


# In[5]:


M.login(email,password)


# In[6]:


M.list()


# In[7]:


M.select("INBOX")


# In[8]:


typ,data=M.search(None,'SUBJECT "This is a python test"')


# In[9]:


typ


# In[10]:


data


# In[11]:


email_id=data[0]


# In[ ]:


result,email_id=M.fetch(email_id,"(RFC882)")


# In[ ]:


raw_email=

