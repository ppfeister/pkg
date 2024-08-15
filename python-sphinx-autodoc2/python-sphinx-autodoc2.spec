Name:           python-sphinx-autodoc2
Version:        0.5.0
Release:        %{autorelease}
Summary:        Measure, monitor and analyze the memory behavior of Python objects 


License:        MIT
URL:            https://github.com/sphinx-extensions2/sphinx-autodoc2
Source0:         %{url}/archive/v%{version}/sphinx-autodoc2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

Recommends:     python-sphinx-autodoc2+cli
Recommends:     python-sphinx-autodoc2+docs
Recommends:     python-sphinx-autodoc2+sphinx
Suggests:       python3-typer+all
Suggests:       python3-furo
Suggests:       python3-myst-parser

%global _description %{expand:
Development tool to measure, monitor and analyze the memory behavior of Python
objects in a running Python application.}

%description %{_description}

%pyproject_extras_subpkg -n python3-sphinx-autodoc2 cli docs sphinx

%package -n     python3-sphinx-autodoc2
Summary:        %{summary}

%description -n python3-sphinx-autodoc2 %{_description}


%prep
%autosetup -p1 -n sphinx-autodoc2-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -e py%{python3_version_nodots}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L autodoc2


# Upstream test issues related to Sphinx, temporary hold on %%check neccessary
#%%check
# tox is present, but it doesn't properly run tests
#%%pytest


%files -n python3-sphinx-autodoc2 -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/autodoc2


%changelog
%autochangelog
