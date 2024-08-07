# Generated by rust2rpm 26
%bcond_without check

%global crate du-dust

Name:           rust-dust
Version:        1.0.0
Release:        %autorelease
Summary:        More intuitive version of du

License:        Apache-2.0
URL:            https://crates.io/crates/du-dust
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          dust-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A more intuitive version of du.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        Apache-2.0
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/dust

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
