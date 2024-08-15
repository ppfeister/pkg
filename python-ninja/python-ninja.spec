%global kitware_ref v1.11.1.g95dee.kitware.jobserver-1

Name:           python-ninja
Version:        1.11.1.1
Release:        %{autorelease}
Summary:        This project provides the infrastructure to build Ninja Python wheels


License:        Apache-2.0
URL:            https://github.com/scikit-build/ninja-python-distributions
Source0:         %{url}/archive/%{version}/ninja-%{version}.tar.gz
Source1:         https://github.com/Kitware/ninja/archive/%{kitware_ref}/kitware-%{kitware_ref}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

%global _description %{expand:
This project provides the infrastructure to build Ninja Python wheels.}

%description %{_description}

%package -n     python3-ninja
Summary:        %{summary}

%description -n python3-ninja %{_description}

%prep
%autosetup -n ninja-python-distributions-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L ninja


%check
%pytest


%files -n python3-ninja -f %{pyproject_files}
%license LICENSE_Apache_20
%doc README.md


%changelog
%autochangelog
