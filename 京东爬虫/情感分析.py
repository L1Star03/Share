import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
plt.rcParams['font.sans-serif'] = ['SimHei']

# 下载必要的 NLTK 数据
nltk.download('vader_lexicon')

# 初始化情感分析器
sia = SentimentIntensityAnalyzer()

# 定义情感分类函数


def classify_sentiment(text):
    scores = sia.polarity_scores(text)
    return '好评' if scores['compound'] > 0 else '差评'

# 定义一个用于统计词频的函数


def count_words(text):
    words = nltk.tokenize.word_tokenize(text)
    freq_dist = nltk.FreqDist(words)
    return freq_dist


# 读取评论文件夹下的所有评论文件，并进行情感分类和词频统计
path = 'comments/'
good_reviews = ''
bad_reviews = ''
for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
        text = f.read()
        sentiment = classify_sentiment(text)
        freq_dist = count_words(text)
        if sentiment == '好评':
            good_reviews += text
        else:
            bad_reviews += text

# 对好评和差评的评论分别生成词云和词频统计
wc_mask = np.array(Image.open("bw.jpg"))
# 生成好评词云
good_wordcloud = WordCloud(mask=wc_mask, font_path='msyh.ttc', width=800, height=800,
                           background_color='white').generate(good_reviews)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(good_wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('good.jpg', dpi=350)

# 生成好评词频统计
good_freq_dist = count_words(good_reviews)
print("好评词频统计：")
print(good_freq_dist.most_common(10))

# 生成差评词云
bad_wordcloud = WordCloud(font_path='msyh.ttc', width=800, height=800,
                          background_color='white').generate(bad_reviews)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(bad_wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

# 生成差评词频统计
bad_freq_dist = count_words(bad_reviews)
print("差评词频统计：")
print(bad_freq_dist.most_common(10))
