cmake_minimum_required(VERSION 2.8)
project(base64)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

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
base64_option(BUILD_SHARED          "Build a shared object"          OFF)
message(STATUS "=======================================================")

if (BUILD_BASE64_TESTS)
    message(STATUS "Building Base64 with Tests")
    add_subdirectory(tests)
endif ()

set(SOURCE_FILES base64.cpp base64.h)

if (BUILD_SHARED)
    set(CMAKE_MACOSX_RPATH ON)
    add_library(base64 SHARED ${SOURCE_FILES})
else (BUILD_SHARED)
    add_library(base64 ${SOURCE_FILES})
endif (BUILD_SHARED)
