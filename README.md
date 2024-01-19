_**ricing made easy!**_ 🍙
# What is this?
Fabric is a python widgets _~~thing~~ framework_   made for \*Nix based systems (Wayland and X11), using GTK+

Fabric aims to provide you high-level and signal-based flow, neither polling nor bash scripting is required to do **basic** stuff, old men!

Also Fabric is configured in python which make's it easier than ever!

> [!NOTE]
> Please note that Fabric is still a work in progress, also the API is a subject to change.

### key features
1. **Simple** yet **Powerful**

	asking how simple actually it is?

	 \- head over to examples
1. X11 and Wayland ready!
2. All python modules are accessible to you!
3. Code  auto-completions ready!, see the stubs guide for more info: TBD
5. Less resource usage

	since everything can be written within the widget code this will no longer require you using external scripts, this will decreasethis widget resource usage

# How to Install?
it's really simple to get fabric working, you just...

1. install python

	Fabric requires python version 3.11 or higher

	for arch linux you do `pacman -S python` to get the latest version of python

3. get Cairo, GTK, GObject introspection and other dependency's
     
	this step does depend on your system, this command will work for arch linux to install the dependency's using `pacman`
	
	`sudo pacman -S gtk3 cairo gtk-layer-shell libgirepository gobject-introspection gobject-introspection-runtime python python-pip python-gobject python-cairo python-loguru pkgconf`

	 if you're not on Arch, you will have to figure out yourself what is the package names for your distro

5. install fabric

    > Fabric is available under the arch user repository with the name `python-fabric-git`

    you also can install fabric globally using `pip install git+https://github.com/Fabric-Development/fabric.git` although we **don't** prefer this way because it might cause dependency issues, it's better to use a [virtual environment](https://docs.python.org/3/library/venv), to get fabric in a virtual environment you'll have to do the following

    make a new folder for your new project

    `mkdir <your-folder-name>`

    change the current directory to this new folder

    `cd <your-folder-name>`

    create a new virtual environment, this command will create a virtual environment with the name `venv`

    `python -m venv venv`

    source the newly created virtual environment

    `source venv/bin/activate`

    now you can install packages, we can install fabric now...

    `pip install git+https://github.com/Fabric-Development/fabric.git`

    fabric is now installed!, later you can install whatever package you want.
---
## Showcase Section
these are some bars/widgets made using Fabric
- example files
	![config can be found under the examples directory](assets/example-files-showcase.png)
