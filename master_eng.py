import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, PhotoImage, Label, Toplevel
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

def loading(callback):
    global loading_window
    loading_window =tk.Toplevel(root)
    loading_window.title("Loading")
    loading_window.geometry("250x150")
    pod_progress = tk.Label(loading_window,text="Signing document...")
    progressbar=ttk.Progressbar(loading_window,mode="indeterminate",length=150)
    progressbar.pack(pady=10)
    pod_progress.pack(pady=10)
    def cls_loadingWindow():
        progressbar.stop()
        loading_window.destroy()
        callback()
    progressbar.start()
    loading_window.after(2000,cls_loadingWindow)

def generate_signature(private_key, message):
    hashed_message = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hashed_message.update(message)
    digest = hashed_message.finalize()

    signature = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    # Haszowanie danych przed weryfikacją
    hashed_message = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hashed_message.update(message)
    digest = hashed_message.finalize()

    try:
        public_key.verify(
            signature,
            digest,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed: Hash function value is different")
        return False

def sign_file():
    def cllback_after_loading_box():
        messagebox.showinfo("File signed", "Document has been signed as ""Signature.txt")

    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            data = file.read()
            signature = generate_signature(private_key, data)
            encoded_signature = base64.b64encode(signature)
            with open("Signature.txt", 'wb') as signature_file:
                signature_file.write(encoded_signature)
        loading(cllback_after_loading_box)

def verify_file():
    public_key = private_key.public_key()
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            data = file.read()
            with open("Signature.txt", 'rb') as signature_file:
                encoded_signature = signature_file.read()
                signature = base64.b64decode(encoded_signature)
                if verify_signature(public_key, data, signature):
                    messagebox.showinfo("Verification status", "Signature is correct")
                else:
                    messagebox.showerror("Verification status", "Signature is incorrect.")

def readme():
    file_path = "README.txt"
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            readme_window = Toplevel(root)
            readme_window.title("README.txt")
            readme_window.geometry("600x760")


            text_widget = tk.Text(readme_window, wrap="word", width=1920, height=1080)
            text_widget.pack(padx=10, pady=10)


            text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("Eletronic Signature")
icon_path = "lock_icon.ico"

root.geometry("150x150")

root.iconbitmap(icon_path)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

helpframe = tk.Frame(frame)
helpframe.pack(padx=1,pady=5)


label_podpis = tk.Label(helpframe, text="SIGN:", font=('Calibri', 8)) 
label_podpis.pack(side=tk.LEFT, anchor="w")
label_weryfikacja = tk.Label(helpframe, text="VERIFY:", font=('Calibri', 8))
label_weryfikacja.pack(side=tk.RIGHT, anchor="e")

help_button = tk.Button(root, text='?', command=readme)
help_button.place(relx=1.0, rely=0.0, anchor='ne')

photo_sign = PhotoImage(file="folder.png")
photo_sign = photo_sign.subsample(50, 50)
sign_button = tk.Button(frame, image=photo_sign, command=sign_file)
sign_button.pack(side=tk.LEFT, padx=5)

photo_verify = PhotoImage(file="folder.png")
photo_verify = photo_verify.subsample(50, 50)
verify_button = tk.Button(frame, image=photo_verify, command=verify_file)
verify_button.pack(side=tk.RIGHT, padx=5)


root.resizable(False, False)

root.mainloop()
