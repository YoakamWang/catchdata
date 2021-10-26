import csv
import requests
from lxml import etree


def get_url(url):
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    html = resp.text
    # resp.encoding="utf-8-sig"
    # html1=resp.text.encode('iso-8859-1').decode('gbk')
    return html


def parse_page(html):
    elem = etree.HTML(html)

    wtime = elem.xpath("//table[@id='hourTable_0']//tr[1]//text()")
    ftime = [i.strip() for i in wtime if i.isspace() == False]
    wtemp = elem.xpath("//table[@id='hourTable_0']//tr[3]//text()")
    ftemp = [i.strip('\n') for i in wtemp if i.isspace() == False]
    wendp = elem.xpath("//table[@id='hourTable_0']//tr[5]//text()")
    fwend = [i.strip('\n') for i in wendp if i.isspace() == False]
    ppas = elem.xpath("//table[@id='hourTable_0']//tr[7]//text()")
    fppas = [i.strip('\n') for i in ppas if i.isspace() == False]
    pwet = elem.xpath("//table[@id='hourTable_0']//tr[8]//text()")
    fwet = [i.strip('\n') for i in pwet if i.isspace() == False]
    #print(ftime)
    data = zip(ftime, ftemp, fwend, fppas, fwet)
    return data


def save2csv(data):
    fd = open("DG_weather.csv", "w", encoding="utf-8-sig", newline="")
    writer_w = csv.writer(fd)
    for row in data:
        writer_w.writerow(row)


def main():
    url = 'https://weather.cma.cn/web/weather/59289.html'
    w_html = get_url(url)
    w_data = parse_page(w_html)
    save2csv(w_data)


if __name__ == "__main__":
    main()
