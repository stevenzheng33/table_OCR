import requests
import os

from aip import AipOcr

import baidu_config as bc


""" My APPID AK SK """

client = AipOcr(bc.APP_ID, bc.API_KEY, bc.SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def read_image_to_xls(filepath, newfile_name, outputpath):
    result = client.tableRecognition(
    get_file_content(filepath),
        {
            'result_type': 'excel',
        },
    )
    print(filepath)
    print(result)
    result_url = result['result']['result_data']
    excel_file = requests.get(result_url, allow_redirects=True)

    open(os.path.join(outputpath, newfile_name) , 'wb').write(excel_file.content)


def convert_all_images(inputpath, outputpath):
    for filename in os.listdir(inputpath):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            completeName = os.path.join(inputpath, filename)
            read_image_to_xls(completeName, filename[:-4]+'.xls', outputpath)
