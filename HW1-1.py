
# coding: utf-8

# In[1]:


#有一家店正在進行促銷，只要客人買10個餅乾就多送1盒巧克力，(無論是自己買或送的)累積滿5盒巧克力就送1塊小蛋糕。
#請以程式輸出最後店家應給予的物品數量。


cookies=int(input())
chocos=int(input())
cakes=int(input())

chocos=chocos+(cookies//10)
cakes =cakes+(chocos//5)

print("Cookies\tChocos\tCakes")
print("{0}\t{1}\t{2}".format(cookies, chocos, cakes))    

