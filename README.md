# DAF Gen
Simple DAF (***D**elayed **A**uditory **F**eedback*) generator aimed at reducing stuttering.

## Screenshot
![Screenshot-1](https://user-images.githubusercontent.com/23141800/35464372-9d59553e-0306-11e8-945c-26535601f002.png)

## Background
What's this all about:
  * [Delayed Auditory Feedback - Wikipedia](https://en.wikipedia.org/wiki/Delayed_Auditory_Feedback)
  * [Delayed Auditory Feedback - Wikibooks](https://en.wikibooks.org/wiki/Speech-Language_Pathology/Stuttering/Delayed_Auditory_Feedback)
  * [На волнах эффекта Ли: Питонизируем генерацию DAF / Хабр](https://habr.com/post/347580/)

## Building and requirements
DAF Gen is created via PyQt5 framework and uses the PyAudio module for voice recording. All the necessary PIP dependencies are listed in *requirements.txt*.

Build and run (on Windows machine):
```
> python3 -m pip install -r requirements.txt
> python3 dafgen.py
```
You can edit the Ui (*dafgen.ui*) with PyQt Designer as you like.

Also it may be convenient to freeze the code into standalone executable. This could be done with *cx_Freeze*:
```
> python3 setup.py build
```

## Platform
DAF Gen is developed and tested on Windows, but it is runnable on Linux systems as well. In this case you should manually resolve DEB dependencies first:
```
$ pip3 install pyaudio
$ sudo apt-get install python3-pyqt5 pyqt5-dev-tools
```
