Name:           python-pathlib-abc
Version:        0.3.1
Release:        1%{?dist}
Summary:        Python base classes for rich path objects


License:        PSF-2.0
URL:            https://github.com/barneygale/pathlib-abc
Source:         %{url}/archive/%{version}/pathlib-abc-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Python base classes for rich path objects.}

%description %{_description}

%package -n     python3-pathlib-abc
Summary:        %{summary}

%description -n python3-pathlib-abc %{_description}

%prep
%autosetup -n pathlib-abc-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pathlib_abc


%check
%tox


%files -n python3-pathlib-abc -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
