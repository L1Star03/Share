# 京东爬虫
[TOC]
# 一. 功能：
功能：本代码简单爬取了京东商品的所有评论，并对评论进行TF-IDF词频分析，绘制不同词性的词云和统计条形图饼图，以及对评论进行情感分析，找到好评并绘制出好评词云词频
# 二. 使用方法：
1. 依赖环境
```
python<=3.12
pip install selenium
pip install PIL
pip install WordCloud
pip install ntlk
pip install matplotlib
需要对应edge浏览器版本的edgedriver并覆盖目录下的msedriver.exe文件
```
2. 将需要爬取的所有链接放在根目录下的/urls文件夹中的urls.xlsx文件中按列排好（不需要名称等，只需要放链接）如图：
![urls.xlsx文件示意图](https://img-blog.csdnimg.cn/d361eb7215f14827a3758e3fc41f7012.png)
3. 将EdgeDriver放在爬取商品评论.py中相应的位置（我指定的是根目录下），在根目录下新建几个文件夹“comments”，“cost”用于储存返回的结果（也可以修改代码，使用mkdir和判断语句来判断当前是否存在上述文件夹并按情况新建。目录如下
![根目录](https://img-blog.csdnimg.cn/1e1b2811a92547f8ab8e637a1368edce.png)
4. 运行爬取商品评论.py，等待爬虫结束就可以在上述新建的文件夹中comments的对应商品名称里找到当前商品的所有评论。运行后comments和cost中的txt文件如下：
![comments文件夹截图](https://img-blog.csdnimg.cn/c63cf099d91c48418667d454e64b5770.png)
![cost文件夹截图](https://img-blog.csdnimg.cn/1cb65e55a45a42a8bf4784e2123a8a32.png)

5. 在根目录下新建文件夹”词性分析“，新建一个停用词表”stopwords.txt“，其中内容按照自己的需要修改，按行间隔两个词，运行词性分析.py，得到的运行结果是所有词性词语的词云，以及一张整合了所有词性的词频图，如下图所示
![词性分析文件夹截图](https://img-blog.csdnimg.cn/49b7b33ee63c41bd902d0c0bf6a1cdc9.png)
![整合图](https://img-blog.csdnimg.cn/696f8da0b51144cbb517f16b1f01a47b.png)

6. 新建文件夹”好评分析“，运行情感分析.py，得到最后的情感分析结果，最后整个根目录结构如下![根目录截图](https://img-blog.csdnimg.cn/24bca088eef34da28300f442dd29499e.png)
情感分析结果示例如下（以某品牌啤酒为例）![请添加图片描述](https://img-blog.csdnimg.cn/3bd35567ec0a4fa6bcb3dc4ff6eb8371.jpeg)
# 三.仓库位置
[GitHub京东爬虫，求求各位给个⭐！！！](https://github.com/L1Star03/Share/tree/main/%E4%BA%AC%E4%B8%9C%E7%88%AC%E8%99%AB)
