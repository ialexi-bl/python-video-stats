# Video stats

Small application that extracts some information about videos into an Excel spreadsheet. Was created for [NTI](https://nti-contest.ru/) contest.
Written in python 3 (tested on versions 3.7 and 3.8).

## Extracted data

- File size
- Duration
- Dimensions and aspect ratio
- Creation date
- FPS
- Audio bitrate
- Amount of audio channels
- Sampling rate

![Table example](/assets/table.png)


## Local testing

Run `main.py` with `python3 main.py` or `python main.py`

## Building and launching

You can build this application locally using

```
python -m PyInstaller -c --add-data "./src/lib/*;./src/lib/" main.py
```

You must have `PyInstaller` installed (`pip install PyInstaller`).

To launch application, open `main.exe` file in `dist/main` folder. This application only works on Windows platforms.
