import requests
import polling

API_URL = "http://18.224.190.115:8080/api/job/"
job_id = "1975cc15-7d48-4504-bbeb-14ffe753ed8d"  # Check your job id from your post request response

status_url = API_URL + job_id

# Polling status and download
polling.poll(
    lambda: requests.get(status_url).json().get("status") == "FINISHED",
    step=60,
    poll_forever=True)
print("Job is Finished. Proceeding to download....")

