from tkinter import filedialog
import base64
import io
import requests


def upload_image():
    filename = get_image_file_name()
    b64_string = convert_file_to_b64(filename)
    out_data = {"image": b64_string, "net_id": "sbp31", "id_no": 172}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image",
                      json=out_data)
    r1 = requests.get("http://vcm-21170.vm.duke.edu/get_image/sbp31/172")
    ret_b64_string = r1.text
    print(ret_b64_string)
    image_bytes = base64.b64decode(ret_b64_string)
    new_filename = filedialog.asksaveasfilename()
    with open(new_filename, "wb") as out_file:
        out_file.write(image_bytes)


def get_image_file_name():
    filename = filedialog.askopenfilename()
    return filename


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


if __name__ == '__main__':
    upload_image()
