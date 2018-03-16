cmake_minimum_required(VERSION 3.2)

project(base64)

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

##### External dependencies

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

#### base64

set(SOURCE_FILES base64.cpp base64.h)

add_library(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

#### tests

# enable_testing()
# include_directories(SYSTEM PRIVATE .)
# add_subdirectory(tests)

# add_test(ALL_TESTS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}_tests)
