# pyscript - Automation tool for Windows
This project is written in Python 3.10.4


## Requirements
- Python 3.10.4 (any other Version should work as long as you get all the requirements)
- numpy
- bezier ([Troubleshoot](https://github.com/dhermes/bezier/issues/277))
- pywin32 (includes win32gui, win32api, win32com)
```cmd
python -m pip install numpy
python -m pip install scipy
python -m pip install pywin32
python -m pip install Pillow-PIL
python -m pip install pynput
```

# Documentation (more comming soon...)

## Mouse class

Return current mouse position on screen, for debugging purposes
```python
def getMousePos(self):
```

Left click
```python
m = Mouse() #needs to be initialized once
m.left()
```

Right click
```python
m.right()
```

```python
m.bez(200, 200)
m.left()
```

Moves mouse to a random point within rectangle, using benzier curve
```python
def moveToSquare(self, x, y, x2, y2):
```

Instantly moves cursor to given position
```python
def moveTo(self, x, y):
```

Checking wether a certain is pixel is found at given position
returns True or False
```python
def isColorAt(self, pos, RGB):
```

Returns RGB of pixel found at given position
```python
def getPixel(self, pos, type=""):
```

## Core class

Random sleep timer
```python
def rnd(lower=0, upper=5000):
```

## Window class

Returns mouse position within the chosen window
```python
def getMouseInWindow(self):
```

