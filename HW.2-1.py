
# coding: utf-8

# In[78]:


#給定一個由大小寫英文字母所組成的字串以及一個英文字母，請輸出字母在字串中出現的間隔距離。

sentence=input() #ABCDAAEFeDaBDCBCBcBCbCBBdad
eng=input() #d 
sentence_long=len(sentence) #long=25 #因為要用位置來去解題
sentence_char=sentence.lower() #abcdaaefed...
eng_num=eng.lower() #d

location=[] #[3,9,12,24,26] #先找出字母所在位置
for i in range(sentence_long): #i=[0,1,2,3,4,...,24]
    if eng_num==sentence_char[i]:  #
        location.append(i)
        #print(location)

result=[]
for j in range(len(location)):  #j=0,1,2,3,4  用J的原因是因為 要想辦法讓 j=0,1,2,3,4 去跟 [3,9,12,24,26] 做位置上的對應
    if j<(len(location)-1): #因為現在是要算間隔 間隔只有4格 所以要 (5-1) 更重要的是放if條件原因是因為如果i=4放進去的話會超出範圍
        location[j+1]-location[j] #因為要算間隔所以前面擷取部分要+1 ex. [2+1]-[2] = 24-12 = 12
        spacing = location[j+1]-location[j]
        #print(spacing)
        result.append(str(spacing))
print(" ".join(result))


