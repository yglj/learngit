# 文件是某种存储在长期存储设备的一段数据
#  文本文件，二进制文件（提供给其他软件使用），视频，图片音频等

# 打开文件  open
# 把文件读入内存，把内存数据写入文件  read/writer
# 关闭文件 close

# read方法会一次性读入并返回所有文件内容
# 方法执行后会把文件指针移动到文件末尾
import os


def demo():
    print(os.path.abspath('../../ip.txt'))
    file = open('../../ip.txt')
    text = file.read()
    print(text)
    print(len(text))

    # 文件指针，标记读取数据的开始位置，执行read（）方法后，会把指针放在读取内容末尾
    file.seek(0)  # 重置读取位置
    text = file.read()  # 再次读取文件
    print(len(text))

    file.close()

# 打开文件方式，默认只读方式  r(只读) w(只写) a(追加)  读写方式：r+,w+,a+  b： 二进制文件

# readline() 行读 ，执行后文件指针移动下一行


def demo2():
    file1 = open('../../ip.txt', 'r')
    file2 = open('./ip.txt', 'w')

    while True:
        text = file1.readline()
        if not text:
            break
        file2.write(text)

    file1.close()
    file2.close()


# 文件目录常用操作
# os: rename,remove,listdir,mkdir,rmdir,getcwd,chdir,path.isdir

gl_dir_num = 0


def tree(path, depth=0):
    depth += 1
    global gl_dir_num
    dir_name = path
    if os.listdir(path):
        gl_dir_num += 1
        for file in os.listdir(dir_name):
            print(' `  ' * depth + '|')
            print('  ' * depth + '——' * depth, file)
            dir_name = os.path.join(path, file)
            if os.path.isdir(dir_name):
                tree(dir_name, depth)


# 给一个路径，是不是空
# 打印所有文件名
# 判断有没有子目录
def move(old, new):
    """
    移动文件
    :return: None
    """
    if os.listdir(old):
        for name in os.listdir(old):
            old_site = os.path.join(old, name)
            new_site = os.path.join(new, name)
            if os.path.exists(new_site):
                print(name)
                new_site = new_site.replace(name, name + '.py')
            os.rename(old_site, new_site)


if __name__ == '__main__':

    # demo2()
    print(os.getcwd())
    # os.mkdir('/home/yl/Desktop/day/base')
    # tree('/home/yl/Desktop/day')
    print(gl_dir_num)

    old_path = '/home/yl/Desktop/day/d4'
    new_path = '/home/yl/Desktop/day/base'
    # os.rename(old_path, new_path)
    # move(old_path, new_path)
    # print(os.path.exists('/home/yl/Desktop/day/d1/1.txt'))





