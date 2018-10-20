#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
	"packages": ["os"],
	"excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(
	name = "dafgen",
	version = "0.1",
	description = "A DAF Generator tool",
	options = {"build_exe": build_exe_options},
	executables = [Executable("dafgen.py", base=base)]
)
