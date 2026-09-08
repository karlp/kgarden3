cmake_minimum_required(VERSION 3.16)

get_filename_component(PROJECT_DIR "../.." ABSOLUTE)
set(MICROPY_PORT_DIR ${PROJECT_DIR}/extern/micropython/ports/esp32)
get_filename_component(MICROPY_BOARD_DIR "." ABSOLUTE)

#####
# Everything below here is copied from upstream, basically, just variants stripped out
# and lockfile comparisons stripped out
# We'd really like it to have more of it moved to esp32_common.cmake so we can include it easier...
# TODO: user frozen manifest?

# Define the output sdkconfig so it goes in the build directory.
set(SDKCONFIG ${CMAKE_BINARY_DIR}/sdkconfig)


# Include board config; this is expected to set SDKCONFIG_DEFAULTS (among other options).
include(${MICROPY_BOARD_DIR}/mpconfigboard.cmake)


# Concatenate all sdkconfig files into a combined one for the IDF to use.
file(WRITE ${CMAKE_BINARY_DIR}/sdkconfig.combined.in "")
foreach(SDKCONFIG_DEFAULT ${SDKCONFIG_DEFAULTS})
    file(READ ${SDKCONFIG_DEFAULT} CONTENTS)
    file(APPEND ${CMAKE_BINARY_DIR}/sdkconfig.combined.in "${CONTENTS}")
endforeach()
configure_file(${CMAKE_BINARY_DIR}/sdkconfig.combined.in ${CMAKE_BINARY_DIR}/sdkconfig.combined COPYONLY)
set(SDKCONFIG_DEFAULTS ${CMAKE_BINARY_DIR}/sdkconfig.combined)

# Include main IDF cmake file.
include($ENV{IDF_PATH}/tools/cmake/project.cmake)

# Generate individual dependencies.lock files based on chip target
# KARL - if we edit this, we dont' need to have a dummy file in lockfiles?
set(LOCKFILE_PATH lockfiles/dependencies.lock.${IDF_TARGET})
idf_build_set_property(DEPENDENCIES_LOCK ${LOCKFILE_PATH})

# Define the project.
project(micropython)