Summary:        A C++11 library for performing operations on two-dimensional vector geometries
Name:           geos
Version:        3.11.0
Release:        1%{?dist}
License:        LGPLv2
URL:            https://trac.osgeo.org/geos
Group:          System Environment/Development
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: http://download.osgeo.org/geos/%{name}-%{version}.tar.bz2
%define sha512 %{name}=40c7553bbb93673c231ddd0131b73bf43b3f50524bc5bd9e6934c068d2c09632f388b7429254ae15d9641da2d15e3a626b430438854e98d9e7419ad04e535189

BuildRequires:  cmake

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the JTS Topology Suite (JTS).
It aims to contain the complete functionality of JTS in C++.

%package    devel
Summary:    Header and development files
Requires:   %{name} = %{version}-%{release}

%description    devel
It contains the libraries and header files

%prep
%autosetup -p1

%build
%cmake \
    -DDEFAULT_BUILD_TYPE=Debug \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}

%cmake_build

%install
%cmake_install

%if 0%{?with_check}
%check
make %{?_smp_mflags} check
%endif

%clean
rm -rf %{buildroot}/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/geos-config
%{_bindir}/geosop
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/geos
%{_includedir}/geos.h
%{_includedir}/geos_c.h
%{_libdir}/*.so
%{_libdir}/cmake/GEOS
%{_libdir}/pkgconfig/geos.pc

%changelog
* Thu Sep 29 2022 Shreenidhi Shedi <sshedi@vmware.com> 3.11.0-1
- Upgrade to v3.11.0
* Fri Jun 17 2022 Shreenidhi Shedi <sshedi@vmware.com> 3.10.2-2
- Fix build with latest cmake
* Mon Apr 18 2022 Gerrit Photon <photon-checkins@vmware.com> 3.10.2-1
- Automatic Version Bump
* Tue Apr 13 2021 Gerrit Photon <photon-checkins@vmware.com> 3.9.1-1
- Automatic Version Bump
* Wed Jul 22 2020 Gerrit Photon <photon-checkins@vmware.com> 3.8.1-1
- Automatic Version Bump
* Mon Mar 09 2020 Ankit Jain <ankitja@vmware.com> 3.8.0-1
- Initial build.  First version.
