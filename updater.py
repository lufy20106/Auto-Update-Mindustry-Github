import os, subprocess, ctypes, time
try:
  import requests
except:
  os.system('pip install requests')
  import requests

# Đường dẫn đến tệp tin cài đặt Mindustry
current_version_file = "version"
mindustry_path = "mindustry.jar"

# Kiểm tra xem tệp tin Current.txt tồn tại hay không, nếu không thì tạo mới
if not os.path.exists(current_version_file):
    with open(current_version_file, "w") as file:
        file.write("None")
elif not os.path.exists(mindustry_path):
      with open(current_version_file, "w") as file:
         file.write("None")
# Lấy phiên bản hiện tại của Mindustry từ tệp tin Current.txt
try:
    with open(current_version_file, "r") as file:
        current_version = file.read().strip()
        print(f"Phiên bản hiện tại của Mindustry: {current_version}")
        time.sleep(0.3)
except Exception as e:
    print(f"Lỗi: {e}")
    current_version = None

if current_version:
    # Lấy phiên bản mới nhất từ GitHub
    response = requests.get("https://api.github.com/repos/Anuken/Mindustry/releases/latest")
    latest_release = response.json()
    latest_version = latest_release["tag_name"]

    if latest_version != current_version:
        print(f"Phiên bản mới của Mindustry được tìm thấy: {latest_version}")
        download_url = latest_release["assets"][0]["browser_download_url"]
        time.sleep(0.3)
        
        # Tải về phiên bản mới
        print("Đang tải về phiên bản mới...")
        response = requests.get(download_url)

        # Lưu trữ phiên bản mới vào tệp tin cài đặt
        with open(mindustry_path, "wb") as f:
            f.write(response.content)

        with open(current_version_file, "w") as file:
            file.write(latest_version)

        print(f"Đã cập nhật Mindustry lên: {latest_version}.")
        print("Mở Mindustry sau 2s")
        time.sleep(2)
        subprocess.Popen(["java", "-jar", mindustry_path])
        cmd_window = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(cmd_window, 0)
    else:
        print("Mindustry đã được cập nhật đến phiên bản mới nhất.")
        print("Mở Mindustry sau 2s")
        time.sleep(2)
        subprocess.Popen(["java", "-jar", mindustry_path])
        cmd_window = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(cmd_window, 0)
else:
    print("Không thể lấy được phiên bản hiện tại của Mindustry.")