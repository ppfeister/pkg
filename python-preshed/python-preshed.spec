Name:           python-preshed
Version:        3.0.9
Release:        1%{?dist}
Summary:        Cython hash tables that assume keys are pre-hashed 


License:        MIT
URL:            https://github.com/explosion/preshed
Source:         %{url}/archive/v%{version}/preshed-%{version}.tar.gz

BuildArch:      x86_64 aarch64

BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  gcc-c++

%global _description %{expand:
Simple but high performance Cython hash table mapping pre-randomized keys to
void* values.}

%description %{_description}

%package -n     python3-preshed
Summary:        %{summary}

%description -n python3-preshed %{_description}

%prep
%autosetup -n preshed-%{version}

# PyProject file not complete and throws off macros
rm -fv pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l preshed


%files -n python3-preshed -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
