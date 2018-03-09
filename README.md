[ ![Download](https://api.bintray.com/packages/DEGoodmanWilson/public-conan/base64%3ADEGoodmanWilson/images/download.svg) ](https://bintray.com/DEGoodmanWilson/public-conan/base64%3ADEGoodmanWilson/_latestVersion)
[![Build Status](https://travis-ci.org/DEGoodmanWilson/conan-base64.svg?branch=stable%2F1.0.2)](https://travis-ci.org/DEGoodmanWilson/conan-base64)
[![Build status](https://ci.appveyor.com/api/projects/status/sxs9n6vb8nqa92l5?svg=true)](https://ci.appveyor.com/project/DEGoodmanWilson/conan-base64)

[Conan.io](https://conan.io) package for the [base64](https://github.com/DEGoodmanWilson/base64) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/DEGoodmanWilson/public-conan/base64%3ADEGoodmanWilson).

## For Users: Use this package

### Basic setup

    $ conan install base64/1.0.2@DEGoodmanWilson/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    base64/1.0.2@DEGoodmanWilson/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to DEGoodmanWilson conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Issues

All issues, such as feature request, bug, support or discussion are centralized on Community repository. If you are interested to open a new issue, please visit https://github.com/DEGoodmanWilson/community/issues.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create DEGoodmanWilson/stable

## Add Remote

    $ conan remote add DEGoodmanWilson "https://api.bintray.com/conan/DEGoodmanWilson/public-conan"

## Upload

    $ conan upload base64/1.0.2@DEGoodmanWilson/stable --all -r DEGoodmanWilson

## License
[MIT](LICENSE)
