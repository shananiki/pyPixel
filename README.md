# pyscript - Automation tool for Windows
This project is written in Python 3.10.4

Major space for code improvement, but I'm still building so I don't tidy up just yet.


## Requirements
```cmd
python -m pip install numpy
python -m pip install scipy
python -m pip install pywin32
python -m pip install Pillow-PIL
python -m pip install pynput
```

# Documentation (more comming soon...)

## Interface class

Contains rectangle for Inventory icon
```python
self.INVENTORY_POS
```

Returns True if the inventory is open
```python
def isInventoryOpen(self):
```

Opens the inventory if closed
```python
def openInventory(self):
```

## Inventory class

Contains x and y coordinates for all 28 inventory spots
```python
self.INVENTORY_POS
```

Drops all inventory items
```python
def drop_all(self):
```

Drops all inventory items exceptions given in tuple
```python
def drop_all_except(self, exceptions):
```

Drops item at position n (1-28)
```python
def drop_item(self, n):
```

Return True if the Inventory is full
```python
def isInventoryFull(self):
```

## Mouse class

Return current mouse position on screen, for debugging purposes
```python
def getMousePos(self):
```

Left click
```python
def left(self):
```

Right click
```python
def right(self):
```

Moves mouse to given point within the window rectangle using a benzier curve
```python
m.bez_w(self, x, y):
```

Moves mouse to given point (whole screen) using a benzier curve
```python
m.bez(self, x, y):
```

Moves mouse to a random point within rectangle, using benzier curve
```python
def moveToSquare(self, x, y, x2, y2):
def moveToSquare_r(self, rect):
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



