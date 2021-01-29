#encoding=utf-8
#>>>>>python解析xml>>>>>>>>使用elementtree>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import xml.etree.ElementTree as ET

tree=ET.parse('example.xml')
root=tree.getroot()
print(f"这是一个早餐菜单\n{root.attrib['year']}")
for child in root:
    print("name:",child[0].text)
    print("price:",child[1].text)
    print("description:",child[2].text)
    print("carlies:",child[3].text)

# 系统信息监控


