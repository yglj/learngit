##DOM vs SAX
##DOM把整个XML读入内存，解析为树，占用内存大，解析慢，优点是可以遍历树的任意节点
##SAX是流模式，边读边解析，占用内存小，解析快，缺点是需要处理事件
##正常情况下，优先考虑SAX，因为DOM实在太占内存。
##start_elemnt
##end_element
##char_data
with open(r'C:\Users\Administrator\Desktop\notebook\spingmvc.xml','r',encoding='utf-8') as f:
     sping = f.read()

     
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
     def start_element(self,name,attrs):
          print('标签头:%s,属性:%s'%(name,attrs))

     def end_element(self,name):
          print('标签尾:%s '%(name))

     def char_data(self,text):
          print(text.lstrip())
          print('文本:%s'%(text.strip()))


xml = r'''<xml version="1.01">
               <ul>
                    <li><a href="python">python</a></li>
                    <li><a herf="ruby">ruby</a></li>
               </ul>
          </xml>

     '''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(sping)

#最简单也是最有效的生成XML的方法是拼接字符串
##L = []
##L.append(r'<?xml version="1.0"?>')
##L.append(r'<root>')
##L.append(encode('some & data'))
##L.append(r'</root>')
##print(''.join(L))

