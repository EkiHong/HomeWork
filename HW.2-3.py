
# coding: utf-8

# In[3]:


「太鼓達人」是一款音樂型遊戲，玩者需要配合畫面上出現不同種類的音符，以正確的節拍敲打太鼓來獲取分數。現在我們將這個遊戲簡化，請你來完成它的功能。音符只有兩種：

紅色音符(咚)：代表要敲打鼓面
藍色音符(喀)：代表要敲打鼓邊
遊戲中有2個數值：

得分：遊戲一開始這個數值是 0，只要在音符出現時敲打太鼓上正確的部位(鼓面或鼓邊)，即可獲得分數，增加的分數為 COMBO 數×100。
COMBO 數：代表連續正確命中音符的數量，遊戲一開始這個數值是 0，只要每次命中一個音符則 COMBO 數就會+1，但只要有一個失誤(打錯部位或沒打)，則 COMBO 數就會歸零。另外，請你記錄玩家出現過最高的 COMBO 數是多少。
另外請注意，如果畫面上沒有音符時，敲打太鼓的任何一個部位並不會影響任何數值，也就是沒有音符的時候做什麼都可以。


gameStr=str(input()) #RRRRBRRRRB   str(字串) 會將 輸入的 RRRRBRRRRB 解讀成'RRRRBRRRRB' 且每個字元都有它的位置 ex. 0="R" 1="R" 4="B"
knockStr=str(input())#RRRRRRRRRR
combo=0 #combo在此程式扮演一直被更改的腳色
combos=0 #combos則是最高combo數
scores=0

for i in range(len(gameStr)): #兩個input需要做 比對動作 須用迭代 range會將gameStr轉換成[0,1,2,3,4,5,6,7,8,9]#for迴圈的導出 必定要是 整數不能為 字串 不
    if gameStr[i]=="-": #如果輸入題目為 "-"不會有任何動作
        continue
    elif gameStr[i]==knockStr[i]: #[] 是能得知他們位置上的值 字串是可以用[]找出其位置之值 
        combo=combo+1
        scores=scores+combo*100
        if combos<combo: #這行是故意讓combo>combos 因為這樣if才能繼續往下走
            combos=combo ##combos 是為了儲存第9行的combo的值
    else: #如果 gameStr[i]!=knockStr[i]則走這行 combo重新計算 
        combo=0 #對應到第9行
print(scores,combos)

