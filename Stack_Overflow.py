#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:/Users/SOHIT/Desktop/ODA/Project/Stack overflow/survey_results_public.csv")


# In[4]:


data.head()


# In[5]:


data.dropna()


# In[6]:


data[data['Employment'].isnull()]


# # Employment 

# In[7]:


#Which of the following best describes your current employment status?
data['Employment']


# In[8]:


Emp_status=data.groupby('Employment')['Respondent'].count()
(Emp_status).fillna(0,inplace=True)
print(Emp_status)


# In[9]:


data.Employment.dropna()


# In[10]:


a1 = Emp_status.plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a1.set_xlabel("Respondant", labelpad=20, weight='bold', size=12)
a1.set_ylabel("Employment status", labelpad=20, weight='bold', size=12)
a1.plot()


# # Employment Status by Geography

# In[11]:


#Employment Status by Geography
sort_by_country=data.groupby(['Country','Employment'],as_index=False)['Respondent'].count()
a8 = sort_by_country[sort_by_country["Country"]=="United States"].plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a8.set_yticklabels(sort_by_country['Employment'])
a8.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a8.set_ylabel("Employment", labelpad=20, weight='bold', size=12)
a8.plot()


# # Career Values

# In[12]:


#How Do Developers Feel About Their Careers and Jobs?

Job_career=data.groupby('JobSat')['Respondent'].count()
a2 = Job_career.plot(kind='barh', figsize=(10,6), color='#86bf91', zorder=2, width=0.2)
a2.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a2.set_ylabel("Job Status", labelpad=20, weight='bold', size=12)
a2.plot()


# # Remote Working

# In[13]:


#How Often Do Developers Work Remotely?

Remote_work=data.groupby('SOPartFreq')['Respondent'].count()
a4 = Remote_work.plot(kind='barh', figsize=(10,8), color='#86bf91', zorder=2, width=0.2)
a4.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a4.set_ylabel("Remote work", labelpad=20, weight='bold', size=12)
a4.plot()


# # Looking for a Job

# In[14]:


#Developer Job Search Status

Job_Search=data.groupby('JobSeek')['Respondent'].count()
a5 =Job_Search.plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a5.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a5.set_ylabel("Job Search Status", labelpad=20, weight='bold', size=12)
a5.plot()


# In[15]:


#Looking for job by Geography
sort_by_country=data.groupby(['Country','JobSeek'],as_index=False)['Respondent'].count()
a6 = sort_by_country[sort_by_country["Country"]=="United States"].plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a6.set_yticklabels(sort_by_country['JobSeek'])
a6.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a6.set_ylabel("Job Search Status", labelpad=20, weight='bold', size=12)
a6.plot()


# # Company Size

# In[60]:


#Company Size

size=data.groupby('OrgSize')['Respondent'].count()
a7 =size.plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a7.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a7.set_ylabel("Company Size", labelpad=20, weight='bold', size=12)
a7.plot()


# # Job Priorities

# In[52]:


#Most Important Job Factors

Job_factor=data.groupby('JobFactors',as_index=False)['Respondent'].count().sort_values('Respondent',ascending=False).head(10)
a3 = Job_factor.plot(kind='barh', figsize=(20,20), color='#86bf91', zorder=2, width=0.2)
a3.set_yticklabels(Job_factor['JobFactors'])
a3.set_xlabel("Respondent", labelpad=20, weight='bold', size=12)
a3.set_ylabel("Job Factor", labelpad=20, weight='bold', size=16)
a3.plot()


# In[46]:


data.JobFactors.unique()


# # Code Review

# In[48]:


#Hours Worked Per Week to review code
Work_hr=data.groupby('MainBranch',as_index=False)['WorkWeekHrs'].mean()
(Work_hr).fillna(0,inplace=True)


# In[49]:


Work_hr


# In[51]:


a9 = Work_hr.plot(kind='barh', figsize=(8,6), color='#86bf91', zorder=2, width=0.2)
a9.set_yticklabels(Work_hr['MainBranch'])
a9.set_xlabel("Work_Week_Hrs", labelpad=20, weight='bold', size=12)
a9.set_ylabel("Developer_Types", labelpad=20, weight='bold', size=12)
a9.plot()


# In[ ]:




