# mitre4havoc

This plugin adds a TreeView to the Havoc UI that displays all MITRE enterprise tactics, techniques and sub-techniques in an ordered fashion. This repository also includes `parse_mitre.py`, a tool that fetches the current TTPs directly from the MITRE framework and stores them in a JSON file, which is then used by the plugin.

## Setup & Usage
After cloning the repository, it is first necessary to fetch the MITRE data by running the following command. After completion, the script will have created tactics.json in the `/tmp` directory. The script requires the python `bs4` and `requests` packages, which can be installed with pip.

```
pip3 install bs4
pip3 install requests

python3 parse_mitre.py
```
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/fbceccf7-18c9-401b-abd5-6d1ffab830d2)


To load the plugin into Havoc, click on **Scripts**, then **Script Manager** and **Load Script**. Select the `mitre4havoc.py` file in the opened dialog. Afterwards, a new tab called *MITRE* should appear in the menu bar at the top. Click on it and select **Open view** to open the MITRE tree view.  
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/e71ce2d0-7260-42ab-80eb-cffa7b26e81f)
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/4e7cf341-09ba-4b27-a1a8-5a4950e9571e)

## Screenshots
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/b9bff740-5284-48ab-9b9d-dd6a79e19f55)
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/29cebe50-2c41-4cf6-a063-4e23434e6e76)
![image](https://github.com/jakobfriedl/mitre4havoc/assets/71284620/7b029a01-2a6c-45fc-abdf-616cdea5ee1c)
