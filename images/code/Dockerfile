FROM codercom/code-server:4.8.3

RUN sudo apt-get update && sudo apt-get install python3 python3-pip -y
RUN pip install prometheus_client

RUN sudo mkdir /extensions

COPY ms-python.python-2022.16.1.vsix /extensions/ms-python.python-2022.16.1.vsix
RUN /usr/bin/code-server --install-extension /extensions/ms-python.python-2022.16.1.vsix

RUN sudo mkdir -p /prometheus/workspace
COPY test_server.py /prometheus/workspace/test_server.py
COPY .vscode/ /prometheus/workspace/.vscode/
RUN sudo chmod 777 -R /prometheus/workspace

COPY settings.json /home/coder/.local/share/code-server/User/settings.json
RUN sudo chmod 777 /home/coder/.local/share/code-server/User/settings.json
