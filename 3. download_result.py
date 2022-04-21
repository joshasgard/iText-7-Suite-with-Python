import requests

API_URL = "http://18.224.190.115:8080/api/job/"
job_id = "1975cc15-7d48-4504-bbeb-14ffe753ed8d"
status_url = API_URL + job_id
get_file_url = status_url + "file/result"
download_result = requests.get(get_file_url)

with open("result.jpg", "wb") as f:
    f.write(download_result.content)
