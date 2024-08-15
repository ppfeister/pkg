%global pypi_name types-colorama
%global pypi_version 0.4.15.20240311

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Typing stubs for colorama

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/python/typeshed/main/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
This is a PEP 561 type stub package for the colorama package. It can be used by
type-checking tools like mypy, pyright, pytype, PyCharm, etc. to check code
that uses colorama.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l colorama-stubs

%files -n python3-%{pypi_name}
%{python3_sitelib}/colorama-stubs
%{python3_sitelib}/types_colorama-%{version}.dist-info

%changelog
* Wed Aug 14 2024 Paul Pfeister <code@pfeister.dev> - 0.4.15.20240311-1
- Initial package.