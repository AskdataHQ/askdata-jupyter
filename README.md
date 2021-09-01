# Askdata for Jupyter notebook
### A proof-of-concept jupyter extension which converts english queries into relevant python code. 

![](jupyter-askdata-demo.gif)

## Supported Operating Systems:
- Ubuntu
- macOS

#### CPU-only install:
For Mac and other Ubuntu installations not having a nvidia GPU, we need to explicitly set an environment variable at time of install.
```
export JUPYTER_ASKDATA_MODE="cpu"

```

#### Installation commands:

```
git clone https://github.com/askdataHQ/jupyter-askdata.git
cd jupyter-askdata
pip install .
jupyter nbextension enable jupyter-askdata/main

```

## Uninstallation:
```
pip uninstall jupyter-askdata
```

## Usage Instructions:

- Start Jupyter notebook server by running the following command: ``` jupyter notebook ```
- If you don't see ``` Nbextensions```  tab in Jupyter notebook run the following command:``` jupyter contrib nbextension install --user ```
- You can open the sample ``` notebooks/ctds.ipynb```  notebook for testing
- Click on the `Terminal` Icon which appears on the menu (to activate the extension)
- Type "help" to see a list of currently supported commands in the repo
