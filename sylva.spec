# Packager: Paul Pfeister <code@pfeister.dev> (GitHub @ppfeister)
Name:           sylva
Version:        0.1.1
Release:        %autorelease
Summary:        Simplify the link between social and real identities

License:        AGPL-3.0-only
URL:            https://github.com/ppfeister/sylva
Source:         %{url}/archive/v%{version}/sylva-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man

Requires:       xorg-x11-server-Xvfb

%global _description %{expand:
Simplify the link between social and real identities
}

%description %{_description}


%prep
%autosetup -p1 sylva-%{version}

%generate_buildrequires
export PDM_BUILD_SCM_VERSION=v%{version}
%pyproject_buildrequires -t -x dev


%build
export PDM_BUILD_SCM_VERSION=v%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sylva

install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --name='%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/sylva.1' \
    '%{buildroot}%{_bindir}/sylva'


%check
%tox -e offline


%files -f %{pyproject_files}
%license LICENSE
%doc .github/README.md
%{_bindir}/sylva
%{_mandir}/man1/sylva.1*


%changelog
* Mon Jul 08 2024 Paul Pfeister <code@pfeister.dev> - 0.15.0-1
- Initial package.

