import os
from glob import glob

import setuptools

INSTALL_LIBS = ['numpy<1.19.0', 'jupyter', 'askdata', 'jupyter_contrib_nbextensions', 'pandas']

def get_serverextension_files():
    data_files = []
    for f in glob('jupyter_text2code/jupyter_askdata_serverextension/**', recursive=True):
        if os.path.isfile(f):
            frags = f.split("/")[:-1]
            frags[0] = 'jupyter-askdata'
            relative_common_path = "/".join(frags)
            data_files.append((os.path.join("share/jupyter/nbextensions/", relative_common_path), [f]))
    return data_files


data_files = [
    ('share/jupyter/nbextensions/jupyter-askdata', [
        "jupyter_askdata/__init__.py",
        "jupyter_askdata/jupyter_askdata.yaml",
        "jupyter_askdata/main.js",
        "jupyter_askdata/jupyter_askdata.css",
        "jupyter_askdata/jupyter_askdata_lib.py"]),
    ('etc/jupyter/jupyter_notebook_config.d', ['jupyter_askdata/etc/jupyter-askdata-extension.json'])
]

data_files.extend(get_serverextension_files())

setuptools.setup(
    name="jupyter-askdata",
    version='0.0.1',
    url="https://github.com/askdataHQ/jupyter-askdata",
    author="Simone Di Somma",
    license="MIT License",
    description="Jupyter server extension to assist with data science",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_LIBS,
    python_requires='>=3.7',
    classifiers=[
        'Framework :: Jupyter',
    ],
    data_files=data_files,
    include_package_data=True,
    zip_safe=False
)
