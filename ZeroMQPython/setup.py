from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages=["Model.clsModel"])

exe = [Executable("dolphinCLI.py")]  # 2

# 3
setup(
    name="Example",
    version="1.0",
    author="Hyvision",
    description="Hyvision",
    options=dict(build_exe = buildOptions),
    executables=exe
)
