# Created by pyp2rpm-3.3.10
%global pypi_name blis
%global pypi_version 1.0.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Fast matrix-multiplication as a self-contained Python library

License:        MIT
URL:            https://github.com/explosion/cython-blis
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-cython
BuildRequires:  python3-numpy
BuildRequires:  gcc-c++
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Fast matrix-multiplication as a self-contained Python library.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Relax numpy for fedora#2210209 and fedora#2239427
ls -la
sed -i 's/numpy>=2\.0\.0,<3\.0\.0/numpy>=1.26.0/' pyproject.toml
sed -i 's/numpy>=2\.0\.0,<3\.0\.0/numpy>=1.26.0/' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/blis-%{pypi_version}-py%{python3_version}.egg-info
%{python3_sitelib}/blis/

%changelog
* Wed Aug 14 2024 Paul Pfeister <code@pfeister.dev> - 6.0.0.20240621-1
- Initial package.
