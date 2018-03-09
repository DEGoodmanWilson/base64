cmake_minimum_required(VERSION 3.2)

##### Use C++14
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

project(base64)

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

##### External dependencies

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

#### tests

enable_testing()
include_directories(SYSTEM PRIVATE .)
add_subdirectory(tests)

add_test(ALL_TESTS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}_tests)

#### library

set(SOURCE_FILES base64.cpp base64.h)

add_library(${PROJECT_NAME} ${SOURCE_FILES})