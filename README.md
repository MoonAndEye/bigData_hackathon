-----20160729-----

前處理的檔案已經寫完了,接下來就是處理

現在初步分成  a > 週末 b >週間


-----20160720 要開始上主菜了-----

如果沒有主菜，只會抓資料是拿不到好薪水的。

因為抓資料並不是會讓你拿到高薪的原因，而是分析出來的資料才是。

分出平日和周末和連假的日期

找出新北市的停車場使用模式

分析資料

(因為資料會不斷新增，所以應該要分出來兩份，一份是一直追加的，另一份是單獨計算某段時間內的資料)

1 > 日 > 先分兩群 a> 禮拜一到禮拜五 b> 禮拜六、日

2 > 時間 > 先分四群 a> 00~06 b> 06~12 c>12~18 d> 18~24

3 > 找出周末嚴重擁擠的停車場 > 在 b c d 這三個時段，有80%的時間是0剩餘的

4 > 找出周末擁擠的停場場 > 在 b c d 這三個時段，有80%的時間停車負載達到80%

5 > 找出周末低利用的停車場 > 在 b c d 這三個時段，有低於50%的負載。

====== 以後有空 再去做通勤時間 =====

可是我要怎麼用地圖?

A> 硬幹吧,在google上自己標地圖,再自己截圖下來

B> 試試看找 google API,讓google的地圖可以直接呈現上面的點。

但這一部分,是不是只能用py2?

C> 資料上有座標，他是 TWD97, 所以如果要用google的地圖,這東西可能要轉換,因為google的格式可能不是 TWD97.

===== 和 Machine Learning 有相關 =====

不斷的餵資料，讓 ML 可以學到，哪一天，哪個時間，停車場會有空位

讓 ML 學著去預則下個周末的哪些時間，可以停哪裡。

然後驗證這個預測是不是對的。

接下來，這個東西，就可以變成一個產品了。

拿去報告

----- Past ----- 稍微加一些想法，在之前拿出去的東西 1 加一個 index，可停車空位 / 最大 
停車位。當這個數字愈接近0，顏色愈靠近紅色。不過在實際表現的時候，會有一個很奇怪的點， 
停車場滿載的時候是0。這個時候最靠近紅色，但因為「可停車」數字是0，所以在半徑上就會變 
成0，一個點，可能會無法表現。

2 其他數據算出，新北市單位面積佔有車子的數量。再將停車場最大容量 / 這個數字，把這個數 
字當成半徑。這樣每個停車場就會有自己的半徑，那這樣第1點的可停車數==0，就不會有看不見 
的問題。

3 查詢者欲前往的地點，以走路10分鐘到20分鐘的距離為半徑，半徑內的停車場應該一起進行計 
算。

4停車場之間應該有交互作用，一樣以10分鐘到20分鐘的距離當標準，來看有沒有關聯。
