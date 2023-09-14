from setuptools import setup, find_packages
import glob

setup(
    name="zpdb",
    version="1.0.3",
    author="YiMing Liu",
    author_email="letusgo126@126.com",
    url="https://github.com/LYMDLUT/zpdb",
    # keywords=("pytorch", "vehicle", "ReID"),
    description="Python debug configuration generator for vscode",
    scripts=glob.glob('scripts/*'),
    install_requires=["jstyleson"],
    # long_description="",
    packages=find_packages(exclude=('examples', 'examples.*')),
)
