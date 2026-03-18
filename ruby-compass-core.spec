#
# Conditional build:
%bcond_with     tests           # build without tests

%define pkgname compass-core
Summary:	The Compass core stylesheet library
Name:		ruby-%{pkgname}
Version:	1.0.3
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	561bc7f5597bfef532eae016e4510cd8
URL:		http://compass-style.org/reference/compass/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-rake
%endif
Requires:	ruby-multi_json >= 1.0
Requires:	ruby-sass >= 3.3.0
Requires:	ruby-sass < 3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compass core stylesheet library and minimum required ruby
extensions. This library can be used stand-alone without the compass
ruby configuration file or compass command line tools.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/compass-core.rb
%{ruby_vendorlibdir}/compass
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
