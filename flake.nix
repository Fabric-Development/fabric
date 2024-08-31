{
  description = ''
    next-gen framework for building desktop widgets using Python
    (check the rewrite branch for progress)
  '';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/24.05";
    utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, utils, ... }:
    utils.lib.eachDefaultSystem (
      system:
      let
        overlay = final: prev: {
          pythonPackagesExtensions = prev.pythonPackagesExtensions ++ [
            (python-final: python-prev: {
              # `fabric` was taken
              fabric-widgets = prev.callPackage ./default.nix { };
            })
          ];
        };

        pkgs = nixpkgs.legacyPackages.${system}.extend overlay;
      in
      {
        packages.default = pkgs.python3Packages.fabric-widgets;
        overlays.default = overlay;
        formatter = pkgs.nixfmt-rfc-style;

        devShells = {
          default = pkgs.mkShell {
            name = "fabric-shell";
            packages = with pkgs; [
              ruff
              gtk3
              gtk-layer-shell
              cairo
              gobject-introspection
              libdbusmenu-gtk3
              gdk-pixbuf
              gnome.gnome-bluetooth
              (python3.withPackages (
                ps: with ps; [
                  setuptools
                  wheel
                  build
                  click
                  pycairo
                  pygobject3
                  loguru
                  psutil
                  fabric-widgets
                ]
              ))
            ];
          };
        };
      }
    );
}
