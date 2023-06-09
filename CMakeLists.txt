cmake_minimum_required(VERSION 3.12)

project(omnimapper)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++20 -pthread -O3 -Wall -Wextra -Wno-unused -pedantic")
set(CMAKE_CXX_STANDARD 20)

find_package(Python3 3.10 COMPONENTS Interpreter Development REQUIRED)

find_package(Boost COMPONENTS python${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR} REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

file(GLOB SRC_FILES src/*.cpp)
add_library(omnimappercpp MODULE ${SRC_FILES})
set_target_properties(omnimappercpp PROPERTIES PREFIX "") # Makes sure the python module is named xxx instead of libxxx on Linux

target_link_libraries(omnimappercpp ${Boost_LIBRARIES})
target_include_directories(omnimappercpp PRIVATE ${Python3_INCLUDE_DIRS})

if (DEV EQUAL "1")
	add_custom_command(TARGET omnimappercpp POST_BUILD 
		COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/cmake/write_timestamped_omnimappercpp.py
		ARGS $<TARGET_FILE_SUFFIX:omnimappercpp>
		WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
	)
	
	install(DIRECTORY ${CMAKE_BINARY_DIR}/timestamped/ DESTINATION .
		FILES_MATCHING PATTERN "omnimappercpp-t*"
	)
endif()

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
	execute_process(COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/cmake/blender_user_addon_path.py
		OUTPUT_VARIABLE BLENDER_ADDON_PATH 
		OUTPUT_STRIP_TRAILING_WHITESPACE
		COMMAND_ERROR_IS_FATAL ANY
	)
	set(CMAKE_INSTALL_PREFIX ${BLENDER_ADDON_PATH}/omnimapper CACHE PATH "install prefix" FORCE)
endif()

install(DIRECTORY py/ DESTINATION .)
install(TARGETS omnimappercpp DESTINATION .)
