add_executable(${PROJECT_NAME}_tests
	main.cpp
    basic_functioning.cpp
    ${PROJECT_SOURCE_DIR}/base64.cpp
    ${PROJECT_SOURCE_DIR}/base64.h
    )

target_link_libraries(${PROJECT_NAME}_tests ${CONAN_LIBS})