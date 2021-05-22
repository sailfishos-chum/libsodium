Name:       libsodium
Version:    1.0.18.stable
Release:    1
Summary:    A modern, portable, easy to use crypto library.
Group:      Applications/Utilities
URL:        https://libsodium.org/
License:    ISC

%description
Sodium is a new, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

%package devel
Summary:    Development headers and libraries for libsodium.
Requires:   %{name} = %{version}-%{release}

%description devel
Sodium is a new, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

%build
cd libsodium-stable
%configure
make

%check
cd libsodium-stable
make check

%install
rm -rf %{buildroot}
cd libsodium-stable
%make_install
ls -lR %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
