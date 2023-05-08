import os
import pandas as pd
import numpy as np
import jieba
import jieba.posseg as pseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
from PIL import Image

# 定义函数来读取评论文件并返回一个字符串
def read_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
        return ''.join(content)

# 定义函数来分析评论文本，并返回一个数据框
def analyze_comments(file_path):
    # 读取评论文件
    comments = read_comments(file_path)

    # 分词并去除停用词
    stopwords = set(pd.read_csv('stopwords.txt', header=None, names=['stopword']))
    stopwords.add('一直')
    stopwords.add('不错')
    stopwords.add('非常')
    stopwords.add('这个')
    stopwords.add('喜欢')
    stopwords.add('啤酒')
    stopwords.add('东西')
    stopwords.add('可以')
    stopwords.add('斑马')
    words = [(w.word, w.flag) for w in pseg.cut(comments) if w.word not in stopwords and len(w.word)>1]

    # 按照词性分类统计词频
    word_counts = {}
    for w in words:
        if w[1] not in word_counts:
            word_counts[w[1]] = {}
        if w[0] not in word_counts[w[1]]:
            word_counts[w[1]][w[0]] = 1
        else:
            word_counts[w[1]][w[0]] += 1

    # 对每个词性的词频进行排序并放入数据框
    dfs = []
    for pos in word_counts:
        df = pd.DataFrame({
            'word': list(word_counts[pos].keys()),
            'count': list(word_counts[pos].values())
        })
        df = df.sort_values(by='count', ascending=False)
        df['pos'] = pos
        dfs.append(df)
    result = pd.concat(dfs)

    return result

# 读取评论文件夹下的所有评论文件
comments_dir = './comments/'
comments_files = os.listdir(comments_dir)

# 分析每个评论文件，并将结果合并为一个数据框
comments_df = pd.concat([analyze_comments(comments_dir + f) for f in comments_files])

# 绘制不同词性的词云
pos_word_counts = {}
for pos in comments_df['pos'].unique():
    words = comments_df[comments_df['pos']==pos]['word']
    word_counts = dict(zip(words, comments_df[comments_df['pos']==pos]['count']))
    pos_word_counts[pos] = word_counts
wc_mask = np.array(Image.open("bw.jpg"))

for pos in pos_word_counts:
    wordcloud = WordCloud(font_path='msyh.ttc', background_color='white', max_words=1000, mask=wc_mask).generate_from_frequencies(pos_word_counts[pos])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(pos, fontsize=16)
    plt.savefig('./词性分析/' + pos + '.jpg', dpi=350)
    plt.show()

# 绘制条形图，展示各个词性下前10个高频词
fig, axs = plt.subplots(len(pos_word_counts), 1, figsize=(8, 6*len(pos_word_counts)))

for i, pos in enumerate(pos_word_counts):
    top_words = sorted(pos_word_counts[pos].items(), key=lambda x: x[1], reverse=True)[:10]
    words, counts = zip(*top_words)
    ax = axs[i]
    ax.bar(words, counts)
    ax.set_title(pos, fontsize=16)
    ax.tick_params(axis='x', labelrotation=90)

plt.tight_layout()
plt.savefig('word_counts.jpg', dpi=450)
plt.show()
