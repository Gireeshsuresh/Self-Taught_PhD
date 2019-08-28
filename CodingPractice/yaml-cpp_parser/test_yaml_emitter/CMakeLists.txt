
project(emit2File CXX)

cmake_minimum_required(VERSION 3.10)
add_definitions(-O3)

# ==============================================================================
# INCLUDES
# ==============================================================================
include_directories(/usr/local/include)


# ==============================================================================
# LIBRARIES
# ==============================================================================
set(USR_LOCAL_LIB /usr/local/lib)
link_directories(${USR_LOCAL_LIB})


# ==============================================================================
# EXECUTABLE
# ==============================================================================
add_executable(${PROJECT_NAME}
               emit2File.cpp
)
target_link_libraries(${PROJECT_NAME} PUBLIC yaml-cpp )