import cx_Freeze
import sys
import psycopg2

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("metaquery.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "MetaSwitch Subscriber Gateway Query",
    options = {"build_exe": {"packages":["Tkinter","psycopg2"], "include_files":["icon.ico"]}},
    version = "1.0",
    description = "MetaSwitch Subscriber Gateway Query",
    executables = executables
    )