import os
import shutil
import tkinter

from datetime import date
from tkinter import filedialog


def get_all_file_dw():
    dir_root = os.getcwd()
    filelist = []
    list_ext = ["webm", "webp", "jpg", "m4a", "mp4"]
    for root, dirs, files in os.walk(dir_root):
        for file in files:
            if "dw_data_yt" not in str(os.path.join(root,file)):
                if file.split(".")[-1] in list_ext:
                    filelist.append(os.path.join(root,file))
    return filelist

def dw_data(url):
    if "http" in url:
        domain = url.split("/")[2]
    else:
        domain = url.split("/")[0]
    if domain in domain_list.keys():
        print("[INFO]", url)
        os.system(cmd_base["win"] + cover_param + root_cmd[domain_list[domain]]+url)
        list_file = get_all_file_dw()
        target_folder = os.getcwd() + "/dw_data_yt" + current_date_f + "/" + root_folder[domain_list[domain]]
        if not os.path.isdir(target_folder):
            os.mkdir(target_folder)
        for ii in list_file:
            shutil.move(ii, target_folder)
    else:
        print("[ERROR]", domain, "not support")

global domain_list
global root_cmd
global root_folder
global current_date
global cmd_base
global cover_param
root_cmd = [
    """--cookies-from-browser firefox --add-metadata -f "bestvideo[height<=1080][ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best" --download-archive the_list.txt """,
    """--add-metadata -f "bestvideo[height<=1080]+bestaudio/best/best" --download-archive the_list.txt """,
    """--add-metadata -f Source --download-archive the_list.txt """,
    """--add-metadata -f "bestvideo[height<=1080]+bestaudio/best/best" --download-archive the_list.txt """,
    """--add-metadata -f "bestvideo[height<=1080]+bestaudio/best/best" --download-archive the_list.txt """
]
root_folder = [
    "YouTube",
    "PornHub",
    "EcchiIwara",
    "NicoVideo",
    "VXideos"
]
cmd_base = {
    "win":".\yt-dlp.exe ",
    "lin":"yt-dlp "
}
domain_list = {"youtu.be":0, "youtube.com":0, "www.youtube.com":0,
"rt.pornhub.com":1, "pornhub.com":1,
"ecchi.iwara.tv":2,
"nicovideo.jp":3, "www.nicovideo.jp":3,
"www.xvideos.com":4,"xvideos.com":4}

root = tkinter.Tk()
root.withdraw()
today = date.today()
os.system(".\yt-dlp.exe -U")
if not os.path.isdir(os.getcwd() + "/dw_data_yt"):
    os.mkdir(os.getcwd() + "/dw_data_yt")
current_date = today.strftime("%Y-%m-%d")
print("+-------------------+")
print("| yt-dlp помощник   |")
print("|          v 0.0.1a |")
print("| GitHub: Hell13Cat |")
print("+-------------------+")
url_need = input("[Ввести ссылки вручную?]+/->")
if url_need != "-":
    list_url_file = os.getcwd() + "/" + "the_list_dw.txt"
    open(list_url_file, "w")
    os.system(list_url_file)
    url = ""
else:
    list_url_file = filedialog.askopenfilename()
    url = ""
cover_need = input("[Нужны ли обложки?]+/->")
if cover_need != "-":
    cover_param = "--write-thumbnail "
else:
    cover_param = ""
date_need = input("[Добавить в папку по дате?]+/->")
if date_need != "-":
    current_date_f = "/bydata/" + current_date
    if not os.path.isdir(os.getcwd() + "/dw_data_yt" + current_date_f):
        os.mkdir(os.getcwd() + "/dw_data_yt" + current_date_f)
    print("[DATE]", current_date)
else:
    current_date_f = ""
if list_url_file == "":
    list_url_file = os.getcwd() + "/" + "the_list_dw.txt"
    if not os.path.isfile(list_url_file):
        open(list_url_file, "w")
    os.system(list_url_file)
urls = open(list_url_file, "r").read().split("\n")
count_vid = 0
for url in urls:
    count_vid += 1
    print("[INFO]", count_vid, "-", len(urls), "downloading....")
    dw_data(url)
ddd = input("[END] ...")