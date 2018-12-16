project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()
#conan_define_targets()

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5Core REQUIRED)
find_package(zlib REQUIRED)
find_package(quazip REQUIRED)

set(CMAKE_MACOSX_RPATH ON)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_INSTALL_RPATH "@loader_path;@executable_path")

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/bin)

add_definitions(-DUNICODE=TRUE)
add_definitions(-D_UNICODE=TRUE)
add_executable(example example.cpp)
#target_link_libraries(example CONAN_PKG::quazip Qt5::Core)
target_link_libraries(example ${zlib_LIBRARIES} ${quazip_LIBRARIES} Qt5::Core)
target_include_directories(example PUBLIC
    ${zlib_INCLUDE_DIRS}
    ${quazip_INCLUDE_DIRS}
)
