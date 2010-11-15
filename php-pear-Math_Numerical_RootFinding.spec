%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Math_Numerical_RootFinding
%define		subver	a2
%define		rel		1
Summary:	%{_pearname} - numerical analysis root finding methods
Summary(pl.UTF-8):	%{_pearname} - metody numeryczne znajdowania pierwiastków
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	770feb76b87ef10d33199cf27cc89440
URL:		http://pear.php.net/package/Math_Numerical_RootFinding/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provide various numerical analysis methods for find root
Available Methods:
- Bisection
- False Position
- Fixed Point
- Newton-Raphson
- Secant

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet udostępnia różne metody numeryczne do znajdowania
pierwiastków. Dostępne metody to:
- bisekcji
- regula-falsi
- stałego przecinka
- Newtona-Raphsona
- siecznych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

rm .%{php_pear_dir}/buildPackageXML.php

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Math/Numerical
%{php_pear_dir}/Math/Numerical/RootFinding.php
%{php_pear_dir}/Math/Numerical/RootFinding

%{_examplesdir}/%{name}-%{version}
