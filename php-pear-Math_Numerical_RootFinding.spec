%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Numerical
%define		_subsubclass	RootFinding
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_subsubclass}

Summary:	%{_pearname} - numerical analysis root finding methods
Summary(pl):	%{_pearname} - metody numeryczne znajdowania pierwiastków
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2aa5cbd9153c4ce3f914a6e79427970a
URL:		http://pear.php.net/package/Math_Numerical_RootFinding/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/%{_subsubclass}

install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/%{_subsubclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/%{_subsubclass}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/%{_subsubclass}
