# bottle-word

This is quite a painful challenge...

<br\>

The premise is as follows; create a way for a 3d printer to automatically play wordscapes with a stylus.

## The plan

The problem can be broken down into the following stages

1. Get the screenshot
2. Character recognition and locating on the screen
3. Generate word lists
4. Translate the words to gcode
5. Send to the printer


## Problems

### Step 1

Enable dev mode on the phone, enable usb debugging, plug in to laptop and use adb...

```
adb exec-out screencap screenshot.png
```

This command is done with the pure-python-adb package

### Step 2

- OpenCV
    - OpenCV is used to pinpoint each individual character while simultaneously getting their location on the image

- Tesseract sucks
    - Otsu's binarisation, greyscale images and other image processing with opencv may be required
    - Tesseract might have to be in page mode 10 for single character recognition, but this is dodgy
    - An alternative to tesseract is to use opencv and xor each located letter with the corresponding letter in a folder of images

- Screenshot resolution
    - Thinking forward, it would be useful to know the screenshot resolution, and take the wheel from the bottom, so it can later be translated more easily into gcode

- Colours
    - Wordscapes has the cheek to change the colour of the wheel sometimes
    - Play on visually impaired mode to avoid the transparency
