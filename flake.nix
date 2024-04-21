{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

    Lightroom-SQL-tools = {
      url = "github:fdenivac/Lightroom-SQL-tools";
      flake = false;
    };

  };

  outputs = { nixpkgs, ... }@inputs:
    let
      forAllSystems = function:
        nixpkgs.lib.genAttrs [ "x86_64-darwin" "aarch64-darwin" ]
        (system: function nixpkgs.legacyPackages.${system});

    in {
      devShells = forAllSystems (pkgs: rec {
        LrToPhotos = pkgs.mkShell {
          name = "LrToPhotos-shell";
          nativeBuildInputs = [ pkgs.python312 ];

          shellHook = ''
            source venv/bin/activate
          '';
        };

        default = LrToPhotos;
      });
    };
}
