#!/usr/bin/env python
# coding: utf-8

# In[83]:


import os
import csv


# In[84]:


budget_data = os.path.join("Resources","budget_data.csv")


# In[85]:



with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    months = 0
    total = 0
    changes = []
    monthlist = []
    previous = 0
    for rowcount in csvreader:
        months = months + 1
        total = total + int(rowcount[1])
        if months == 1:
            previous = int(rowcount[1])
        else:
            monthlychange = int(rowcount[1]) - previous
            changes.append(monthlychange)
            monthlist.append(rowcount[0])
            previous = int(rowcount[1])
          


# In[ ]:





# In[ ]:





# In[86]:


avechange = (sum(changes))/(len(changes))


# In[87]:


MinChanges = min(changes)
MinMonth = monthlist[changes.index(min(changes))]


# In[88]:


MaxChanges = max(changes)
MaxMonth = monthlist[changes.index(max(changes))]


# In[89]:


with open('analysis/output.txt','w')as file:
    print('Financial Analysis')
    file.write(f'\nFinancial Analysis\n')
    print('----------------------------')
    file.write(f'----------------------------\n')
    print(f'Total Months: {months}')
    file.write(f'Total Months: {months}\n')
    print(f'Total: $ {total}')
    file.write(f'Total: $ {total}\n')
    print(f'Average  Change: ${avechange:.2f}')
    file.write(f'Average  Change: ${avechange:.2f}\n')
    print(f'Greatest Increase in Profits: {MaxMonth} {MaxChanges}')
    file.write(f'Greatest Increase in Profits: {MaxMonth} {MaxChanges}\n')
    print(f'Greatest Decrease in Profits: {MinMonth} {MinChanges}')
    file.write(f'Greatest Decrease in Profits: {MinMonth} {MinChanges}\n')


# In[ ]:





# In[ ]:





# In[ ]:




