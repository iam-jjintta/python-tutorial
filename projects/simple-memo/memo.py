
import sys
import webbrowser
import tkinter as tk

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class FileManager:

    filetypes = (('텍스트 파일', '*.txt'), ('모든 파일', '*.*'))
    filename = None
    text = None

    @classmethod
    def open_file(cls, event=None):
        try:
            cls.filename = askopenfilename(initialdir='/',
                                           title = '파일 열기',
                                           filetypes=cls.filetypes)

            with open(cls.filename) as file:
                cls.text.delete('1.0', 'end')
                for line in file.readlines():
                    cls.text.insert('end', line)

        except FileNotFoundError as e:
            pass

    @classmethod
    def save_as_file(cls, event=None):
        try:
            cls.filename = asksaveasfilename(initialdir='/',
                                             title='다른 이름으로 저장',
                                             filetypes=cls.filetypes)

            with open(cls.filename, 'w') as file:
                file.write(cls.text.get('1.0', 'end-1c'))

        except FileNotFoundError as e:
            pass

    @classmethod
    def save_file(cls, event=None):
        if not cls.filename:
            cls.save_as_file(event)
        else:
            try:
                with open(cls.filename, 'w') as file:
                    file.write(cls.text.get('1.0', 'end-1c'))

            except FileNotFoundError as e:
                pass


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.setting_window()
        self.create_widgets()
        self.setting_shortcut()


    def setting_window(self):
        def setting_window_size(width, height):
            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()
            x = (ws / 2) - (width / 2)
            y = (hs / 2) - (height / 2)

            self.master.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        self.master.title('흔한 찐따의 메모장')
        setting_window_size(640, 480)


    def create_widgets(self):
        def create_filemenu():
            menu = tk.Menu(tearoff=False)
            menu.add_command(label='열기',
                            accelerator='Ctrl+O',
                            command=self.fm.open_file)
            menu.add_command(label='저장',
                            accelerator='Ctrl+S',
                            command=self.fm.save_file)
            menu.add_command(label='다른 이름으로 저장',
                            accelerator='Ctrl+A',
                            command=self.fm.save_as_file)
            menu.add_command(label='종료',
                            accelerator='Ctrl+Q',
                            command=self.master.destroy)
            return menu

        def create_helpmenu():
            menu = tk.Menu(tearoff=False)
            menu.add_command(label='찐따 격리소',
                             command=lambda: webbrowser.open('https://iamjjintta.tistory.com/'))
            menu.add_command(label='흔한 찐따의 GitHub 페이지',
                             command=lambda: webbrowser.open('https://github.com/iam-jjintta/'))
            return menu

        self.text = tk.Text()
        self.text.pack(fill='both', expand=True)

        self.fm = FileManager
        self.fm.text = self.text

        self.menu = tk.Menu(self.master, tearoff=False)

        filemenu = create_filemenu()
        self.menu.add_cascade(label='파일', menu=filemenu)

        helpmenu = create_helpmenu()
        self.menu.add_cascade(label='도움말', menu=helpmenu)

        self.master.config(menu=self.menu)


    def setting_shortcut(self):
        self.text.bind('<Control-o>', self.fm.open_file)
        self.text.bind('<Control-s>', self.fm.save_file)
        self.menu.bind_all('<Alt_L><o>', self.fm.open_file)
        self.menu.bind_all('<Alt_L><s>', self.fm.save_file)
        self.menu.bind_all('<Alt_L><a>', self.fm.save_as_file)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
    sys.exit(0)
