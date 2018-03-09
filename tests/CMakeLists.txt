add_executable(${PROJECT_NAME}_tests
	main.cpp
    basic_functioning.cpp
    ${PROJECT_SOURCE_DIR}/base64.cpp
    ${PROJECT_SOURCE_DIR}/base64.h
    )

target_link_libraries(base64_tests ${CONAN_LIBS})