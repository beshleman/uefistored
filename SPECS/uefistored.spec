Name:           uefistored
# TODO: set current version
Version:        0.1
Release:        1%{?dist}
Summary:        Variables store for UEFI guests
# TODO: add license in repository
# Suggested: GPLv2 which is what the Xen project uses
License:        GPLv2
URL:            https://github.com/xcp-ng/uefistored
Source0:        https://github.com/xcp-ng/uefistored/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel

# TODO: what about varstored-tools?
Provides: varstored
Obsoletes: varstored

%description
TODO

%prep
%autosetup -p1

%build
make

%install
%make_install
# symlink binary to varstored to let XAPI find it
ln -s uefistored %{buildroot}%{_sbindir}/varstored

%files
%{_sbindir}/uefistored
%{_sbindir}/varstored

%changelog
Fri Jul 17 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.1-1
- TODO, update changelog entry for first build
