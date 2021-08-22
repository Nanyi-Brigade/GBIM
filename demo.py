import os
from handdet import HandDet
from handclas import HandClas
from utils import Camera

# 打开web地图
web_path = '"C:/Program Files (x86)/Lenovo/SLBrowser/SLBrowser.exe"'  # 自己的浏览器路径
map_url = "https://map.baidu.com/search/%E5%85%A8%E5%9B%BD/@12959219.600021668,4825334.630023856,4.09z/maptype%3DB_EARTH_MAP?querytype=s&wd=%E5%85%A8%E5%9B%BD&c=1&provider=pc-aladin&pn=0&device_ratio=2&da_src=shareurl"
os.system(web_path + " " + map_url)
# 手识别的测试
hdet = HandDet("handdet/output/best_model")
hclas = HandClas("handclas/output/best_model")
test_camera = Camera(
    update_func=hdet.get_hand,
    class_func=hclas.get_clas)
print("Start acquisition, press 'q' to exit.")
test_camera.get_img()