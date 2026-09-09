# include default manifest
include("$(PORT_DIR)/boards/manifest.py")

# TODO - include your own extra shit here.
freeze("modules")
#module("tft_config.py", base_path="$(BOARD_DIR)/../../src")

# Add as many as you feel you need
module("vga1_16x16.py", base_path="$(BOARD_DIR)/../../extern/st7789_mpy/fonts/bitmap")
module("vga1_8x8.py", base_path="$(BOARD_DIR)/../../extern/st7789_mpy/fonts/bitmap")