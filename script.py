from cx_Freeze import setup, Executable
import sys

base = "Win32GUI"
if sys.platform == 'Win32':
	base = "Win32GUI"
	
executables = [Executable("Main.py", base = base, icon="Img/GameIcon.ico")]

packages = ["pygame","pygame_menu","sys"]
excludes = ["tkinter", "PyQt5", "pytz", "pyperclip", "numpy", "logging", "multiprocessing",\
 "json", "urllib", "setuptools", "asyncio", "concurrent", "ctypes", "distutils", "email", "html", "http", "lib2to3", "pkg_resources", "pydoc_data"]
includes_file = ["Img","Sound"]

options = {'build_exe': {'packages':packages, 'excludes': excludes, 'include_files': includes_file},}

setup(name = "ZombieGame", options = options, vesion ="0.5.0", executables = executables)