import subprocess
import os
import shutil

def get_libreoffice_path():
    cmd = shutil.which("libreoffice") or shutil.which("soffice")
    if cmd:
        return cmd
    win_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
    if os.path.exists(win_path):
        return win_path
    return "libreoffice"

def convert_docx_to_pdf(input_path, output_path):
    output_dir = os.path.dirname(output_path)
    libreoffice_path = get_libreoffice_path()
    command = [
        libreoffice_path,
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        output_dir,
        input_path
    ]

    subprocess.run(command, check=True)

