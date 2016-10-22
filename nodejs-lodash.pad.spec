%{?scl:%scl_package nodejs-lodash.pad}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash.pad

%global npm_name lodash.pad
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash.pad
Version:	3.1.1
Release:	2%{?dist}
Summary:	The modern build of lodash’s `_.pad` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

BuildRequires:	%{?scl_prefix}npm(lodash._basetostring)
BuildRequires:	%{?scl_prefix}npm(lodash._createpadding)

Requires:	%{?scl_prefix}npm(lodash._basetostring)
Requires:	%{?scl_prefix}npm(lodash._createpadding)

%description
The modern build of lodash’s `_.pad` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/lodash.pad

%doc README.md LICENSE

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.1-2
- Use macro in -runtime dependency

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 3.1.1-1
- Initial build
