%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Numerical
%define		_subsubclass	RootFinding
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_subsubclass}

Summary:	%{_pearname} - numerical analysis root finding methods
Summary(pl):	%{_pearname} - metody numeryczne znajdowania pierwiastków
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3495ca09b22910b6b98ea8bd558fc7f9
URL:		http://pear.php.net/package/Math_Numerical_RootFinding/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Ten pakiet udostêpnia ró¿ne metody numeryczne do znajdowania
pierwiastków. Dostêpne metody to:
- bisekcji
- regula-falsi
- sta³ego przecinka
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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/%{_subsubclass}
