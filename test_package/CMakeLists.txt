project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
conan_define_targets()

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5Core REQUIRED)
#find_package(zlib REQUIRED)
#find_package(quazip REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example CONAN_PKG::quazip Qt5::Core)
#target_link_libraries(example ${zlib_LIBRARIES} ${quazip_LIBRARIES} Qt5::Core)
#target_include_directories(example PUBLIC 
#    ${zlib_INCLUDE_DIRS}
#    ${quazip_INCLUDE_DIRS}
#)
