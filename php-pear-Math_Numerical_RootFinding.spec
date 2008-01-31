%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Numerical
%define		_subsubclass	RootFinding
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_%{_subsubclass}

Summary:	%{_pearname} - numerical analysis root finding methods
Summary(pl.UTF-8):	%{_pearname} - metody numeryczne znajdowania pierwiastków
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c7844e254e232f9bfa4ba53748a47045
URL:		http://pear.php.net/package/Math_Numerical_RootFinding/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-common >= 3:4.2.0
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/%{_subsubclass}
