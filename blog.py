# 네이버 검색 API 예제 - KBO 검색
import os
import sys
import urllib.request
import json

print("KBO 검색")

client_id = 
client_secret = 
encText = urllib.parse.quote("KBO")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
json_data = ""
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    json_data = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

# Parse the JSON data
data = json.loads(json_data)

extracted_teams = []
for team in data['league']['teams']:
    extracted_team = {
        "name": team.get("name", ""),
        "location": team.get("location", ""),
        "website": team.get("website", "")
    }
    extracted_teams.append(extracted_team)

# 출력
for team in extracted_teams:
    print("팀 이름:", team['name'])
    print("연고지:", team['location'])
    print("홈페이지:", team['website'])
