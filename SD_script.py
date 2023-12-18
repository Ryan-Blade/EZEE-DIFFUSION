import os
import ctypes
import subprocess
import requests

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Checks if the script is running with administrator privileges
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)

    # Exits the script if the user doesn't grant administrator privileges
    exit()

# Sets the folder name, Git repository URL, and file download URL
folder_name = "Stable Diffusion"
git_repo_url = "https://github.com/AUTOMATIC1111/stable-diffusion-webui"  # Replace with your Git repository URL
file_download_url = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt"

# Sets the path to the C drive
c_drive_path = "C:\\"

# Creates the folder path
folder_path = os.path.join(c_drive_path, folder_name)

# Checks if the folder already exists
if os.path.exists(folder_path):
    print(f"Folder '{folder_name}' already exists in the C drive.")
else:
    try:
        # Creates the folder in the C drive
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully in the C drive.")
        
        # Changes the current working directory to the new folder
        os.chdir(folder_path)
        
        # Git clones the repository
        subprocess.run(["git", "clone", git_repo_url])
        
        print(f"Git repository cloned into '{folder_name}' folder.")
    except OSError as e:
        print(f"Failed to create folder '{folder_name}'. Error: {e}")

# Creates the models folder if it doesn't exist
models_folder_path = os.path.join(folder_path, "stable-diffusion-webui", "models", "Stable-diffusion")
os.makedirs(models_folder_path, exist_ok=True)

# Downloads the file and save it to the specified path
file_path = os.path.join(models_folder_path, "v1-5-pruned-emaonly.ckpt")
response = requests.get(file_download_url)
with open(file_path, 'wb') as file:
    file.write(response.content)

print(f"File downloaded and saved to '{file_path}'.")
