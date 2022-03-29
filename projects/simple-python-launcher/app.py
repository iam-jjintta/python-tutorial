
import sys
import tkinter as tk

from pyide.editor import Editor


if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap('icon.ico')

    editor = Editor(root, title='흔한 찐따의 파이썬 실행기')
    editor.mainloop()
    sys.exit(0)
