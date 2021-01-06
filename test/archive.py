import webbrowser # python표준 라이브러리인 webbrowser를 import
import json # python표준 라이브러리인 json을 import
from urllib.request import urlopen # python표준 라이브러리인 urllib.request모듈에서 urlopen만 import

print("Let's find an old website.") # String 출력

site = input("Type a website URL: ") # 사용자에게 URL을 입력받아서, site 변수에 저장
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)

# TEST
# print("====================> ", url)

response = urlopen(url) # 위에서 만들어진 url의 웹서버에 연결하여 웹서비스 요청
contents = response.read() # 응답 데이터를 가져와서 contents변수에 할당

text = contents.decode("UTF-8") # 내용을 JSON형식의 텍스트 문자열로 디코딩하여 text변수에 할당
data = json.loads(text) # text를 데이터(파이썬 자료구조)로 변환

##
# 예외처리 부분
#  오류를 확인하는데, 없다면 try: 안의 4줄을 실행하고, 실패하면 except: 다음의 1줄을 실행한다.
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)



