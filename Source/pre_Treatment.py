import cv2
import os
import glob

# Tien xu ly 
class pre_Treatment():
    
    # Tach anh tu video, input path video, output path chua img 
    def VDtoIMG(input_Path,output_Path, id_IMG, count = 0):

        # exist_ok = True => xử lý khi thư mục đã tồn tại
        os.makedirs(output_Path, exist_ok=True)

        video = cv2.VideoCapture(input_Path)

        # Lấy (fps) của video
        fps = int(video.get(cv2.CAP_PROP_FPS))
        

        while True:
            # Đọc một frame từ video
            ret, frame = video.read()

            if not ret:
                break

            if count % fps == 0:
                # Tính toán thời gian của frame hiện tại
                seconds = count // fps
                image_path = os.path.join(output_Path, f'image_{seconds}_{id_IMG}.jpg')
                cv2.imwrite(image_path, frame)

            count += 1
        video.release()
        print(f"_______Complete !, IMGS is saved in '{output_Path}' ")

    # Dọn thư mục 
    def clean_Up_Folder(path_In):
        # Lấy tất cả các tệp trong thư mục
        files = glob.glob(os.path.join(path_In, "*"))

        # Xóa từng tệp trong thư mục
        for file in files:
            if os.path.isfile(file):
                os.remove(file)

        print(f"_______{path_In} is cleaned !")





vdPath = r"D:\Work\ComputerVison_MouseControl\Data\VD_1.mp4"
outPath = r"D:\Work\ComputerVison_MouseControl\Data\IMG"
outPath2 = r"D:\Work\ComputerVison_MouseControl\Data\IMG2"

pre_Treatment.clean_Up_Folder(outPath)
# pre_Treatment.VDtoIMG(vdPath,outPath)


