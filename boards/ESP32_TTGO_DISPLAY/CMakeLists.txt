cmake_minimum_required(VERSION 3.16)

# Your path to where you have micropython.
get_filename_component(PROJECT_DIR "../.." ABSOLUTE)
set(MICROPY_PORT_DIR ${PROJECT_DIR}/extern/micropython/ports/esp32)
get_filename_component(MICROPY_BOARD_DIR "." ABSOLUTE)

set(MICROPY_HW_BOARD_NAME "Lilygo TTGO T-Display")

# The "common" files that are still in top level camkefiles in micropython
include(../mpy.esp32.common2.cmake)

# We can't "include" a project() call, it has to be in this file.
project(micropython)