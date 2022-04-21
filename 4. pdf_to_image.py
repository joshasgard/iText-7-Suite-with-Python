import requests
import polling

API_URL = "http://18.224.190.115:8080/api/job/"


def postRequest():
    # Send Post Request for PDF to IMAGE CONVERSION
    payload = {
        "job": {
            "request": {
                "type": "PDF_TO_IMAGES",
                "imageType": "JPEG",
                "pageNumbers": "1",
                "defaultPageScaling": 1,
            },
            "sourceFiles": {
                "checksum": "a0078eae317194bf913db457b16a54fd",
                "fileType": "application/pdf",
                "fileSize": 318046,
                "fileName": "test.pdf",
            },
        }
    }

    headers = {
        "Content-Type": "multipart/form-data;boundary=----arbitraryboundary",
        "Connection": "keep-alive",
    }

    files = {"file": open("test.pdf", "rb")}

    response = requests.post(API_URL, data=payload, files=files, headers=headers)
    print(response.text)
    return response


# Polling status and download
def test(response):
    return response.json().get("status") == "FINISHED"


def main():
    try:
        # Send Post request
        post_response = postRequest()
        job_id = post_response.json().get("id")
        status_url = API_URL + job_id
        get_file_url = status_url + "file/result"
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
