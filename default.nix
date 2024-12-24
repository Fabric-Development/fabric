{
  lib,
  python312Packages,
  gtk3,
  gtk-layer-shell,
  cairo,
  gobject-introspection,
  libdbusmenu-gtk3,
  gdk-pixbuf,
  cinnamon-desktop,
  gnome-bluetooth,
}:
python312Packages.buildPythonPackage {
  pname = "python-fabric";
  version = "0.0.2";
  pyproject = true;

  src = ./.;

  buildInputs = [
    gtk3
    gtk-layer-shell
    cairo
    gobject-introspection
    libdbusmenu-gtk3
    gdk-pixbuf
    cinnamon-desktop
    gnome-bluetooth
  ];

  dependencies = with python312Packages; [
    setuptools
    click
    pycairo
    pygobject3
    pygobject-stubs
    loguru
    psutil
  ];

  meta = {
    changelog = "";
    description = ''
      next-gen framework for building desktop widgets using Python (check the rewrite branch for progress)
    '';
    homepage = "https://github.com/Fabric-Development/fabric";
    license = lib.licenses.agpl3Plus;
    maintainers = with lib.maintainers; [];
  };
}
