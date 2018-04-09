from lxml import etree

with open('./html', 'r', encoding='UTF-8') as f:
    html = f.read()
# print(html)
selector = etree.HTML(html)
print(selector.xpath('//div[@id="login"]/form/input[2]/@value'))