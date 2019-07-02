# HouseSpider
---

说实话没几行代码，没啥技术含量，爬取的时候比较粗鲁，更细的信息提取放在了本地来做了。

先用浏览器找到自己感兴趣的城市，然后复制链接到对应代码位置，如：

`start_urls = ['http://esf.nanjing.fang.com/house/h316/']`

运行说明：  
> 爬取"房天下"的数据
```bash
scrapy runspider ftx.py -o ftx.csv
```

> 下面这个是爬取链家的数据
```bash
scrapy runspider lianjia.py -o lianjia.csv
```

本地具体怎么提取信息和分析请参考：

[房天下信息提取](https://github.com/Jiezhi/HouseSpider/blob/master/ftx.ipynb)

[链家信息提取](https://github.com/Jiezhi/HouseSpider/blob/master/lianjia.ipynb)

