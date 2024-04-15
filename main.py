import tkinter as tk
from tkinter import filedialog
import pytube
# Hàm tải video
def download_video():
    # Lấy URL video từ trường nhập liệu
    url = url_entry.get()
    # Kiểm tra URL video hợp lệ
    if not is_valid_url(url):
        error_label.config(text="URL video không hợp lệ!")
        return

    # Lấy chất lượng video
    quality = selected_quality.get()

    # Lấy thư mục lưu video
    save_dir = save_dir_entry.get()

    # Tải video xuống
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.filter(resolution=quality).first()
        video.download(save_dir)
        # Hiển thị thông báo tải xuống thành công
        success_label.config(text="Tải video thành công!")
    except Exception as e:
        # Hiển thị thông báo lỗi
        error_label.config(text=f"Lỗi tải video: {e}")

# Kiểm tra URL video hợp lệ
def is_valid_url(url):
    # Sử dụng biểu thức chính quy để kiểm tra URL
    import re
    regex = r"(?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/watch\?v=([a-zA-Z0-9_-]+)"
    match = re.search(regex, url)
    return bool(match)

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Tải video YouTube")

# Khung nhập URL video
url_frame = tk.Frame(root)
url_frame.pack()

url_label = tk.Label(url_frame, text="URL video:")
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(url_frame)
url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Khung lựa chọn chất lượng và thư mục lưu
quality_frame = tk.Frame(root)
quality_frame.pack()

quality_label = tk.Label(quality_frame, text="Chất lượng video:")
quality_label.pack(side=tk.LEFT)

# Tạo biến để lưu chất lượng video được chọn
selected_quality = tk.StringVar()
selected_quality.set("360p")  # Thiết lập chất lượng mặc định

quality_dropdown = tk.OptionMenu(quality_frame, selected_quality, "360p", "480p", "720p", "1080p")
quality_dropdown.pack(side=tk.LEFT)

save_dir_label = tk.Label(quality_frame, text="Thư mục lưu:")
save_dir_label.pack(side=tk.LEFT)

# Tạo biến StringVar để lưu đường dẫn được chọn
selected_save_dir = tk.StringVar()

save_dir_entry = tk.Entry(quality_frame, textvariable=selected_save_dir)
save_dir_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

def select_save_dir():
    selected_save_dir.set(filedialog.askdirectory())

save_dir_button = tk.Button(quality_frame, text="Chọn thư mục", command=select_save_dir)
save_dir_button.pack(side=tk.LEFT)

# Nút tải xuống
download_button = tk.Button(root, text="Tải xuống", command=download_video)
download_button.pack(pady=10)

# Hiển thị thông báo
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

success_label = tk.Label(root, text="", fg="green")
success_label.pack()

# Chạy giao diện
root.mainloop()