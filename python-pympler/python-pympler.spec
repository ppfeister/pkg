Name:           python-pympler
Version:        1.1
Release:        %{autorelease}
Summary:        Measure, monitor and analyze the memory behavior of Python objects 


License:        Apache-2.0
URL:            https://github.com/pympler/pympler
Source:         %{url}/archive/%{version}/pympler-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-bottle

%global _description %{expand:
Development tool to measure, monitor and analyze the memory behavior of Python
objects in a running Python application.}

%description %{_description}

%package -n     python3-pympler
Summary:        %{summary}

%description -n python3-pympler %{_description}

%prep
%autosetup -n pympler-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pympler


%check
%{py3_test_envvars} %{python3} test/runtest.py


%files -n python3-pympler -f %{pyproject_files}
%license LICENSE
%license NOTICE
%doc README.md


%changelog
%autochangelog
