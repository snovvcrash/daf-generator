# DAF Gen
Simple Delayed Auditory Feedback (DAF) generator aimed at reducing stuttering.

## Screenshot
![alt text](https://user-images.githubusercontent.com/23141800/35464372-9d59553e-0306-11e8-945c-26535601f002.png)

## Building and requirements
DAF Gen is created via PyQt5 framework and uses the PyAudio module for voice recording. All the necessary dependencies are listed in *requirements.txt*.

Build and run (on Windows machine):
```
> python3 -m pip install -r requirements.txt
> python3 dafgen.py
```
You can edit the Ui (*dafgen.ui*) with PyQt Designer as you like.

Also it may be convenient to freeze the code into standalone executable. This could be done with cx_Freeze:
```
> python3 setup.py build
```

## Platform
DAF Gen is developed and tested on Windows, but it is runnable on Linux systems as well. In this case you should manually dependencies first:
```
$ pip3 install pyaudio
$ sudo apt-get install python3-pyqt5 pyqt5-dev-tools
```

## Help
If you have any questions, feel free to contact me at <snovvcrash@protonmail.com>.
