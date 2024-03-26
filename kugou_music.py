#导入需要的库
import requests

#网络资源
m_url = "https://webfs.hw.kugou.com/202403252046/f53571164e68f1d5d4da1088e2a7f303/v2/c187f8a1b35424cbc8d7fcd78fdcff66/part/0/2352345/G326/M0A/F0/53/clip_JpUEAGS-lgyAaDU1AC3vJo0iRNs543.mp3"

#伪装定义了一个字典
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}

#请求数据
m_resp = requests.get(m_url,headers = headers)

#下载保存
with open("music.mp3","wb") as file:
    file.write(m_resp.content)

