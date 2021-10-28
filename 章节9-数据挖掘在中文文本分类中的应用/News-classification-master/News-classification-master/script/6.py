#coding: utf-8
import os
import time
import random
import jieba
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn import tree, metrics
from sklearn import feature_extraction, model_selection
# 导入文本特征向量转化模块
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import feature_selection
from sklearn.datasets import fetch_20newsgroups
def TextProcessing(folder_path, test_size=0.2):
    folder_list = os.listdir(folder_path)
    class_list = []
    data_list = [] #存储分完词，去除停用词等清洗工作之后的每一个文本
    # 类间循环
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder)
        files = os.listdir(new_folder_path)
        # 类内循环
        j = 0
        for file in files:
            raw=" "
            with open(os.path.join(new_folder_path, file), 'r', encoding='UTF-8') as fp:
                for line in fp.readlines():  # 依次读取每行
                    line = line.strip()  # 去掉每行头尾空白
                    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                        continue  # 是的话，跳过不处理
                    raw += line+" "  # 保存
                    #print(raw)
            data_list.append(raw)
            class_list.append(folder)#文本类别标签

    ## 划分训练集和测试集
    train_data_list, test_data_list, train_class_list, test_class_list =model_selection.train_test_split(data_list, class_list, test_size=0.2, random_state=1)
    #print(train_data_list)
    return train_data_list, test_data_list, train_class_list, test_class_list
#文本特征选择与向量化，不同的特征词选择方法，不同的特征词数目
def TextFeature(train_data_list, test_data_list, train_class_list, test_class_list, fs_method, fs_num):
    term_set_fs1 = feature_selection.feature_selection(train_data_list, train_class_list, fs_method)
    term_set_fs = feature_selection.feature_selection(train_data_list, train_class_list, fs_method)[:fs_num]
    print('Feature selection...')
    print('fs method:' + fs_method, 'fs num:' + str(fs_num))
    term_dict = dict(zip(term_set_fs, range(len(term_set_fs))))
    print(len(term_set_fs1))
    print(term_set_fs1)
    # 分别对训练数据集和测试集进行文本向量化（以归一化的tf-idf计算词语的权重）
    '''vectorizer = CountVectorizer()
    # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer.fixed_vocabulary = True
    vectorizer.vocabulary_ = term_dict
    transformer = TfidfTransformer()
    # 该类会统计每个词语的tf-idf权值
    tfidf_train = transformer.fit_transform(vectorizer.fit_transform(train_data_list))
    # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    tfidf_test = transformer.fit_transform(vectorizer.fit_transform(test_data_list))
    # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    weight_train = tfidf_train.toarray()
    weight_test = tfidf_test.toarray()
    print(weight_train)
    '''
    '''for i in range(len(weight_train)):
    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word)):
        print(word[j],weight_train[i][j])
    '''
    tv = TfidfVectorizer(sublinear_tf=True, max_df=0.5, vocabulary=term_dict)
    #tv = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
    tfidf_train = tv.fit_transform(train_data_list)
    #tv2 = TfidfVectorizer(vocabulary=term_dict)
    tv2 = TfidfVectorizer(vocabulary=tv.vocabulary_)
    tfidf_test = tv2.fit_transform(test_data_list)
    word= tv.get_feature_names()
    ## word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    # print(word)
    weight_train = tfidf_train.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    weight_test = tfidf_test.toarray()

    return weight_train, weight_test, train_class_list, test_class_list
# 利用朴素贝叶斯分类算法来构建文本分类模型,并计算分类准确率
def TextClassifyModelBuilding(weight_train, weight_test, train_class_list, test_class_list):
    # 创建模型
    mnb = MultinomialNB(alpha=0.01)
    # 对训练数据集进行模型训练生成文本分类器
    classifier = mnb.fit(weight_train, train_class_list)
    # 使用构建的分类器对测试数据集进行文本类别预测，并输出显示分类准确率，召回率等各项指标
    predict_class_list = classifier.predict(weight_test)
    acc = np.mean(predict_class_list == test_class_list)
    #test_accuracy = classifier.score(weight_test, test_class_list)


    #print('输出显示准确率：')
    #print(test_accuracy)
    '''
    print(predict_class_list)
    print("准确率:", classifier.score(weight_test, test_class_list))
    print("其他指标：\n", classification_report(test_class_list, predict_class_list))
    print("finished")
    
    '''
    return acc
if __name__ == '__main__':
    print("start")
    ## 1.1数据读取
    ## 1.2文本预处理（分词，停用词去除，数字等不规则符号去除等）,按比例将整个数据集划分测试集与训练集
    folder_path = '../data/train_data'
    train_data_list, test_data_list, train_class_list, test_class_list=TextProcessing(folder_path, test_size=0.2)
    print("jieguo:")
    #print(train_data_list)
    '''
    # 1 下载新闻数据
    news = fetch_20newsgroups(subset="all")

    # 2 分割训练数据和测试数据
    train_data_list, test_data_list, train_class_list, test_class_list = model_selection.train_test_split(news.data,
                                                        news.target,
                                                        test_size=0.2,
                                                        random_state=1)
   '''
    ## 2.1文本特征词选择
    fs_method_list = ['IG', 'MI']
    #fs_method_list = ['IG']
    fs_num_list = range(10000, 88000, 10000)
    acc_dict = {}
    ## 2.2文本向量化
    for fs_method in fs_method_list:
        acc_list = []
        for fs_num in fs_num_list:
            weight_train, weight_test, train_class_list, test_class_list = TextFeature(train_data_list, test_data_list, train_class_list, test_class_list, fs_method, fs_num)
            acc= TextClassifyModelBuilding(weight_train, weight_test, train_class_list, test_class_list)
            acc_list.append(acc)
        acc_dict[fs_method] = acc_list
        print('fs method:', acc_dict[fs_method])

    for fs_method in fs_method_list:
        plt.plot(fs_num_list, acc_dict[fs_method], '--^', label=fs_method)
        plt.title('feature  selection')
        plt.xlabel('fs num')
        plt.ylabel('accuracy')
        plt.ylim((0.4, 0.8))

    plt.legend(loc='upper left', numpoints=1)
    plt.show()






