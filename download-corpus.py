#!/usr/bin/env python3
import os

import requests


def download_feather(download_path, file_name, url, clean):
    # Define file path
    file_path = os.path.join(download_path, file_name)

    # Check if result needs to be generated
    if clean or not os.path.exists(file_path):
        try:
            data = requests.get(url, verify=False)
            with open(file_path, 'wb') as file:
                file.write(data.content)
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")
            return None


def main():
    file_path = os.path.realpath(__file__)
    script_path = os.path.dirname(file_path)
    download_path = os.path.join(script_path, "corpus", "raw")
    file_name = "speeches.feather"
    url = "https://dvn-cloud.s3.amazonaws.com/10.7910/DVN/FIKIBO/179a4d79861-5829ebf90c25?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27speeches.feather&response-content-type=application%2Foctet-stream&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220527T183228Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAIEJ3NV7UYCSRJC7A%2F20220527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4e2f57360eae5891847bbb72921c9c27c21fdf5ac2b6032599907b1c18331fb7"

    # Make results path
    os.makedirs(os.path.join(download_path), exist_ok=True)

    # Download
    download_feather(download_path=download_path, file_name=file_name, url=url, clean=True)


if __name__ == "__main__":
    main()
