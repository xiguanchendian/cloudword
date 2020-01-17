from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


with open("F:\Pycharm\cloudword\word.txt") as fp:
    text = fp.read()
    text = trans_CN(text)
    # print(text)
    mask = np.array(image.open("C:\\Users\\Administrator\\Desktop\\python.png"))
    wordcloud = WordCloud(
        mask=mask
        # ,
        # font_path = "C:\\Windows\\Fonts\\msyh.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
