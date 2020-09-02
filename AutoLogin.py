from db_connection import Connection
from login import AutoLogin
import tkinter as tk
import pyperclip
import os


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_geometry(self, '720x480')
        tk.Tk.wm_resizable(self, False, False)
        tk.Tk.wm_title(self, 'LoL Auto Login')
        self.database = Connection('database.db')
        self.current_frame = None
        self.switch_frame(Login)
    
    def switch_frame(self, frame):
        try:
            self.current_frame.destroy()
        except:
            pass
        self.current_frame = frame(self)
        self.current_frame.pack()
    

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        
        self.data = []
        #--------------------
        tk.Label(self, text = 'Auto Login', font = ('Arial', 30, 'bold')).pack(pady = 10)

        frame = tk.Frame(self, bd = 2, relief = tk.GROOVE)
        frame.pack(side = tk.LEFT)
        
        self.listbox = tk.Listbox(frame, font = ('Arial', 18, 'bold'), bd = 0)
        self.listbox.pack(side = tk.LEFT)
        self.scrollbar = tk.Scrollbar(frame, command = self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        tk.Button(self, text = 'Confirm', font = ('Arial', 18, 'bold'), command = self.confirm, width = 15, relief = tk.GROOVE, bd = 3).pack(padx = 50, pady = 15)
        tk.Button(self, text = 'View info', font = ('Arial', 18, 'bold'), command = self.view_info, width = 15, relief = tk.GROOVE, bd = 3).pack(padx = 50, pady = 15)
        tk.Button(self, text = 'Add account', font = ('Arial', 18, 'bold'), command = lambda: master.switch_frame(AddAccount), width = 15, relief = tk.GROOVE, bd = 3).pack(padx = 50, pady = 15)
        tk.Button(self, text = 'Delete', font = ('Arial', 18, 'bold'), command = self.delete, width = 15, relief = tk.GROOVE, bd = 3).pack(padx = 50, pady = 15)
        #----------------
        self.get_accounts()
    

    def get_accounts(self):
        self.data = self.master.database.read('accounts')
        for record in self.data:
            self.listbox.insert(tk.END, '{}'.format(record[2]))


    def confirm(self):
        global index
        try:
            index = self.listbox.curselection()[0]
        except:
            self.master.switch_frame(Login)
            return
        login = AutoLogin('password.png', self.data[index][0], self.data[index][1])
        login.login()

    
    def view_info(self):
        global index
        try:
            index = self.listbox.curselection()[0]
        except:
            self.master.switch_frame(Login)
            return
        self.master.switch_frame(ShowInfo)
        

    def delete(self):
        global index
        try:
            index = self.listbox.curselection()[0]
        except:
            self.master.switch_frame(Login)
            return
        del self.data[index]
        self.master.database.wipe('accounts')
        for record in self.data:
            self.master.database.write('accounts', record)
        self.master.switch_frame(Login)



class AddAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text = 'Add an account', font = ('Arial', 30, 'bold')).pack(pady = 10)

        info = tk.Frame(self, bd = 2, relief = tk.GROOVE)
        info.pack()
        tk.Label(info, text = 'Username', font = ('Arial', 20, 'bold')).grid(row = 0, column = 0)
        tk.Label(info, text = 'Password', font = ('Arial', 20, 'bold')).grid(row = 1, column = 0)
        tk.Label(info, text = 'IGN', font = ('Arial', 20, 'bold')).grid(row = 2, column = 0)
        self.username = tk.Entry(info, font = ('Arial', 18, 'bold'), width = 20)
        self.username.grid(row = 0, column = 1, padx = 5)
        self.password = tk.Entry(info, font = ('Arial', 18, 'bold'), width = 20)
        self.password.grid(row = 1, column = 1, padx = 5)
        self.ign = tk.Entry(info, font = ('Arial', 18, 'bold'), width = 20)
        self.ign.grid(row = 2, column = 1, padx = 5)

        tk.Button(self, text = 'Confirm', font = ('Arial', 18, 'bold'), command = self.confirm, width = 15, relief = tk.GROOVE, bd = 3).pack()
        tk.Button(self, text = 'Back', font = ('Arial', 18, 'bold'), command = lambda: master.switch_frame(Login), width = 15, relief = tk.GROOVE, bd = 3).pack()

    
    def confirm(self):
        username = self.username.get()
        password = self.password.get()
        ign = self.ign.get()

        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.ign.delete(0, tk.END)

        db = Connection('database.db')
        db.write('accounts', (username, password, ign))



class ShowInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        
        tk.Label(self, text = 'Account info', font = ('Arial', 30, 'bold')).pack(pady = 30)

        content = tk.Frame(self, bd = 2, relief = tk.GROOVE)
        content.pack()
        tk.Label(content, text = 'Username', font = ('Arial', 20, 'bold')).grid(row = 0, column = 0, padx = 5)
        self.user = tk.Entry(content, font = ('Arial', 18, 'bold'))
        self.user.grid(row = 0, column = 1, padx = 5)
        tk.Label(content, text = 'Password', font = ('Arial', 20, 'bold')).grid(row = 1, column = 0, padx = 5)
        self.passw = tk.Entry(content, font = ('Arial', 18, 'bold'))
        self.passw.grid(row = 1, column = 1, padx = 5)
        tk.Label(content, text = 'IGN', font = ('Arial', 20, 'bold')).grid(row = 2, column = 0, padx = 5)
        self.ig = tk.Entry(content, font = ('Arial', 18, 'bold'))
        self.ig.grid(row = 2, column = 1, padx = 5)
        self.get_info()
        
        tk.Button(self, text = 'Copy', font = ('Arial', 18, 'bold'), command = self.copy, width = 15, relief = tk.GROOVE, bd = 3).pack()
        tk.Button(self, text = 'Back', font = ('Arial', 18, 'bold'), command = lambda: master.switch_frame(Login), width = 15, relief = tk.GROOVE, bd = 3).pack()

    
    def get_info(self):
        global index
        self.info = self.master.database.read('accounts')[index]
        self.username, self.password, self.ign = self.info

        self.user.delete(0, tk.END)
        self.user.insert(0, self.username)
        self.passw.delete(0, tk.END)
        self.passw.insert(0, self.password)
        self.ig.delete(0, tk.END)
        self.ig.insert(0, self.ign)

    
    def copy(self):
        string = 'username: {}\npassword: {}\nign: {}'.format(self.username, self.password, self.ign)
        pyperclip.copy(string)



if __name__ == '__main__':
    Main().mainloop()