Name:           python-thinc
Version:        9.0.0
Release:        1%{?dist}
Summary:        Functional and refreshing take on deep learning


License:        MIT
URL:            https://github.com/explosion/thinc
Source:         %{url}/archive/v%{version}/thinc-%{version}.tar.gz

BuildArch:      x86_64 aarch64

BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  gcc-c++

%global _description %{expand:
Thinc is a lightweight deep learning library that offers an elegant,
type-checked, functional-programming API for composing models, with support
for layers defined in other frameworks such as PyTorch, TensorFlow and MXNet.}

%description %{_description}

%package -n     python3-thinc
Summary:        %{summary}

%description -n python3-thinc %{_description}

%prep
%autosetup -n thinc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l thinc


%files -n python3-thinc -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 0.1.5-1
- Initial package.
