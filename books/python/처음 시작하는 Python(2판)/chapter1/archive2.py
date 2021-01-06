import webbrowser
import requests # <=== 이 라이브러리는 외부 라이브러리인데, 작성 당시 아직 그 부분을 공부하지 않아서, 이와 같은 에러 메세지 출력됨 ModuleNotFoundError: No module named 'requests'

print( "Let's find an old website!" )

site = input( "Type a website : " )
era = input( "Type a year, month, and day, like 20150613" )

url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)

response = requests.get(url)
text = response.json()

try :
    old_site = data["archived_snapshot"]["closest"]["url"]
    print( "Found this copy : ", old_site )
    print( "It should appear in your browser now." )
    webbrowser.open(old_site)
except : 
    print( "Sorry, no luck finding", site)



