#str ,bytes Unicode编码的两种数据类型encode()，decode() 编码/解码

#chardet 检测编码,支持检测中文，日文，韩文多种语言
import chardet
#encoding,confidenece:检测正确率,language
print(chardet.detect(b'i need a job'))
data = '忽如一夜春风来，千树万树梨花开'.encode('gbk')
print(chardet.detect(data))
data = '忽如一夜春风来，千树万树梨花开'.encode('utf-8')
print(chardet.detect(data))
data =  '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
