# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release

# Include any dependencies generated for this target.
include sample/CMakeFiles/SamplePointcloud.dir/depend.make

# Include the progress variables for this target.
include sample/CMakeFiles/SamplePointcloud.dir/progress.make

# Include the compile flags for this target's objects.
include sample/CMakeFiles/SamplePointcloud.dir/flags.make

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o: sample/CMakeFiles/SamplePointcloud.dir/flags.make
sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o: ../../sample/SamplePointcloud.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o -c /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/SamplePointcloud.cpp

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.i"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/SamplePointcloud.cpp > CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.i

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.s"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/SamplePointcloud.cpp -o CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.s

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.requires:
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.requires

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.provides: sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.requires
	$(MAKE) -f sample/CMakeFiles/SamplePointcloud.dir/build.make sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.provides.build
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.provides

sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.provides.build: sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o

# Object files for target SamplePointcloud
SamplePointcloud_OBJECTS = \
"CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o"

# External object files for target SamplePointcloud
SamplePointcloud_EXTERNAL_OBJECTS =

sample/samplepointcloud: sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o
sample/samplepointcloud: sample/CMakeFiles/SamplePointcloud.dir/build.make
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_core.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_calib3d.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_features2d.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_flann.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_highgui.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_imgproc.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_legacy.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_ml.so
sample/samplepointcloud: /home/nick/Documents/RedhawkQuad/Groundstation/Linux/opencv/lib/libopencv_video.so
sample/samplepointcloud: ../../bin/libalvar200.so
sample/samplepointcloud: ../../bin/libalvarplatform200.so
sample/samplepointcloud: sample/libSharedSamples.a
sample/samplepointcloud: sample/libSharedGlutViewer.a
sample/samplepointcloud: /usr/lib/libGLU.so
sample/samplepointcloud: /usr/lib/libGL.so
sample/samplepointcloud: /usr/lib/libglut.so
sample/samplepointcloud: sample/CMakeFiles/SamplePointcloud.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable samplepointcloud"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SamplePointcloud.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sample/CMakeFiles/SamplePointcloud.dir/build: sample/samplepointcloud
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/build

sample/CMakeFiles/SamplePointcloud.dir/requires: sample/CMakeFiles/SamplePointcloud.dir/SamplePointcloud.cpp.o.requires
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/requires

sample/CMakeFiles/SamplePointcloud.dir/clean:
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && $(CMAKE_COMMAND) -P CMakeFiles/SamplePointcloud.dir/cmake_clean.cmake
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/clean

sample/CMakeFiles/SamplePointcloud.dir/depend:
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample/CMakeFiles/SamplePointcloud.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sample/CMakeFiles/SamplePointcloud.dir/depend
