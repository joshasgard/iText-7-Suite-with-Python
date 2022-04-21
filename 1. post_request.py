import requests

API_URL = "http://18.224.190.115:8080/api/job/"

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
