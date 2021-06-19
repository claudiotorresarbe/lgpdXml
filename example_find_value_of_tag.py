#library
from lgpdXml import *

#text
xml = '''<name>john</name><uf>rn</uf><city>natal</city><age>31</age>'''

#call class
text = lgpdXml(xml)

#find using tag
searchVal = text.find('<uf>','</uf>')

#result
print(searchVal)
