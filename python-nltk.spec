Name:           python-nltk
Version:        3.8.2
Release:        1%{?dist}
Summary:        Natural Language Toolkit


License:        Apache-2.0
URL:            https://github.com/nltk/nltk
Source:         %{url}/archive/%{version}/nltk-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in
Natural Language Processing.}

%description %{_description}

%package -n     python3-nltk
Summary:        %{summary}

%description -n python3-nltk %{_description}

%prep
%autosetup -n nltk-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nltk


%check
%tox

%files -n python3-nltk -f %{pyproject_files}
%doc README.md


%changelog
* Sun Aug 11 2024 Paul Pfeister <code@pfeister.dev> - 3.8.2-1
- Initial package.
