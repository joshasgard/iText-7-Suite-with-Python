import requests
import polling

API_URL = "http://18.224.190.115:8080/api/job/"
job_id = "421223fb-e363-43fc-b4fe-4e2aa36f84ed"  # Check your job id from your post request response

status_url = API_URL + job_id
# url_try = "http://18.224.190.115:8080/api/job/421223fb-e363-43fc-b4fe-4e2aa36f84ed"
get_file_url = status_url + "file/result"

# Polling status and download
def test(response):
    return response.status_code == 200


def main():
    try:
        # Check result status
        polling.poll(
            lambda: requests.get(status_url),
            step=60,
            poll_forever=True,
            check_success=test,
        )
        print("Job is Finished. Proceeding to download....")

        # Download result when status is Finished
        download_result = requests.get(get_file_url)
        with open("result.jpg", "wb") as f:
            f.write(download_result.content)

    except KeyboardInterrupt:
        print("exiting")
        exit()


main()
