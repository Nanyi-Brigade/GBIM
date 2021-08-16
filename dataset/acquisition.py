from utils import Camera


if __name__ == "__main__":
    save_path = "dataset"
    acq_camera = Camera()
    print("Start acquisition, press 'q' to exit.")
    acq_camera.get_img(save_path)