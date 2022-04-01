
import sys
import tkinter as tk

from pyemail.mailbox import MailBox


title = '흔한 찐따의 이메일 프로그램'
icon = 'icon.ico'


if __name__ == '__main__':
    root = tk.Tk()
    mailbox = MailBox(root, title=title, icon=icon)
    mailbox.mainloop()
    sys.exit(0)
