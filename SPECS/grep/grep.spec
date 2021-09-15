Summary:	Programs for searching through files
Name:		grep
Version:	3.0
Release:	5%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/grep
Group:		Applications/File
Vendor:		VMware, Inc.
Distribution: Photon

Source0:	http://ftp.gnu.org/gnu/grep/%{name}-%{version}.tar.xz
%define sha1 %{name}=7b742a6278f28ff056da799c62c1b9e417fe86ba

Conflicts:      toybox < 0.7.3-7

%description
The Grep package contains programs for searching through files.

%package    lang
Summary:    Additional language files for grep
Group:      System Environment/Base
Requires:   %{name} = %{version}-%{release}

%description lang
These are the additional language files of grep

%prep
%setup -q

%build
sh ./configure --prefix=%{_prefix} \
            --bindir=/bin \
            --disable-silent-rules

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}

%check
#disable grep -P, not suppported.
sed -i '1474d' tests/Makefile
sed -i '2352,2358d' tests/Makefile
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
/bin/*
%{_mandir}/*/*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
* Mon Sep 13 2021 Shreenidhi Shedi <sshedi@vmware.com> 3.0-5
- Conflict only with toybox < 0.7.3-7
* Mon Oct 02 2017 Alexey Makhalov <amakhalov@vmware.com> 3.0-4
- Added conflicts toybox
* Wed Aug 23 2017 Rongrong Qiu <rqiu@vmware.com> 3.0-3
- Disable grep -P for make check bug 1900287
* Tue May 02 2017 Anish Swaminathan <anishs@vmware.com> 3.0-2
- Add lang package.
* Fri Mar 24 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.0-1
- Upgrading grep to 3.0 version
* Thu Oct 06 2016 ChangLee <changlee@vmware.com> 2.21-3
- Modified %check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.21-2
- GA - Bump release of all rpms
* Mon Apr 6 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 2.21-1
- Upgrading grep to 2.21 version, and adding
* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.16-1
- Initial build. First version
