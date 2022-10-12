Summary:    Provide tools to manage multipath devices
Name:       device-mapper-multipath
Version:    0.9.1
Release:    1%{?dist}
License:    GPL+
Group:      System Environment/Base
Vendor:     VMware, Inc.
URL:        http://christophe.varoqui.free.fr
Distribution: Photon

Source0: https://github.com/opensvc/multipath-tools/archive/refs/tags/multipath-tools-%{version}.tar.gz
%define sha512 multipath-tools=060ed31a23477b3ba73710f2fad3f9a5540514f5820ce5e0edebce687a7caf9b018c8e8205a24ba7c05d0aee7957b74f94ee2e2139e9f6ab30b439dae8bd3a87

# fix for CVE-2022-41973, CVE-2022-41974
Patch0: CVE-fixes.patch

BuildRequires:  userspace-rcu-devel
BuildRequires:  libaio-devel
BuildRequires:  device-mapper-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd-devel
BuildRequires:  json-c-devel

Requires:   userspace-rcu
Requires:   libaio
Requires:   device-mapper
Requires:   libselinux
Requires:   libsepol
Requires:   readline
Requires:   ncurses
Requires:   systemd
Requires:   kpartx = %{version}-%{release}

%description
Device-mapper-multipath provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do.

%package -n kpartx
Summary:    Partition device manager for device-mapper devices
Requires:   device-mapper
%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package devel
Summary: Development libraries and headers for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
It contains the libraries and header files to create applications

%prep
%autosetup -p1 -n multipath-tools-%{version}

%build
%make_build

%install
%make_install %{?_smp_mflags} \
    SYSTEMDPATH=%{_libdir} \
    bindir=%{_sbindir} \
    syslibdir=%{_libdir} \
    usrlibdir=%{_libdir} \
    libdir=%{_libdir}/multipath \
    pkgconfdir=%{_libdir}/pkgconfig

install -vd %{buildroot}%{_sysconfdir}/multipath

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_sbindir}/mpathpersist
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/multipathc
%{_udevrulesdir}/*
%{_unitdir}/*
%{_libdir}/*.so.*
%{_libdir}/multipath/*.so
%{_mandir}/man5/*
%{_mandir}/man8/mpathpersist.8.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%dir %{_sysconfdir}/multipath
%config(noreplace) %{_libdir}/modules-load.d/multipath.conf
%{_mandir}/man8/multipathc.8.gz
%{_tmpfilesdir}/multipath.conf

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n kpartx
%defattr(-,root,root,-)
%{_sbindir}/kpartx
%{_libdir}/udev/kpartx_id
%{_mandir}/man8/kpartx.8.gz

%changelog
* Tue Oct 11 2022 Shreenidhi Shedi <sshedi@vmware.com> 0.9.1-1
- Upgrade to v0.9.1
* Wed Nov 24 2021 Vikash Bansal <bvikas@vmware.com> 0.8.4-2
- Bump up version to compile with new libsepol
* Wed Oct 07 2020 Shreenidhi Shedi <sshedi@vmware.com> 0.8.4-1
- Upgrade to version 0.8.4
* Tue Aug 18 2020 Michelle Wang <michellew@vmware.com> 0.8.3-2
- Fix how to call json_object_object_get_ex in ./libdmmp/libdmmp_private.h
- due to json-c 0.15 update json_object_object_get_ex return value
* Wed Apr 08 2020 Susant Sahani <ssahani@vmware.com> 0.8.3-1
- Update to 0.8.3
* Thu Dec 06 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 0.7.3-3
- Make device-mapper a runtime dependency of kpartx.
* Wed Sep 26 2018 Anish Swaminathan <anishs@vmware.com>  0.7.3-2
- Remove rados dependency
* Wed Oct 04 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.7.3-1
- Update to 0.7.3
* Tue May 9  2017 Bo Gan <ganb@vmware.com> 0.7.1-1
- Update to 0.7.1
* Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  0.5.0-3
- Change systemd dependency
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.5.0-2
- GA - Bump release of all rpms
* Mon Jun 22 2015 Divya Thaluru <dthaluru@vmware.com> 0.5.0-1
- Initial build. First version
