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
include sample/CMakeFiles/SharedGlutViewer.dir/depend.make

# Include the progress variables for this target.
include sample/CMakeFiles/SharedGlutViewer.dir/progress.make

# Include the compile flags for this target's objects.
include sample/CMakeFiles/SharedGlutViewer.dir/flags.make

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o: sample/CMakeFiles/SharedGlutViewer.dir/flags.make
sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o: ../../sample/GlutViewer.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o -c /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/GlutViewer.cpp

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.i"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/GlutViewer.cpp > CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.i

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.s"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && /usr/bin/g++-4.4  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample/GlutViewer.cpp -o CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.s

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.requires:
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.requires

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.provides: sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.requires
	$(MAKE) -f sample/CMakeFiles/SharedGlutViewer.dir/build.make sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.provides.build
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.provides

sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.provides.build: sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o

# Object files for target SharedGlutViewer
SharedGlutViewer_OBJECTS = \
"CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o"

# External object files for target SharedGlutViewer
SharedGlutViewer_EXTERNAL_OBJECTS =

sample/libSharedGlutViewer.a: sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o
sample/libSharedGlutViewer.a: sample/CMakeFiles/SharedGlutViewer.dir/build.make
sample/libSharedGlutViewer.a: sample/CMakeFiles/SharedGlutViewer.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX static library libSharedGlutViewer.a"
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && $(CMAKE_COMMAND) -P CMakeFiles/SharedGlutViewer.dir/cmake_clean_target.cmake
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SharedGlutViewer.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sample/CMakeFiles/SharedGlutViewer.dir/build: sample/libSharedGlutViewer.a
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/build

sample/CMakeFiles/SharedGlutViewer.dir/requires: sample/CMakeFiles/SharedGlutViewer.dir/GlutViewer.cpp.o.requires
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/requires

sample/CMakeFiles/SharedGlutViewer.dir/clean:
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample && $(CMAKE_COMMAND) -P CMakeFiles/SharedGlutViewer.dir/cmake_clean.cmake
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/clean

sample/CMakeFiles/SharedGlutViewer.dir/depend:
	cd /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/sample /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample /home/nick/Documents/RedhawkQuad/Groundstation/Linux/alvar/build/build_gcc44_release/sample/CMakeFiles/SharedGlutViewer.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sample/CMakeFiles/SharedGlutViewer.dir/depend
