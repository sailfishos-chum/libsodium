# Sailfish OS RPM Spec for libsodium

This is based on packaging work of aerique and extended for
compilation at OBS. Build is included into Chum repositories.

Below, the original README for building the library using aerique
approach.

This RPM spec file is for compiling `libsodium` and `libsodium-devel` for
Sailfish OS and specifically for the `aarch64` architecture. (It has only been
tested on `aarch64`.)

This library is a build and run dependency for
[ownKeepass](https://openrepos.net/content/jobe/ownkeepass) for which the
official repository at the moment only has `i486` and `armv7hl` packages.

This is my second RPM spec file ever, so feel free to point out improvements.

## Dependencies

### Build

- [Sailfish OS Builds in Docker](https://git.sr.ht/~aerique/sfosbid)

## Build Steps

### Preparing Sailfish OS Builds in Docker

- `mkdir ~/software` (if it does not exist yet)
- `cd ~/software`
- `git clone https://git.sr.ht/~aerique/sfosbid sfosbid-git`
- `cd sfosbid-git`
- `./download.sh`
- `./build.sh -u`
- `./run.sh -u`

### Building libsodium and libsodium-devel

This section assumes you've run `./run.sh -u` from the previous section and are
now in the Docker container.

- `cd projects`
- `git clone https://git.sr.ht/~aerique/libsodium-spec libsodium-spec-git`
- `cd libsodium-spec-git`
- `curl -o libsodium-1.0.18-stable.tar.gz https://download.libsodium.org/libsodium/releases/libsodium-1.0.18-stable.tar.gz `
- `tar xvfz libsodium-1.0.18-stable.tar.gz`
- `mb2 -t SailfishOS-latest-aarch64 build`

If the build finishes successfully you'll now have `libsodium` and
`libsodium-devel` packages in the `RPMS` directory. These will also be available
outside of the Docker container if you leave it.
