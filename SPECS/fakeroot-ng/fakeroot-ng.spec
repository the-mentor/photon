Summary:       Fools programs into thinking they are running with root permission
Name:          fakeroot-ng
Version:       0.18
Release:       4%{?dist}
License:       GPLv2+
URL:           http://fakeroot-ng.lingnu.com/
Group:         System Environment/Base
Vendor:        VMware, Inc.
Distribution:  Photon

Source0:       http://downloads.sourceforge.net/project/fakerootng/fakeroot-ng/%{version}/fakeroot-ng-%{version}.tar.gz
%define sha512 %{name}=8ece6830d229b92537d9c0a2eb42cb9ec4ae6b83453303004dded5eab0707b9ae8eaa2c71aac6ea68226c43cf08db6b0939a9422aab32948f5ecb185ee01d854

Patch0:        Add-sched-h-to-process-cpp.patch

BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:     x86_64

%description
Fakeroot-ng is a clean re-implementation of fakeroot. The core idea
is to run a program, but wrap all system calls that program performs
so that it thinks it is running as root, while it is, in practice,
running as an unprivileged user. When the program is trying to perform
a privileged operation (such as modifying a file's owner or creating
a block device), this operation is emulated, so that an unprivileged
operation is actually carried out, but the result of the privileged
operation is reported to the program whenever it attempts to query
the result.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
%make_install %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root,-)
%{_bindir}/fakeroot-ng
%doc %{_mandir}/man1/fakeroot-ng.1.gz

%changelog
* Mon Sep 19 2022 Vamsi Krishna Brahmajosyula <vbrahmajosyula@vmware.com> 0.18-4
- Fix build with latest tool chain
* Mon Oct 22 2018 Ajay Kaher <akaher@vmware.com> 0.18-3
- Adding BuildArch
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.18-2
- GA - Bump release of all rpms
* Fri Jul 10 2015 Luis Zuniga <lzuniga@vmware.com> 0.17-0.1
- Initial build for Photon
