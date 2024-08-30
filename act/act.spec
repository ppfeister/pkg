# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/nektos/act
%global goipath         github.com/nektos/act
Version:                0.2.65

%gometa -L -f

%global _description %{expand:
Run your GitHub Actions locally.
}

%global golicenses      LICENSE pkg/lookpath/LICENSE
%global godocs          README.md

Name:           golang-github-nektos-act
Release:        %autorelease
Summary:        Run your GitHub Actions locally 🚀

License:        MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND ISC
URL:            %{gourl}
Source:         %{gosource}

%description %{_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/act %{goipath}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE pkg/lookpath/LICENSE
%doc README.md
%{_bindir}/act
%endif

%gopkgfiles

%changelog
%autochangelog
