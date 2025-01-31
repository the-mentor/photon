Summary:        Command-line tools to communicate with a FIDO device over USB
Name:           libfido2
Version:        1.11.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/Yubico/%{name}
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://github.com/Yubico/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
%define sha512 %{name}=d9644453d67b84ec8385dfb63796adb3eae2d7f7cb47fbb1bcf9ca7f5cce400623738cc3317d629c2f0af630424cb2788217f8c7f20d1b52b7369c729052d572

BuildRequires:  cmake
BuildRequires:  libcbor-devel
BuildRequires:  systemd-devel

Requires:  libcbor
Requires:  systemd

%description
A library provide the functionality and CLI tools to communicate with a FIDO
device over USB, and to verify attestation and assertion signatures.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

%package tools
Summary:        FIDO2 CLI tools
Requires:       %{name} = %{version}-%{release}

%description tools
FIDO2 CLI tools to access and configure a FIDO2 compliant authentication device.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_exec_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DBUILD_EXAMPLES=OFF

%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%doc NEWS README.adoc
%license LICENSE
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.11.0

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Sep 01 2022 Vamsi Krishna Brahmajosyula <vbrahmajosyula@vmware.com> 1.11.0-1
- Upgrade to latest version
* Fri Jun 17 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.10.0-2
- Fix build with latest cmake
* Fri May 13 2022 Nitesh Kumar <kunitesh@vmware.com> 1.10.0-1
- Initial version
