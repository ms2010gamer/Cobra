workspace "cobra"
    startproject "cobraeditor"
    architecture "x64"

    configurations { "Debug", "Release" }

    filter "configurations:Debug"
        defines { "DEBUG" }
        flags { "Symbols" }

    filter "configurations:Release"
        defines { "NDEBUG" }
        optimize "On"
    
tdir = "bin/%{cfg.buildcfg}/%{prj.name}"
odir = "bin-obj/%{cfg.buildcfg}/%{prj.name}"

project "cobraeditor"
    location "cobraeditor"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"

    targetdir(tdir)
    objdir(odir)

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp",
    }

    flags
    {
        "FatalWarnings"
    }