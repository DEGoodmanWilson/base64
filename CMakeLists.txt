cmake_minimum_required(VERSION 3.9)
set(PROJECT_NAME base64)
project(${PROJECT_NAME})

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

message(STATUS "${PROJECT_NAME} CMake Options")
message(STATUS "=======================================================")
base64_option(BUILD_SHARED          "Build a shared object"          OFF)
message(STATUS "=======================================================")

#### tests

enable_testing()
include_directories(SYSTEM PRIVATE .)
add_subdirectory(tests)

add_test(ALL_TESTS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}_tests)

#### library

set(SOURCE_FILES base64.cpp base64.h)

if (BUILD_SHARED)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
    add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})
    set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON) # This doesn't seem to be actually working…
else (BUILD_SHARED)
    add_library(${PROJECT_NAME} ${SOURCE_FILES})
endif (BUILD_SHARED)