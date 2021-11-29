%global security_hardening none
%global commit          d2063b7693e0e35db97b2264aa987eb6341ae779
%define debug_package %{nil}

Summary:        iPXE open source boot firmware
Name:           ipxe
Version:        1.20.1
Release:        3%{?dist}
License:        GPLv2
URL:            http://ipxe.org
Group:          System Environment/Daemons
Vendor:         VMware, Inc.
Distribution:   Photon
#Download URL:  https://github.com/ipxe/ipxe/archive/v%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
%define sha1    ipxe=7d55f469cd12142f79d8730a0a80c954cd9d50ec
Patch0:         ipxe-gcc-10.patch
Patch1:         ipxe-gcc-10-fcommon.patch
BuildArch:      x86_64
BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  cdrkit
BuildRequires:  gcc
BuildRequires:  libgcc
BuildRequires:  libgcc-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib
BuildRequires:  zlib-devel

%description
iPXE is the leading open source network boot firmware. It provides a full
PXE implementation enhanced with additional features.

%prep
%autosetup -n %{name}-%{version} -p1

%build
cd src
make %{_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
mkdir -p %{buildroot}/usr/share/ipxe
install -vDm 644 src/bin/ipxe.{dsk,iso,lkrn,usb} %{buildroot}/usr/share/ipxe/
install -vDm 644 src/bin/*.{rom,mrom} %{buildroot}/usr/share/ipxe/

%files
%defattr(-,root,root)
/usr/share/ipxe/ipxe.dsk
/usr/share/ipxe/ipxe.iso
/usr/share/ipxe/ipxe.lkrn
/usr/share/ipxe/ipxe.usb
/usr/share/ipxe/10222000.rom
/usr/share/ipxe/10500940.rom
/usr/share/ipxe/10ec8139.rom
/usr/share/ipxe/15ad07b0.rom
/usr/share/ipxe/1af41000.rom
/usr/share/ipxe/8086100e.mrom
/usr/share/ipxe/8086100f.mrom
/usr/share/ipxe/808610d3.mrom
/usr/share/ipxe/80861209.rom
/usr/share/ipxe/rtl8139.rom

%changelog
*   Wed Sep 08 2021 Nitesh Kumar <kunitesh@vmware.com> 1.20.1-3
-   Replacement of ITS suggested words.
*   Thu Jan 14 2021 Alexey Makhalov <amakhalov@vmware.com> 1.20.1-2
-   GCC-10 support.
*   Wed Sep 09 2020 Gerrit Photon <photon-checkins@vmware.com> 1.20.1-1
-   Automatic Version Bump
*   Wed Apr 01 2020 Alexey Makhalov <amakhalov@vmware.com> 20180717-3
-   Fix compilation issue with gcc-8.4.0
*   Mon Oct 22 2018 Ajay Kaher <akaher@vmware.com> 20180717-2
-   Adding BuildArch
*   Thu Oct 11 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 20180717-1
-   Use commit date instead of commit id as the package version.
*   Wed Aug 08 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> d2063b7-1
-   Update version to get it to build with gcc 7.3
*   Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com>  553f485-2
-   deactivate debuginfo gen
*   Mon Mar 13 2017 Alexey Makhalov <amakhalov@vmware.com> 553f485-1
-   Version update to build with gcc-6.3
-   Removed linux/linux-devel build-time dependency
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> ed0d7c4-2
-   GA - Bump release of all rpms
*   Thu Nov 12 2015 Vinay Kulkarni <kulkarniv@vmware.com> ed0d7c4-1
-   Initial build. First version
