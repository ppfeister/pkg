Name:           python-cymem
Version:        2.0.8
Release:        1%{?dist}
Summary:        Cython memory pool for RAII-style memory management


License:        MIT
URL:            https://github.com/explosion/cymem
Source:         %{url}/archive/v%{version}/cymem-%{version}.tar.gz

BuildArch:      x86_64 aarch64

BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  gcc-c++

%global _description %{expand:
cymem provides two small memory-management helpers for Cython. They make it
easy to tie memory to a Python object's life-cycle, so that the memory is freed
when the object is garbage collected.}

%description %{_description}

%package -n     python3-cymem
Summary:        %{summary}

%description -n python3-cymem %{_description}

%prep
%autosetup -n cymem-%{version}

# PyProject file not complete and throws off macros
rm -fv pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l cymem


%files -n python3-cymem -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
