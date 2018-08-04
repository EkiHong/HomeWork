
# coding: utf-8

# In[7]:


#某一堂Python程式設計課要同學分組做期末報告，分組的方式為依座號順序，每 N 個人一組，每一組中座號最大的人就是組長。如 N=3 時：1, 2, 3 為第一組，4, 5, 6 為第二組….
#以此類推，而座號3就是第一組組長。請完成一個程式，在輸入同學的座號後，判斷他是哪一組，並得知他是否為組長。

n=int(input())
m=int(input())

if m%n==0:
    print("leader of team", m//n )
else:
    print("member of team", m//n+1 ) 

