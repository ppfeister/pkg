# Note: python-coveralls is the name of the package on PyPI, so
# python-python-coveralls is in fact the intended name.
Name:           python-python-coveralls
Version:        2.9.2
Release:        1%{?dist}
Summary:        Python API for coveralls.io


License:        Apache-2.0
URL:            https://github.com/z4r/python-coveralls
Source:         %{url}/archive/%{version}/python-coveralls-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Python API for coveralls.io}

%description %{_description}

%package -n     python3-python-coveralls
Summary:        %{summary}

%description -n python3-python-coveralls %{_description}

%prep
%autosetup -n python-coveralls-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l coveralls

rm '%{buildroot}%{_bindir}/coveralls'


# Checks are questionable and therefore skipped.


%files -n python3-python-coveralls -f %{pyproject_files}
%doc README.rst


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
