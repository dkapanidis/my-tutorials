# Jupyter

Start

```sh
$ docker compose up
[+] Running 1/1
 ⠿ Container day01-notebook-1
Attaching to day01-notebook-1
day01-notebook-1  | Executing the command: jupyter lab
day01-notebook-1  | [I 2021-12-17 16:31:27.582 ServerApp] jupyterlab | extension was successfully linked.
day01-notebook-1  | [W 2021-12-17 16:31:27.587 NotebookApp] 'ip' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
day01-notebook-1  | [W 2021-12-17 16:31:27.587 NotebookApp] 'port' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
day01-notebook-1  | [W 2021-12-17 16:31:27.588 NotebookApp] 'port' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
day01-notebook-1  | [I 2021-12-17 16:31:27.599 ServerApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/jupyter_cookie_secret
day01-notebook-1  | [I 2021-12-17 16:31:27.789 ServerApp] nbclassic | extension was successfully linked.
day01-notebook-1  | [I 2021-12-17 16:31:27.836 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.9/site-packages/jupyterlab
day01-notebook-1  | [I 2021-12-17 16:31:27.837 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
day01-notebook-1  | [I 2021-12-17 16:31:27.844 ServerApp] jupyterlab | extension was successfully loaded.
day01-notebook-1  | [I 2021-12-17 16:31:27.857 ServerApp] nbclassic | extension was successfully loaded.
day01-notebook-1  | [I 2021-12-17 16:31:27.862 ServerApp] Serving notebooks from local directory: /home/jovyan
day01-notebook-1  | [I 2021-12-17 16:31:27.862 ServerApp] Jupyter Server 1.8.0 is running at:
day01-notebook-1  | [I 2021-12-17 16:31:27.862 ServerApp] http://d680e93ed800:8888/lab?token=32d00e72097c81d160d42b52f32039ecd855631d21350324
day01-notebook-1  | [I 2021-12-17 16:31:27.862 ServerApp]     http://127.0.0.1:8888/lab?token=32d00e72097c81d160d42b52f32039ecd855631d21350324
day01-notebook-1  | [I 2021-12-17 16:31:27.863 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
day01-notebook-1  | [C 2021-12-17 16:31:27.868 ServerApp]
day01-notebook-1  |
day01-notebook-1  |     To access the server, open this file in a browser:
day01-notebook-1  |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-8-open.html
day01-notebook-1  |     Or copy and paste one of these URLs:
day01-notebook-1  |         http://d680e93ed800:8888/lab?token=32d00e72097c81d160d42b52f32039ecd855631d21350324
day01-notebook-1  |         http://127.0.0.1:8888/lab?token=32d00e72097c81d160d42b52f32039ecd855631d21350324
```

To access the server open the last link on the logs in a browser.