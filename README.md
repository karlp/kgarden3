# Obsolete
Decided to just keep this all in the [ktwinkler repo](https://github.com/karlp/ktwinkler/), where most of the hardware is already anyway.

At least we used this to update our micropython custom board setups :)

# Original below...

# Karl's Garden v something or other
Repo for hardware, software and scribble related to (mostly) garden decorations for halloween


# Building for the custom board
```
podman run --rm --device /dev/ttyUSB0 -v .:/project:Z -w /project/boards/ESP32_CUSTOM -e HOME=/tmp espressif/idf:v5.5.4 idf.py -b 921600 build erase-flash flash
```



# (notes) running a clean mpy build once
```
git submodule update --init lib/micropython-lib lib/berkeley-db-1.xx
podman run --rm --device /dev/ttyUSB0 -v .:/project:Z -w /project/ports/esp32 -e HOME=/tmp espressif/idf:v5.5.4 idf.py -b 921600 build erase-flash flash
```

Had to split the erase-flash and flash for that mosx4 board, it has a shitty reset handling, but otherwise, you're good here
