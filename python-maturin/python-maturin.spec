Name:           python-maturin
Version:        1.7.0
Release:        1%{?dist}
Summary:        Build and publish crates with pyo3, cffi and uniffi bindings


License:        Apache-2.0
URL:            https://github.com/PyO3/maturin
Source:         %{url}/archive/v%{version}/maturin-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  rust-anyhow-devel

%global _description %{expand:
Build and publish crates with pyo3, cffi and uniffi bindings as well as rust
binaries as python packages with minimal configuration. It supports building
wheels for python 3.8+ on windows, linux, mac and freebsd, can upload them to
pypi and has basic pypy and graalpy support.}

%description %{_description}

%package -n     python3-maturin
Summary:        %{summary}

%description -n python3-maturin %{_description}

%prep
%autosetup -n maturin-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l maturin


%files -n python3-maturin -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
