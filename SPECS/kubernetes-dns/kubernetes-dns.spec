Summary:        Kubernetes DNS
Name:           kubernetes-dns
Version:        1.21.2
Release:        3%{?dist}
License:        ASL 2.0
URL:            https://github.com/kubernetes/dns/archive/%{version}.tar.gz
Source0:        kubernetes-dns-%{version}.tar.gz
%define sha1    kubernetes-dns-%{version}.tar.gz=35647d9d3421bf33d73b7e2cb9713b4abe349117
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  go
BuildRequires:  ca-certificates

%description
Kubernetes DNS is a name lookup service for kubernetes pods.

%prep -p exit
%autosetup -n dns-%{version}
export GO111MODULE=auto

%build
%ifarch x86_64
export ARCH=amd64
%endif

%ifarch aarch64
export ARCH=arm64
%endif

export VERSION=%{version}
export PKG=k8s.io/dns
export GOARCH=${ARCH}
export GOHOSTARCH=${ARCH}
export GOOS=linux
export GOHOSTOS=linux
export GOROOT=/usr/lib/golang
export GOPATH=/usr/share/gocode
export CGO_ENABLED=0
export GO111MODULE=auto
mkdir -p ${GOPATH}/src/${PKG}
cp -r * ${GOPATH}/src/${PKG}/
pushd ${GOPATH}/src/${PKG}
ARCH=${ARCH} VERSION=${VERSION} PKG=${PKG} go install \
    -installsuffix "static" \
    -ldflags "-X ${PKG}/pkg/version.VERSION=${VERSION}" \
    ./...

%install
install -m 755 -d %{buildroot}%{_bindir}
binaries=(dnsmasq-nanny e2e kube-dns sidecar sidecar-e2e)
for bin in "${binaries[@]}"; do
  echo "+++ INSTALLING ${bin}"
  install -pm 755 -t %{buildroot}%{_bindir} ${GOPATH}/bin/${bin}
done

%check
export ARCH=amd64
export VERSION=%{version}
export PKG=k8s.io/dns
export GOPATH=/usr/share/gocode
pushd ${GOPATH}/src/${PKG}
./build/test.sh cmd pkg

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/dnsmasq-nanny
%{_bindir}/e2e
%{_bindir}/kube-dns
%{_bindir}/sidecar
%{_bindir}/sidecar-e2e

%changelog
*   Tue Feb 22 2022 Piyush Gupta <gpiyush@vmware.com> 1.21.2-3
-   Bump up version to compile with new go
*   Mon Jan 24 2022 Piyush Gupta <gpiyush@vmware.com> 1.21.2-2
-   Bump up version to compile with new go
*   Thu Nov 18 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.21.2-1
-   Update to version 1.21.2
*   Wed Oct 20 2021 Piyush Gupta <gpiyush@vmware.com> 1.15.6-7
-   Bump up version to compile with new go
*   Tue Oct 05 2021 Piyush Gupta <gpiyush@vmware.com> 1.15.6-6
-   Bump up version to compile with new go
*   Fri Jun 11 2021 Piyush Gupta <gpiyush@vmware.com> 1.15.6-5
-   Bump up version to compile with new go
*   Thu Mar 25 2021 Piyush Gupta<gpiyush@vmware.com> 1.15.6-4
-   Bump up version to compile with new go
*   Fri Feb 05 2021 Harinadh D <hdommaraju@vmware.com> 1.15.6-3
-   Bump up version to compile with new go
*   Fri Jan 15 2021 Piyush Gupta<gpiyush@vmware.com> 1.15.6-2
-   Bump up version to compile with new go
*   Tue Jun 30 2020 Gerrit Photon <photon-checkins@vmware.com> 1.15.6-1
-   Automatic Version Bump
*   Fri May 18 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 1.14.8-1
-   kubernetes-dns 1.14.8.
*   Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 1.14.6-3
-   Aarch64 support
*   Wed Nov 01 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.14.6-2
-   Remove go testing framework binary.
*   Mon Oct 02 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.14.6-1
-   kubernetes-dns 1.14.6.
*   Mon Sep 11 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.14.4-1
-   kubernetes-dns 1.14.4.
*   Wed Jun 28 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.14.2-1
-   kubernetes-dns for PhotonOS.
