'''
흔한 찐따의 파이썬 실행기
'''


import tkinter as tk


class FileDialog:
    "기존의 FileManager -> FileDialog로 변경"

    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfilename


    def __init__(self, text):
        self.text = text
        self.filename = None
        self.filetypes = (
            ('Python File', '*.py'),
            ('All File', '*.*')
        )


    def open_file(self, event=None):
        openfilename = FileDialog.askopenfilename
        self.filename = openfilename(
            initialdir='/',
            title='파일 열기',
            filetypes=self.filetypes
        )

        try:
            with open(self.filename, mode='r', encoding='locale') as file:
                self.text.delete('1.0', 'end')
                for line in file.readlines():
                    self.text.insert('end', line)
        except FileNotFoundError:
            pass


    def save_as_file(self, event=None):
        saveasfilename = FileDialog.asksaveasfilename
        self.filename = saveasfilename(
            initialdir='/',
            title='다른 이름으로 저장',
            filetypes=self.filetypes
        )
        self._save_file()


    def save_file(self, event=None):
        if not self.filename:
            self.save_as_file()
        else:
            self._save_file()


    def _save_file(self):
        try:
            filename = self.filename
            ext = filename.split('/')[-1]
            if '.' not in ext:
                filename = self.filename + '.py'
                self.filename = filename
            with open(filename, mode='w', encoding='locale') as file:
                text = self.text.get('1.0', 'end-1c')
                file.write(text)
        except FileNotFoundError:
            pass


class Menubar:
    "메뉴바 클래스 새로 추가"

    import webbrowser


    def __init__(self, filedialog):
        self.filedialog = filedialog
        self._menu = tk.Menu(tearoff=False)
        self.initialization()


    @property
    def menu(self):
        return self._menu


    def initialization(self):
        filemenu = self.generate_filemenu()
        self._menu.add_cascade(label='파일', menu=filemenu)

        helpmenu = self.generate_helpmenu()
        self._menu.add_cascade(label='도움말', menu=helpmenu)


    def generate_filemenu(self):
        menu = tk.Menu(tearoff=False)
        menu.add_command(
            label='열기',
            accelerator='Ctrl+O',
            command=lambda: self.filedialog.open_file()
        )
        menu.add_command(
            label='저장',
            accelerator='Ctrl+S',
            command=lambda: self.filedialog.save_file()
        )
        menu.add_command(
            label='다른 이름으로 저장',
            accelerator='Ctrl+A',
            command=lambda: self.filedialog.save_as_file()
        )
        return menu


    def generate_helpmenu(self):
        webbrowser = Menubar.webbrowser
        menu = tk.Menu(tearoff=False)
        menu.add_command(
            label='찐따 격리소',
            command=lambda: webbrowser.open('https://iamjjintta.tistory.com/')
        )
        menu.add_command(
            label='흔한 찐따의 GitHub 페이지',
            command=lambda: webbrowser.open('https://github.com/iam-jjintta/')
        )
        return menu


class OutputWindow(tk.Toplevel):
    "파이썬 코드 실행 시 결과창"

    from .pyexc import Executor


    def __init__(self, master=None, title='Output'):
        super().__init__(master)
        self.title(title)
        self.executor = OutputWindow.Executor()


    def execute(self, code):
        output = self.executor.runcode(code)

        text = tk.Text(self)
        text.pack(fill='both', expand=True)

        text.insert('end', f'[Python v{self.executor.version}]\n')
        text.insert('end', output)

        text.configure(
            font=("Consolas", 16)
            # , state='disabled'
        )


class Editor(tk.Frame):
    "텍스트 에디터"

    def __init__(self, master=None, title='흔한 찐따의 파이썬 실행기', width=640, height=480):
        super().__init__(master)
        self.setting_window(title=title, width=width, height=height)
        self.create_widgets()
        self.bind_events()


    def setting_window(self, title, width=640, height=480):
        def resize_window(width, height):
            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()
            x = int((ws / 2) - (width / 2))
            y = int((hs / 2) - (height / 2))
            self.master.geometry(f'{width}x{height}+{x}+{y}')
        self.master.title(title)
        resize_window(width, height)


    def create_widgets(self):
        self.text = tk.Text()
        self.text.pack(fill='both', expand=True)

        self.font_size = 16
        self.text.configure(
            font=("Consolas", self.font_size),
        )

        self.filedialog = FileDialog(self.text)
        self.menubar = Menubar(self.filedialog)
        runmenu = tk.Menu(tearoff=False)
        runmenu.add_command(
            label='실행',
            accelerator='F5',
            command=lambda: self.execute()
        )
        self.menubar.menu.add_cascade(label='실행 (F5)', menu=runmenu)
        self.master.config(menu=self.menubar.menu)


    def resize_font(self, event):
        "마우스 줌인(Zoom-In) 줌아웃(Zoom-Out) 이벤트"
        if event.delta > 0:
            if self.font_size >= 100:
                return
            else:
                self.font_size += 2
        elif event.delta < 0:
            if self.font_size <= 7:
                return
            else:
                self.font_size -= 2
        self.text.configure(font=("Consolas", self.font_size))


    def execute(self, event=None):
        "코드 실행 이벤트"
        code = self.text.get('1.0', 'end-1c')
        outwin = OutputWindow()
        outwin.execute(code)


    def replace(self, event=None):
        "Tab 문자 치환 이벤트"
        self.text.insert(tk.INSERT, ' '*4)
        return 'break'


    def bind_events(self):
        self.text.bind('<Control-o>', lambda e: self.filedialog.open_file())
        self.text.bind('<Control-s>', lambda e: self.filedialog.save_file())
        self.text.bind('<F5>', lambda e: self.execute())
        self.text.bind('<Control_L><MouseWheel>', self.resize_font)
        self.text.bind('<Tab>', lambda e: self.replace())
        menu = self.menubar.menu
        menu.bind_all('<Alt_L><o>', lambda e: self.filedialog.open_file())
        menu.bind_all('<Alt_L><s>', lambda e: self.filedialog.save_file())
        menu.bind_all('<Alt_L><a>', lambda e: self.filedialog.save_as_file())

