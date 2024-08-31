{ lib
, python311Packages
, gtk3
, gtk-layer-shell
, cairo
, gobject-introspection
, libdbusmenu-gtk3
, gdk-pixbuf
, gnome
}:

python311Packages.buildPythonPackage rec {
  pname = "fabric";
  version = "0.0.1";
  pyproject = true;

  src = ./.;

  buildInputs = [
    gtk3
    gtk-layer-shell
    cairo
    gobject-introspection
    libdbusmenu-gtk3
    gdk-pixbuf
    gnome.gnome-bluetooth
  ];

  dependencies = with python311Packages; [
    setuptools
    click
    pycairo
    pygobject3
    loguru
    psutil
  ];

  meta = {
    changelog = "";
    description = ''
    next-gen framework for building desktop widgets using Python (check the rewrite branch for progress)
    '';
    homepage = "https://github.com/Fabric-Development/fabric";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [];
  };
}
