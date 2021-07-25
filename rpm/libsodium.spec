Name:       libsodium
Version:    1.0.18
Release:    1
Summary:    A modern, portable, easy to use crypto library.
Group:      Applications/Utilities
URL:        https://libsodium.org/
License:    ISC
Source: %{name}-%{version}.tar.gz

BuildRequires: gcc libtool autoconf automake

%description
Sodium is a new, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

%package devel
Summary:    Development headers and libraries for libsodium.
Requires:   %{name} = %{version}-%{release}

%description devel
Sodium is a new, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

%prep
%setup -q -n %{name}-%{version}/libsodium

%build
DO_NOT_UPDATE_CONFIG_SCRIPTS=1 ./autogen.sh
%configure
%{__make} %{?_smp_mflags}

%check
make check

%install
rm -rf %{buildroot}
%make_install

%post -n libsodium -p /sbin/ldconfig

%postun -n libsodium -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/libsodium.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/sodium.h
%{_includedir}/sodium/*.h
%{_libdir}/pkgconfig/libsodium.pc
