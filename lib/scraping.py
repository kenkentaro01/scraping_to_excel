from bs4 import BeautifulSoup
import urllib.request as req
import urllib
import os
import time

# 全銀協TIBOR運営期間サイトからpdfを取得
zengin_url = "https://www.jbatibor.or.jp/rate/"
res = req.urlopen(zengin_url)
soup = BeautifulSoup(res,"html.parser")

# selectメソッドで「,」を入れるとまたはといった表現になる。
result = soup.select('.box_article_content a[target="_blank"][href*="JAPANESEYENTIBOR"]')

pdf_link = result[0].get("href")
# URLからファイル名を抽出する
pdf_filename = pdf_link.split('/')[-1]

target_dir = "./json_output"

save_path = os.path.join(target_dir,pdf_filename)
print(save_path)
urllib.request.urlretrieve(pdf_link, save_path)
time.sleep(2)