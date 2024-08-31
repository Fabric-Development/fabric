{
  description = ''
  next-gen framework for building desktop widgets using Python (check the rewrite branch for progress)
  '';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/24.05";
    nixpkgs-unstable.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    nixpkgs-unstable,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem
    (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      unstable-pkgs = nixpkgs-unstable.legacyPackages.${system};

      pythonWithPackages = pkgs.python311.withPackages (ps: with ps; [
        setuptools
        wheel
        build
        click
        pycairo
        pygobject3
        loguru
        psutil
        self.packages.${system}.default
        ]);
    in {
      packages = {
        default = pkgs.callPackage ./default.nix { };
      };
      apps = {
      };
      devShells = {
        default = pkgs.mkShell {
          name = "fabric-shell";
          packages = [
            unstable-pkgs.basedpyright
            unstable-pkgs.ruff
            pythonWithPackages
            pkgs.gtk3
            pkgs.gtk-layer-shell
            pkgs.cairo
            pkgs.gobject-introspection
            pkgs.libdbusmenu-gtk3
            pkgs.gdk-pixbuf
            pkgs.gnome.gnome-bluetooth
          ];
        };
      };
    });
}


