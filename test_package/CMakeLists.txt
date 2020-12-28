cmake_minimum_required(VERSION 3.15)

project(CoroConanTestPackage CXX)

find_package(coro MODULE REQUIRED)

add_executable(CoroConanTestPackage
    CoroConanTestPackage.cpp)

set_property(GLOBAL
    PROPERTY
        CXX_STANDARD                20
        CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -v -std=c++20")

target_link_libraries(CoroConanTestPackage
    PRIVATE
        coro::coro)
