
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    entry_output_folder.delete(0, tk.END)
    entry_output_folder.insert(0, folder_path)

def convert_to_exe():
    file_path = entry_file_path.get()
    output_folder = entry_output_folder.get()
    if not file_path:
        messagebox.showerror("Fehler", "Bitte wählen Sie eine Python-Datei aus.")
        return
    if not output_folder:
        messagebox.showerror("Fehler", "Bitte wählen Sie einen Zielordner aus.")
        return

    try:
        subprocess.run(['python', '-m', 'PyInstaller', '--onefile', '--windowed', '--distpath', output_folder, file_path], check=True)
        exe_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + '.exe')
        if os.path.exists(exe_file):
            messagebox.showinfo("Erfolg", f"Die Datei wurde erfolgreich konvertiert: {exe_file}")
        else:
            messagebox.showerror("Fehler", "Die Konvertierung ist fehlgeschlagen.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"Fehler bei der Konvertierung: {e}")

root = tk.Tk()
root.title("Python to EXE Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_select_file = tk.Label(frame, text="Python-Datei auswählen:")
label_select_file.grid(row=0, column=0, padx=5, pady=5)

entry_file_path = tk.Entry(frame, width=50)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Durchsuchen", command=select_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

label_output_folder = tk.Label(frame, text="Zielordner auswählen:")
label_output_folder.grid(row=1, column=0, padx=5, pady=5)

entry_output_folder = tk.Entry(frame, width=50)
entry_output_folder.grid(row=1, column=1, padx=5, pady=5)

button_output_folder = tk.Button(frame, text="Durchsuchen", command=select_output_folder)
button_output_folder.grid(row=1, column=2, padx=5, pady=5)

button_convert = tk.Button(frame, text="In EXE konvertieren", command=convert_to_exe, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
button_convert.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
