from ast import arg
import requests
import polling
import logging

API_URL = "http://18.224.190.115:8080/api/job/"
job_id = EXAMPLE_JOB_ID

status_url = "".join([API_URL, job_id])
get_file_url = "".join([status_url, "/file/result"])

# Polling status and download
def custom_request(url: str):
    if requests.get(url=url).json().get("status") != "FINISHED":
        logging.info("Polling started.......")
        logging.info("Waiting.......")
        return False
    return True


def main():
    try:
        # Check result status
        polling.poll(custom_request, step=60, args=(status_url), poll_forever=True)
        print("Got status as Finished. Proceeding....")
        # Download result when status is Finished
        download_result = requests.get(get_file_url)
        with open("result.jpg", "wb") as f:
            f.write(download_result.content)
        exit()
    except:
        logging.info("exiting")
        exit()


main()
