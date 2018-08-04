
# coding: utf-8

# In[2]:


#如果一個字串，從前面唸過去，跟從後面唸回來是一樣的。
#例如阿巴合唱團 ABBA 就符合這個條件，這樣的文字我們稱它為「迴文」。現在給你一個字串，請你判斷它是不是一個迴文。

rowStr=input()                 #先放一個ABBA
rowLst=[]                      #這是YES NO 的存放區
while rowStr!="-----":         #當rowLst != "-----" 繼續走下去迴圈
    if rowStr==rowStr[::-1]:   # 如果ABBA 反寫過來 還是等於 ABBA的話
        rowLst.append("YES")   #將 "YES" 加入 rowLst
    else:                      #如果不是
        rowLst.append("NO")    #將 "NO" 加入 rowLst
    rowStr=input()             # 要不限次數的輸入 input 則要將 input 放入 while 迴圈內 直到 rowStr 的輸入 等於 "-----"才跳出迴圈
while rowStr == "-----":       #當輸入等於"-----" 則停止運作
    break
for i in rowLst:               #將剛剛所有的 YES NO 丟進 i 這個變數
    print(i)                   #將其印出

