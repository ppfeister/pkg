# Packager: Paul Pfeister <ppfeister@fedoraproject.org> (GitHub @ppfeister)
Name:           sherlock-project
Version:        0.14.4
Release:        1%{?dist}
Summary:        Hunt down social media accounts by username across social networks

License:        MIT
URL:            https://github.com/sherlock-project/sherlock
Source:         %{url}/archive/master.tar.gz
# Switch to new Source URL after adoption of tagged releases

# Fedora compatibility (upstream dependency change planned)
Patch0:         https://raw.githubusercontent.com/ppfeister/pkg/master/sherlock/0001-Remove-tor.patch
#TODO All paths within repo will change to sherlock-project or sherlock_project at 0.15.0


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man


%global _description %{expand:
Hunt down social media accounts by username across 400+ social networks and
websites. New targets are tested and implemented regularly.
}

%description %{_description}


%prep
%autosetup -p1 -n sherlock-master
sed -i '/torrequest/d' 'pyproject.toml' # Pending upstream changes with Patch0

%generate_buildrequires
%pyproject_buildrequires -t -x dev


%build
# Project now uses Poetry and dynamic versioning, so pyproject version is 0
# __init__ is currently the single source of truth for version info
sherlock_version=$(sed -n 's/^__version__ *= *"\([0-9.]*\)"/\1/p' sherlock/__init__.py)
sed -r -i "s/^version *= .*?$/version = \"$sherlock_version\"/" pyproject.toml
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L sherlock

sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock/__main__.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock/sherlock.py'

install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --name='%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/sherlock.1' \
    '%{buildroot}%{_bindir}/sherlock'


%check
%tox -e offline


%files -f %{pyproject_files}
%license LICENSE
%doc docs/README.md
%{_bindir}/sherlock
%{_mandir}/man1/sherlock.1*


%changelog
* Tue Jun 26 2024 Paul Pfeister <code@pfeister.dev> 0.14.4-1
- Initial package.
