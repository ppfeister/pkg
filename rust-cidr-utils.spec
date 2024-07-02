# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate cidr-utils

Name:           rust-cidr-utils
Version:        0.6.1
Release:        %autorelease
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs

License:        MIT
URL:            https://crates.io/crates/cidr-utils
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
This crate provides functions for working with IPv4 CIDRs and IPv6
CIDRs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+combiner-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+combiner-devel %{_description}

This package contains library source intended for building other packages which
use the "combiner" feature of the "%{crate}" crate.

%files       -n %{name}+combiner-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+iterator-devel %{_description}

This package contains library source intended for building other packages which
use the "iterator" feature of the "%{crate}" crate.

%files       -n %{name}+iterator-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+separator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+separator-devel %{_description}

This package contains library source intended for building other packages which
use the "separator" feature of the "%{crate}" crate.

%files       -n %{name}+separator-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
