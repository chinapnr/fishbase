from numpy import *
import jieba

from fish_base import get_long_filename_with_sub_dir_module


class ClassNaiveBayes:

    # 训练 list, 默认内容, 原书中的内容
    train_doc_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                      ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                      ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                      ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                      ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                      ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 倾向性向量, 0:正面 1:负面
    train_doc_sent_vec = [0, 1, 0, 1, 0, 1]

    # 单词列表集合
    word_list = []

    # 正面和负面概率, 先验概率
    p0_v = 0
    p1_v = 0
    p_ab = 0

    stopwords_list = []

    # 2016.5.18
    # 读入停用词
    def read_stopwords(self):

        self.stopwords_list = []

        # 获得停用词文件的本地文件
        filename = get_long_filename_with_sub_dir_module('bayes', 'stopwords.txt')[1]

        with open(filename, 'r') as f:
            for line in f:
                self.stopwords_list.append(line.rstrip())

        print(self.stopwords_list)

    # 2016.5.19
    def word_optimize(self, l):
        # 停用词过滤
        temp_word_list = [x for x in l if x not in self.stopwords_list]
        return temp_word_list

    # 2016.5.16 5.19
    # 创建单词集合
    # 输入 data_list: 数据列表内容, 两维list
    # 输出 单维list
    def create_word_list(self, data_list):
        # create empty set
        word_set = set([])
        for document in data_list:
            # union of the two sets
            word_set = word_set | set(document)
        word_list = list(word_set)
        # 词汇处理
        word_list = self.word_optimize(word_list)
        # print('word list count:', len(word_list))
        return word_list

    # 2016.5.16
    # 将单词 list 转换为向量
    # 输入 word_list: 单词列表 new_word_list: 需要向量化的单词列表
    # 输出 vec: 生成的向量数组
    @staticmethod
    def words_to_vec(word_list, new_word_list):
        vec = [0] * len(word_list)
        for word in new_word_list:
            if word in word_list:
                vec[word_list.index(word)] += 1
            else:
                pass
                # print("the word: %s is not in my Vocabulary!" % word)
        return vec

    # 2016.5.16
    # 进行 naive bayes 训练
    # 输入 train_matrix: 训练举证 train_category: 正反向量列表
    # 输出 p0_v, p1_v:正面反面概率, p_ab:先验概率
    @staticmethod
    def train_nb0(train_matrix, train_category):

        num_train_docs = len(train_matrix)
        num_words = len(train_matrix[0])
        p_ab = sum(train_category) / float(num_train_docs)

        # 创建给定长度的填满1的数组
        p0_num = ones(num_words)
        p1_num = ones(num_words)

        p0_d = 2.0
        p1_d = 2.0
        for i in range(num_train_docs):
            if train_category[i] == 1:
                p1_num += train_matrix[i]
                p1_d += sum(train_matrix[i])
            else:
                p0_num += train_matrix[i]
                p0_d += sum(train_matrix[i])

        p1_v = log(p1_num / p1_d)
        p0_v = log(p0_num / p0_d)
        return p0_v, p1_v, p_ab

    # 2016.5.16
    # 分类
    # 输入 向量, 正面反面概率,事件概率
    # 输出 正面或者反面
    @staticmethod
    def classify_nb(vec, p0_vec, p1_vec, p_class1):
        # element-wise mult
        p0 = sum(vec * p0_vec) + log(1.0 - p_class1)
        p1 = sum(vec * p1_vec) + log(p_class1)
        print('p0:', p0, 'p1:', p1)
        if p1 > p0:
            return 1
        else:
            return 0

    # 2016.5.16
    # 训练, 生成需要的向量参数等
    def train(self):
        # 生成单词列表集合
        self.word_list = self.create_word_list(self.train_doc_list)

        # 训练矩阵初始化
        train_matrix = []

        # 根据训练文档进行循环
        for post_in_doc in self.train_doc_list:
            # 构建训练矩阵, 将单词列表转化为向量
            train_matrix.append(self.words_to_vec(self.word_list, post_in_doc))

        # 根据训练矩阵和情感分析向量进行训练,得到
        self.p0_v, self.p1_v, self.p_ab = self.train_nb0(array(train_matrix), array(self.train_doc_sent_vec))

    # 2016.5.16
    # 根据输入内容测试 Naive Bayes 模型
    # 输入 test_word_list: 需要测试的单词 list
    # 输出 0 or 1, 表示正面或者反面
    def run_nb(self, word_list):

        # 对输入的内容转化为向量
        this_post_vec = array(self.words_to_vec(self.word_list, word_list))

        # 返回分类的值
        return self.classify_nb(this_post_vec, self.p0_v, self.p1_v, self.p_ab)

    # 2016.5.18
    @staticmethod
    def init_cut_word():
        jieba.initialize()

    # 2016.5.18
    # 打开训练文档, 将内容增加到内部变量
    def open_train_doc_ch(self, filename, class_mark):

        train_txt0 = []
        with open(filename, 'r') as f:
            for line in f:
                train_txt0.append(line.rstrip())

        for item in train_txt0:
            s = list(jieba.cut(item))
            self.train_doc_list.append(s)
            self.train_doc_sent_vec.append(class_mark)

    # 2016.5.18
    # 根据测试样本来测试分类的准确率
    # 输出 人工正确/机器判断正确 人工错误/机器判断错误 的两个百分比
    def test_nb(self, filename):

        test_doc_list = []
        pre_class_list = []

        # 设定测试结果 dict
        test_result_dict = {'11': 0, '10': 0, '00': 0, '01': 0}

        # 打开测试文本
        with open(filename, 'r') as f:
            for line in f:
                # 获得人工设定的类别
                pre_class_list.append(line[0:1])
                # 获得需要测试的文本
                test_doc_list.append(line[2:].rstrip())

        # 测试文本的长度
        test_doc_count = len(test_doc_list)

        for i, item in enumerate(test_doc_list):

            s = list(jieba.cut(item))

            # 对输入单词进行优化处理
            s = self.word_optimize(s)

            # 获得程序分类结果
            computer_class = self.run_nb(s)
            # 获得人工设定的分类结果
            pre_class = pre_class_list[i]

            # 结果记录到测试结果 dict 中
            index = '**'

            if pre_class == '1':
                index = str(10 + computer_class)
            if pre_class == '0':
                index = '0' + str(computer_class)

            test_result_dict[index] += 1

            print(s, pre_class, computer_class)

        print(test_result_dict)

        # 返回结果, 假设测试文本中正面和负面各占一半
        return test_result_dict['00'] / (test_doc_count / 2), test_result_dict['11'] / (test_doc_count / 2)
