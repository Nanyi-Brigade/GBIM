import os
from handdet import HandDet
from handclas import HandClas
from utils import Camera

# 打开web地图
web_path = '"C:/Program Files (x86)/Lenovo/SLBrowser/SLBrowser.exe"'  # 自己的浏览器路径
map_url = "https://map.baidu.com/@11585451,3556256.7499999995,12z"  # 成都
os.system(web_path + " " + map_url)
# 手识别的测试
hdet = HandDet("handdet/output/best_model")
hclas = HandClas("handclas/output/best_model")
test_camera = Camera(
    updata_func=hdet.get_vis,
    save_func=hdet.get_hand,
    class_func=hclas.get_clas)
print("Start acquisition, press 'q' to exit.")
test_camera.get_img()