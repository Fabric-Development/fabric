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
    nixpkgs,
    nixpkgs-unstable,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem
    (system: let
      overlay = final: prev: {
        pythonPackagesExtensions =
          prev.pythonPackagesExtensions
          ++ [
            (
              python-final: python-prev: {
                fabric-widgets = prev.callPackage ./default.nix {};
              }
            )
          ];
      };

      pkgs = nixpkgs.legacyPackages.${system}.extend overlay;
      unstable-pkgs = nixpkgs-unstable.legacyPackages.${system};

      pythonWithPackages = pkgs.python3.withPackages (ps:
        with ps; [
          setuptools
          wheel
          build
          click
          pycairo
          pygobject3
          loguru
          psutil
          fabric-widgets
        ]);
    in {
      packages = {
        default = pkgs.python3Packages.fabric-widgets;
      };

      overlays.default = overlay;

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
