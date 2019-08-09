# encoding:utf-8
import json
import jieba

'''
 文件中每一行为一个dict，key有三个：['question_id'],['question'],['doc_tokens']. 
question_id为问题的编号。 
question 为当前的问题。 
doc_tokens 为 分词过后的文本。
 例如：{"question": "浦发银行电话", "question_id": 181554, "doc_tokens": ["浦发银行", "的", "电话", "95528"]}
'''

# 构造字典
# python2json = {}
# # 构造list
# listData = [1, 2, 3]
# python2json["listData"] = listData
# python2json["strData"] = "test python obj 2 json"
#
# # 转换成json字符串
# json_str = json.dumps(python2json)
# print(json_str)


#
# seg_list = jieba.cut("我来到北京清华大学")
# with open('.\\tmp.json', 'w') as f:
#     json.dump(python2json, f)
#     f.write('\n')
#
#     json.dump(python2json, f)
#     f.write('\n')
#
#     json.dump(python2json, f)
#     f.write('\n')
# # !/usr/bin/python
#
#
# import json


def writeDict(data):
    with open(".\\tmp.json", "w", encoding='utf8') as f:
        jsondata = json.dumps(data, ensure_ascii=False, indent=4)
        print(jsondata)
        f.write(jsondata)


if __name__ == '__main__':
    dict_1 = {"北京": "BJP", "北京北": "VAP", "北京南": "VNP", "北京东": "BOP", "北京西": "BXP"}

    writeDict(dict_1)
# jieba.cut的默认参数只有三个,jieba源码如下
# cut(self, sentence, cut_all=False, HMM=True)
# 分别为:输入文本 是否为全模式分词 与是否开启HMM进行中文分词
