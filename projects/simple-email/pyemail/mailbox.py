
import tkinter as tk
from . import simple_email as se


def resize_window(master, width=640, height=480):
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()

    x = int((ws / 2) - (width / 2))
    y = int((hs / 2) - (height / 2))

    master.geometry(f'{width}x{height}+{x}+{y}')


class FileDialog:

    from tkinter.filedialog import askopenfilename


    filetypes = (('모든 파일', '*.*'),)

    def __init__(self, file_inputer):
        self.openfilename = FileDialog.askopenfilename
        self.files = []
        self.file_inputer = file_inputer


    def attach_file(self):
        filename = self.openfilename(
            initialdir='/',
            title='파일 첨부',
            filetypes=self.filetypes
        )
        self.files.append(filename)
        attach_files = ', '.join([file.split('/')[-1] for file in self.files])
        self.file_inputer['text'] = attach_files


    def reset_files(self):
        self.files.clear()
        self.file_inputer['text'] = '없음'


class Login(tk.Toplevel):

    def __init__(self, master=None, title='로그인', icon=None):
        super().__init__(master)
        self.icon = icon

        self.setting_window(title)
        self.create_widgets()
        self.setting_widgets()
        self.grid_widgets()
        self.bind_events()


    def setting_window(self, title, width=250, height=100):
        self.title(title)
        if self.icon:
            self.iconbitmap(self.icon)
        resize_window(self, width, height)


    def create_widgets(self):
        self.lbl_address = tk.Label(self)
        self.address = tk.Entry(self)
        self.lbl_password = tk.Label(self)
        self.password = tk.Entry(self, show='*')
        self.btn_login = tk.Button(self)


    def setting_widgets(self):
        self.lbl_address['text'] = '이메일 계정'
        self.lbl_password['text'] = '비밀번호'
        self.btn_login['text'] = '로그인'


    def grid_widgets(self):
        self.lbl_address.grid(row=0, column=0)
        self.address.grid(row=0, column=1)
        self.lbl_password.grid(row=1, column=0)
        self.password.grid(row=1, column=1)
        self.btn_login.grid(row=2, column=0, columnspan=2)


    def bind_events(self):
        self.btn_login['command'] = lambda: self.login()


    def login(self):
        address = self.address.get()
        password = self.password.get()
        se.EmailAccount.set_account(address, password)
        self.destroy()


class MailBox(tk.Frame):

    def __init__(self, master=None, title='흔한 찐따의 이메일 프로그램', icon=None):
        super().__init__(master)
        self.icon = icon

        self.setting_window(title)
        self.create_widgets()
        self.setting_widgets()
        self.grid_widgets()
        self.bind_events()


    def generate_gmail_sender(self):
        google = se.SERVER_INFO['Google']
        smtp = google['SMTP']
        host = smtp['Host']
        port = smtp['Port']['TSL']

        gmail = se.Email(host, port, is_tsl=True)
        return gmail


    def setting_window(self, title, width=640, height=480):
        self.master.title(title)
        if self.icon:
            self.master.iconbitmap(self.icon)
        resize_window(self.master, width, height)
        self.master.resizable(width=False, height=False)


    def create_widgets(self):
        self.lbl_subject = tk.Label()
        self.subject = tk.Entry()
        self.lbl_to = tk.Label()
        self.to = tk.Entry()
        self.btn_attach = tk.Button()
        self.lbl_attach = tk.Label()
        self.lbl_content = tk.Label()
        self.content = tk.Text()
        self.btn_login = tk.Button()
        self.btn_send = tk.Button()
        self.btn_cancel = tk.Button()
        self.filedialog = FileDialog(self.lbl_attach)


    def setting_widgets(self):
        self.lbl_subject['text'] = '제목'
        self.lbl_to['text'] = '받는 사람'
        self.lbl_content['text'] = '내용'
        self.lbl_attach['text'] = '없음'
        self.btn_attach['text'] = '첨부파일'
        self.btn_login['text'] = '로그인'
        self.btn_send['text'] = '보내기'
        self.btn_cancel['text'] = '취소'


    def grid_widgets(self):
        sticky = tk.N + tk.S + tk.W + tk.E
        self.lbl_subject.grid(row=0, column=0, sticky=sticky)
        self.subject.grid(row=0, column=1, sticky=sticky)
        self.lbl_to.grid(row=1, column=0, sticky=sticky)
        self.to.grid(row=1, column=1, sticky=sticky)
        self.btn_attach.grid(row=2, column=0, sticky=sticky)
        self.lbl_attach.grid(row=2, column=1, sticky=sticky)
        self.lbl_content.grid(row=3, column=0, sticky=sticky)
        self.content.grid(row=3, column=1, sticky=sticky)
        self.btn_login.grid(row=4, column=0, columnspan=2, sticky=sticky)
        self.btn_send.grid(row=5, column=0, columnspan=2, sticky=sticky)
        self.btn_cancel.grid(row=6, column=0, columnspan=2, sticky=sticky)


    def bind_events(self):
        self.btn_attach['command'] = lambda: self.filedialog.attach_file()
        self.btn_login['command'] = lambda: Login(title='로그인', icon=self.icon)
        self.btn_send['command'] = lambda: self.send()
        self.btn_cancel['command'] = lambda: self.cancel()


    def send(self):
        gmail = self.generate_gmail_sender()

        gmail.Subject = self.subject.get()
        gmail.To = self.to.get()
        gmail.From = se.EmailAccount.address
        gmail.Message = self.content.get('1.0', 'end-1c')
        for file in self.filedialog.files:
            gmail.attach(file)

        gmail.send()


    def cancel(self):
        self.subject.delete(0, tk.END)
        self.to.delete(0, tk.END)
        self.content.delete('1.0', tk.END)
        self.filedialog.reset_files()
