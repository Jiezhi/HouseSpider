# HouseSpider
---

> 也老大不小了，该买套房子安定下来了。没什么钱，也就有点破技术了，所以就抓了一些数据到本地来分析，看看到底适合买在哪里。

说实话没几行代码，没啥技术含量，爬取的时候比较粗鲁，更细的信息提取放在了本地来做了。

运行说明：  
> 爬取"房天下"的数据到文件"ftx0227.csv"，这里采用.csv主要是方便自己导入**jupyter notebook**里分析。

```bash
scrapy runspider ftx.py -o ftx.csv
```
> 下面这个是爬取链家的数据
```bash
scrapy runspider lianjia.py -o lianjia.csv
```

