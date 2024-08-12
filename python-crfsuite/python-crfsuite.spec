Name:           python-crfsuite
Version:        0.3.1 
Release:        1%{?dist}
Summary:        Rust binding to crfsuite


License:        MIT
URL:            https://github.com/messense/crfsuite
Source:         %{url}/archive/v%{version}/crfsuite-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Rust binding to crfsuite}

%description %{_description}

%package -n     python3-crfsuite
Summary:        %{summary}

%description -n python3-crfsuite %{_description}

%prep
%autosetup -n crfsuite-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l crfsuite


%check
%tox

%files -n python3-crfsuite -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 3.8.2-1
- Initial package.
