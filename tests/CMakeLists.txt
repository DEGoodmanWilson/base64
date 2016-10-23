cmake_minimum_required(VERSION 2.8)

enable_testing()

add_executable(base64_tests main.cpp
        basic_functioning.cpp
        )

target_link_libraries(base64_tests base64 ${CONAN_LIBS})

add_test(base64 ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/base64_tests)