# VSCode Based Development Environment With Docker
This repository provides `python3` setup for Python3 based development.

## Pre-Requisites
1. [Visual Studio Code](https://code.visualstudio.com)
2. Visual Studio Code plugin [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Docker with access to internet.

## Tools on Host Machine.
| Tool |   Version Used |
| ---:          |     :---      |
| Operating System | Linux Mint 20.0 (Based on Ubuntu 20.04/focal)
| Docker*         | 20.10.2, build 2291f61 |

## Inside The Docker Container.
| Artifact |   Version Provided |
| ---:          |     :---      |
| Python3 | 3.8.5
| ipython3         | 7.13.0 |
| pip3             | 20.0.2 |
| jupyter core     | 4.6.3 |
| jupyter-notebook | 6.0.3 |
| qtconsole        | not installed |
| ipython          | 7.13.0 |
| ipykernel        | 5.2.0 |
| jupyter client   | 6.1.2 |
| jupyter lab      | not installed |
| nbconvert        | 5.6.1 |
| ipywidgets       | 6.0.0 |
| nbformat         | 5.0.4 |
| traitlets        | 4.3.3 |
## Included
1. Necessary `Dockerfile` required to build a container.
1. Preconfigured `.devcontainer.json` inside `.devcontainer` folder with necessary `vscode` extensions,
1. Preconfigured `launch.json` to launch a debugger. The debugger by default will is setup to enter `src/test.py` file.
1. Preconfigured `tasks.json` with helpful shortcuts. `Ctrl+Shift+B` to see the available shortcuts.

    a. A shortcut to launch `ipython` interactive session in the host-browser is included.
1. A `ipython` style cell is formed if a line starts with `# %%%`. See `src/test.py` for example. If a debugger is invoked on such a file, a preview pane is automatically opened in `vscode` showing the result, e.g., a plot.

## How To Use
1. Ensure pre-requisites are met,
2. Clone this repository,
3. Open Visual Studio Code, Run the Remote-Containers: `Open Folder in Container...` command and select the folder where (the master branch of) this repository is cloned.
   1. See [this link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for more help.
4. VSCode will attempt to build the container based on the provided [Dockerfile](./.devcontainer/Dockerfile) automatically.
5. On success, `Ctrl+Shift+B` will bring a menu of possible build choices that may be selected from.
