%define debug_package %{nil}

Name:     car
Version:  2.16.0
Release:  1
Summary:  Work with car (Content addressed ARchive) files
License:  Apache-2.0 OR MIT
Group:    Archiving
URL:      https://github.com/ipfs/%{name}
Source0:  https://github.com/ipfs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:  %{name}-%{version}-deps.tar.zst

Patch0:  update-deps.patch

BuildRequires:  golang

%description
Golang implementation of the CAR specifications, both CARv1 and CARv2.

%prep
%autosetup -a 1 -p 1 -n go-%{name}-%{version}
mv vendor cmd/

%build
# Set build environment, in particular use "-mod=vendor" to use the Go modules from the source archive's vendor dir
export BUILD_USER=abf BUILD_HOST=OpenMandriva
export CGO_CPPFLAGS="${CPPFLAGS}" CGO_CFLAGS="${CFLAGS}" CGO_CXXFLAGS="${CXXFLAGS}" CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-trimpath -buildvcs=false -buildmode=pie -mod=vendor"

cd cmd/%{name}
go build -o ../../%{name}

%install
mkdir -p %{buildroot}/%{_bindir}
mv %{name} %{buildroot}/%{_bindir}/

%files
%license LICENSE.md
%doc cmd/%{name}/README.md
%{_bindir}/%{name}
