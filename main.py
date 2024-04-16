from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog
from pytube import YouTube
import os
import tkinter as tk
# Hàm tải video
def download_video():
    # Lấy URL video từ trường nhập liệu
    url = url_entry.get()
    # Lấy chất lượng video
    quality = res.get()
    # Lấy thư mục lưu video
    save_dir = save_dir_entry.get()
    if save_dir=="":
        save_dir="downloads"
    # Tải video xuống
    progress_label.grid(row=5, column=0, sticky="ew")
    progress_bar.grid(row=5,column=1)
    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        video = yt.streams.filter(resolution=quality).first()
        os.path.join("Tải xuống", f"{yt.title}")
        video.download(save_dir)
        # Hiển thị thông báo tải xuống thành công
        status_label.configure(text="Tải video thành công!",text_color="green")
    except Exception as e:
        # Hiển thị thông báo lỗi
        status_label.configure(text=f"Lỗi tải video: {e}",text_color="red")
def on_progress(video,chunk,bytes_remaining):
    total_size=video.filesize
    bytes_dowloaded =total_size-bytes_remaining
    percent_completed=bytes_dowloaded/total_size*100    
    progress_label.configure(text=str(int(percent_completed))+"%")
    progress_label.update()
    progress_bar.set(float(percent_completed/100))

# Kiểm tra URL video hợp lệ
def is_valid_url(url):
    # Sử dụng biểu thức chính quy để kiểm tra URL
    import re
    regex = r"(?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/watch\?v=([a-zA-Z0-9_-]+)"
    match = re.search(regex, url)
    return bool(match)
def find_url():
    url = url_entry.get()
    if not is_valid_url(url):
        status_label.configure(text="URL không hợp lệ", text_color="red")
        return
    else:
        try:
            yt = YouTube(url)
            status_label.configure(text=yt.title, text_color="green")
            ress = [i.resolution for i in yt.streams if i.resolution]
            ress = list(set(ress))
            ress.sort()
            quality_combobox.config(values=ress)
            return
        except Exception as e:
        # Hiển thị thông báo lỗi
            status_label.configure(text=f"{e}",text_color="red")


# Tạo giao diện người dùng
root = ctk.CTk()
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("System")
# Tạo title
root.title("Phần mềm Tải video YouTube")
# Giới hạn cho giao diện
root.geometry("720x480")
root.minsize(720,480)
root.maxsize(1080,720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH,expand=True,padx=10,pady=10)
content_frame.grid_columnconfigure(0, weight=3,)
content_frame.grid_columnconfigure(1, weight=5,)
content_frame.grid_columnconfigure(2, weight=2,)
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_rowconfigure(1, weight=1) 
content_frame.grid_rowconfigure(2, weight=1)  
content_frame.grid_rowconfigure(3, weight=1) 
content_frame.grid_rowconfigure(4, weight=1)
content_frame.grid_rowconfigure(5, weight=1)  
# Khung nhập URL video
title_label=ctk.CTkLabel(content_frame,text="Tải video Yotube",font=("Arial", 24, "bold"))
url_label = ctk.CTkLabel(content_frame, text="Nhập link youtube:")
url_entry = ctk.CTkEntry(content_frame,width = 400 , height = 40)
# Nút tìm kiếm
find_icon = tk.PhotoImage(file="icon/image.png")
find_icon.__sizeof__
find_button = ctk.CTkButton(content_frame,command=find_url,image=find_icon,text="",height = 40,width=40)

# Khung lựa chọn chất lượng và thư mục lưu
quality_label = ctk.CTkLabel(content_frame, text="Chất lượng video:")
# Tạo biến để lưu chất lượng video được chọn
res = ctk.StringVar()
res.set("360p")  # Thiết lập chất lượng mặc định
ress=[]
quality_combobox = ttk.Combobox(content_frame,values=ress,textvariable=res,width=20,height=50 )
save_dir_label = ctk.CTkLabel(content_frame, text="Thư mục lưu:")
# Tạo biến StringVar để lưu đường dẫn được chọn
selected_save_dir = ctk.StringVar()
save_dir_entry = ctk.CTkEntry(content_frame, textvariable=selected_save_dir, width = 400 , height = 40)
def select_save_dir():
    selected_save_dir.set(filedialog.askdirectory())
save_dir_button = ctk.CTkButton(content_frame, text="Chọn thư mục", command=select_save_dir)
title_label.grid(row=0,column=1,sticky="ew")
url_label.grid(row=1, column=0, sticky="w")
url_entry.grid(row=1, column=1, sticky="ew")
find_button.grid(row=1, column=2, sticky="ew")
quality_label.grid(row=2, column=0, sticky="w")
quality_combobox.grid(row=2, column=1, sticky="ew")
save_dir_label.grid(row=3, column=0, sticky="w")
save_dir_entry.grid(row=3, column=1, sticky="ew")
save_dir_button.grid(row=3, column=2, sticky="w")
# Nút tải xuống
download_button = ctk.CTkButton(content_frame, text="Tải xuống", command=download_video)
download_button.grid(row=4,column=1)
# # Hiện thị thông tin download
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)
# # Hiển thị thông báo
status_label = ctk.CTkLabel(root, text="",)
status_label.pack(pady=(10,5))

# Chạy giao diện
root.mainloop()