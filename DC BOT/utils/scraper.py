import requests
from bs4 import BeautifulSoup

def get_announcements(page=1):
    url = f'https://ap2.pccu.edu.tw/pccupost/post/List.asp?page={page}'  # 修改为适合的 URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    announcements = []
    
    # 根据网页的结构抓取公告信息
    table = soup.find('table')  # 假设公告在表格中
    rows = table.find_all('tr')[1:]  # 跳过表头
    
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            title = columns[3].text.strip()  # 公告标题
            date_range = columns[0].text.strip()  # 公告日期
            organization = columns[2].text.strip()  # 组织
            # 格式化标题，例如"组织 - 日期范围: 标题"
            announcements.append((f"{organization} - {date_range}: {title}", columns[1].find('a')['href']))  # 假设链接在第二列
            
    return announcements
