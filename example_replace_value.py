#library
from lgpdXml import *

#text
xml = '''<name>john</name><uf>rn</uf><city>natal</city><age>31</age>'''

#call class
text = lgpdXml(xml)

#replace using tag
newText = text.replace('<city>','natal','</city>','parnamirim')

#result
print(newText)
