import requests
from lxml import etree
from lxml.html import tostring
import json



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    "Referer": "http://www.ausomg.com/goods/search.htm",
    "Host":'www.ausomg.com'
}
def get_urls(url,data):
    goods_url_lists = []
    resp = requests.post(url, data=data, headers=headers)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    goods_lists = html.xpath("//ul[@class='goods_list clearfix']/li")
    for goodsTag in goods_lists:
        goods_url = goodsTag.xpath("./div[@class='img']/a/@href")[0]
        goods_url_lists.append(goods_url)

    return goods_url_lists


def get_goods_detail(url):
    print(url)
    resp = requests.get(url,headers=headers)
    html = etree.HTML(resp.text)
    goods_images = html.xpath("//div[@class='goods_img']/div[1]//ul//img/@src")
    goods_name = url.split("-",1)[1]
    goods_category = html.xpath("//div[@class='breadcrumb']/a[2]//text()")[0]
    goods_market_price = html.xpath("//div[@class='price']/div[@class='pris']/span[2]/text()")
    if goods_market_price:
        market_price = goods_market_price[0].split("$")[1].split(".")[0]
    else:
        market_price = "￥0"
    shop_price = html.xpath("//div[@class='itms']/span[2]/text()")[0].split(".")[0]
    goods_desc_str = html.xpath("//div[@class='text']")[0]
    goods_desc = tostring(goods_desc_str,method="html").decode("utf-8")
    goods_info = {
        'goods_url':url,
        'goods_name':goods_name,
        'goods_image':goods_images,
        'goods_category':goods_category,
        'market_price':market_price,
        'shop_price':shop_price,
        'goods_desc':goods_desc
    }
    # print(goods_info)
    return goods_info


def main():
    url = "http://www.ausomg.com/goods/search.htm?keyword="
    goods_url_lists = []
    for i in range(1,6):
        data = {
            'keyWords': "",
            "createOrder": 1,
            'pageNo': i
        }
        per_page_goods_url = get_urls(url, data)
        goods_url_lists += per_page_goods_url

    all_goods = []
    for goods_url in goods_url_lists:
        goods_info = get_goods_detail(goods_url)
        all_goods.append(goods_info)
    # print(all_goods)
    with open("goods.py",'w',encoding="utf-8") as fp:
        json.dump(all_goods,fp,ensure_ascii=False)
    print("数据爬取存储完毕！")
if __name__ == '__main__':
    main()