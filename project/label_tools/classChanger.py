import glob

'''
使用方法：
设置label.txt
将classChanger和label.txt放在labels文件夹同目录下（不是里），运行就可以
例子：

注意：
在修改前请保存一下原txt数据，后面可能因为labels顺序的变化需要重新赋值
'''

#根据label.txt生成枚举字典
labels = []
with open("label.txt", 'r') as f:
    for i in f.readlines():
        labels.append(i.replace('\n', ''))
labelsDictionary = {}
num = 0
for i in labels:
    labelsDictionary[i] = str(num)
    num += 1
for filename in glob.glob('labels/**/*.txt', recursive=True):
    for i in labels: #找到图片是哪个类
        if filename.find(i)!= -1: #确定类并开始换第一个字符
            numReplace = labelsDictionary[i]
            with open(filename, 'r') as f:
                original_lines = f.readlines()
            with open(filename, 'w') as out:
                for line in original_lines:
                    #判断class值是否有2位
                    if line[1]==" ":
                        newLine = numReplace+line[1:]
                    else:
                        newLine = numReplace + line[2:]
                    out.write(newLine)

