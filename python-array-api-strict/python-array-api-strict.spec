Name:           python-array-api-strict
Version:        2.0.1
Release:        %{autorelease}
Summary:        Strict implementation of the Python array API


License:        BSD-3-Clause
URL:            https://github.com/data-apis/array-api-strict
Source:         %{url}/archive/%{version}/array-api-strict-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
BuildRequires:  python3-hypothesis

%global _description %{expand:
array_api_strict is a strict, minimal implementation of the Python array API.

The purpose of array-api-strict is to provide an implementation of the array
API for consuming libraries to test against so they can be completely sure
their usage of the array API is portable.}

%description %{_description}

%package -n     python3-array-api-strict
Summary:        %{summary}

%description -n python3-array-api-strict %{_description}

%prep
%autosetup -n array-api-strict-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l array_api_strict


%check
%pytest


%files -n python3-array-api-strict -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
