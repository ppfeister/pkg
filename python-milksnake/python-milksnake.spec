Name:           python-milksnake
Version:        0.1.5
Release:        1%{?dist}
Summary:        Rust binding to milksnake


License:        Apache-2.0
URL:            https://github.com/getsentry/milksnake
Source:         %{url}/archive/%{version}/milksnake-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Rust binding to milksnake}

%description %{_description}

%package -n     python3-milksnake
Summary:        %{summary}

%description -n python3-milksnake %{_description}

%prep
%autosetup -n milksnake-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l milksnake


%check
%tox

%files -n python3-milksnake -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
