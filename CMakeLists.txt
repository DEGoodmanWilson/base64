cmake_minimum_required(VERSION 3.6)
project(base64)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

##### External dependencies

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

##### Options

macro(base64_option OPTION_NAME OPTION_TEXT OPTION_DEFAULT)
    option(${OPTION_NAME} ${OPTION_TEXT} ${OPTION_DEFAULT})
    if(DEFINED ENV{${OPTION_NAME}})
        # Allow setting the option through an environment variable
        set(${OPTION_NAME} $ENV{${OPTION_NAME}})
    endif()
    if(${OPTION_NAME})
        add_definitions(-D${OPTION_NAME})
    endif()
    message(STATUS "  ${OPTION_NAME}: ${${OPTION_NAME}}")
endmacro()

message(STATUS "Base64 CMake Options")
message(STATUS "=======================================================")
base64_option(BUILD_BASE64_TESTS    "Build the test suite"           OFF)
message(STATUS "=======================================================")

if (BUILD_BASE64_TESTS)
    message(STATUS "Building Base64 with Tests")
    add_subdirectory(tests)
endif ()

set(SOURCE_FILES base64.cpp base64.h)
add_library(base64 ${SOURCE_FILES})