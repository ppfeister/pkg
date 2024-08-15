Name:           python-jiter
Version:        0.5.0
Release:        1%{?dist}
Summary:        Fast iterable JSON parser


License:        MIT
URL:            https://github.com/pydantic/jiter
Source:         %{url}/archive/v%{version}/jiter-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This is a standalone version of the JSON parser used in pydantic-core. The
recommendation is to only use this package directly if you do not use pydantic.
}

%description %{_description}

%package -n     python3-jiter
Summary:        %{summary}

%description -n python3-jiter %{_description}

%prep
%autosetup -n jiter-%{version}
cd crates/jiter-python


%generate_buildrequires
cd crates/jiter-python
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jiter


%files -n python3-jiter -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
