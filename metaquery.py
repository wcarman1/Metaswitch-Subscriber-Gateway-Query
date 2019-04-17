import Tkinter as tk
import ttk
import tkMessageBox as messagebox
import psycopg2


MetaIp = 'ip of your switch'
DbName = 'shadow_config_db'
DbUser = 'shadowconfigread'
DbPass = 'db password'


class StartUp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, 'icon.ico')
        tk.Tk.wm_title(self, "MetaSwitch Subscriber Gateway Query")
        tk.Tk.wm_resizable(self, width=False, height=False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def mc(event=None):
    try:
        if len(inputMac.get()) < 11:
            List.delete(0, tk.END)
            List.insert(tk.END, "Mac Address must be at least 11 characters long. '-' count as characters")
            return
        if not():
            global conn1
            conn1 = psycopg2.connect(
                "dbname=%s user=%s host=%s password=%s" % (DbName, DbUser, MetaIp, DbPass))
            global cur1
            cur1 = conn1.cursor()
            mac = inputMac.get()
            stmt = """SELECT 'Subscriber Gateway ' || BaseInformation_Description AS match, BaseInformation_DomainName AS 
                domain_name FROM  Meta_SubG WHERE BaseInformation_DomainName LIKE UPPER(%s)"""
            cur1.execute(stmt, ('%' + mac + '%',))
            List.delete(0, tk.END)
            rows = cur1.fetchall()
            if cur1.rowcount:
                for row in rows:
                    List.insert(tk.END, row[0] + '   ' + row[1])
            else:
                stm = """SELECT 'Subscriber Gateway ' || BaseInformation_Description AS match, BaseInformation_DomainName AS 
                    domain_name FROM  Meta_SubG WHERE BaseInformation_DomainName LIKE LOWER(%s)"""
                cur1.execute(stm, ('%' + mac + '%',))
                List.delete(0, tk.END)
                rows = cur1.fetchall()
                if not cur1.rowcount:
                        messagebox.showinfo("Info", "Query returned no data")
                else:
                    for row in rows:
                        List.insert(tk.END, row[0] + '   ' + row[1])
    except psycopg2.Error:
        messagebox.showwarning("Error", "Could not connect to MetaSwitch")
        if conn1:
            conn1.rollback()

    cur1.close()
    conn1.close()


def ip(event=None):
    try:
        if len(inputIP.get()) < 4:
            list1.delete(0, tk.END)
            list1.insert(tk.END, "IP Address must be at least 4 characters long. '.' count as characters")
            return
        if not ():
            global conn
            conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s" % (DbName, DbUser, MetaIp, DbPass))
            global cur
            cur = conn.cursor()
            ipadd = inputIP.get()
            stmt = """SELECT 'Subscriber Gateway ' || BaseInformation_Description AS match,
                    BaseInformation_IPAddress AS ip_address FROM  Meta_SubG WHERE BaseInformation_IPAddress LIKE(%s)"""
            cur.execute(stmt, ('%' + ipadd + '%',))
            list1.delete(0, tk.END)
            rows = cur.fetchall()
            if not cur.rowcount:
                messagebox.showinfo("Info", "Query returned no data")
            else:
                for row in rows:
                    list1.insert(tk.END, row[0] + '   ' + row[1])
    except psycopg2.Error:
        messagebox.showerror("Error", "Could not connect to MetaSwitch")
        if conn:
            conn.rollback()

    cur.close()
    conn.close()


def clear():
    inputMac.delete(0, tk.END)
    List.delete(0, tk.END)


def clear2():
    inputIP.delete(0, tk.END)
    list1.delete(0, tk.END)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button3 = ttk.Button(self, text="Search by IP Address", command=lambda: controller.show_frame(PageOne))
        button3.pack(pady=10)
        label = tk.Label(self, text="Enter the Mac Address in XX-XX-XX-XX-XX-XX format:")
        label.pack(pady=3, padx=100)
        global inputMac
        inputMac = tk.Entry(self)
        inputMac.pack(pady=5)
        inputMac.focus()
        button1 = ttk.Button(self, text="Search", command=mc)
        inputMac.bind("<Return>", mc)
        global List
        List = tk.Listbox(self)
        List.config(width=75, height=10, selectmode="extended")
        List.pack()
        scrollbar = tk.Scrollbar(self)
        List.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=List.yview)
        button2 = ttk.Button(self, text="Clear All", command=clear)
        button1.pack(pady=3, padx=10, side="right")
        button2.pack(side="right")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button3 = ttk.Button(self, text="Search by Mac Address", command=lambda: controller.show_frame(StartPage))
        button3.pack(pady=10)
        label = tk.Label(self, text="Enter the IP Address in XXX.XXX.XXX.XXX format:")
        label.pack(pady=3, padx=100)
        global inputIP
        inputIP = tk.Entry(self)
        inputIP.pack(pady=5)
        inputIP.focus()
        button1 = ttk.Button(self, text="Search", command=ip)
        inputIP.bind("<Return>", ip)
        global list1
        list1 = tk.Listbox(self)
        list1.config(width=75, height=10, selectmode="extended")
        list1.pack()
        scrollbar = tk.Scrollbar(self)
        list1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=list1.yview)
        button2 = ttk.Button(self, text="Clear All", command=clear2)
        button1.pack(pady=3, padx=10, side="right")
        button2.pack(side="right")


app = StartUp()
app.mainloop()
