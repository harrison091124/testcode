import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)  # Get方式获取网页数据
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    from_data = {'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
                 'salt': '16158647818957', 'sign': '0d5676534837c68da8add3d1b47ec24b', 'lts': '1615864781895',
                 'bv': '818e2470a16ccb5d68270d01f2d298b2', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
                 'action': 'FY_BY_REALTIME'}


    # 请求表单数据
    response = requests.post(url, data=from_data)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    # 打印翻译后的数据
    # print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    get_translate_date('我爱中国')
