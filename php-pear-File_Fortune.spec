%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Fortune
%define		_status		beta
%define		_pearname	File_Fortune

Summary:	%{_pearname} - interface for reading from and writing to fortune files
Summary(pl):	%{_pearname} - interfejs do odczytu i zapisywania plików fortunek
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c4769e79b5f5063aabb18132d57f31f9
URL:		http://pear.php.net/package/File_Fortune/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Fortune provides a PHP interface to reading fortune files. With
it, you may retrieve a single fortune, a random fortune, or all
fortunes in the file.

File_Fortune_Writer provides an interface for manipulating the
contents of a fortune file. It allows you to write a complete fortune
file and the associated binary header file from an array of fortunes.
You may also add fortunes, delete fortunes, or update individual
fortunes in a fortune file. All write operations will produce a binary
header file to allow for greater compatability with the fortune and
fortune-mod programs (as well as other fortune interfaces).

In PEAR status of this package is: %{_status}.

%description -l pl
File_Fortune dostarcza interfejs PHP do odczytu plików z fortunkami.
Przy jego u¿yciu mo¿liwe jest odczytanie pojedynczej lub losowej
fortunki, jak równie¿ wszystkie fortunki z pliku.

File_Fortune_Writer dostarcza interfejs do obróbki zawarto¶ci pliku z
fortunkami. Pozwala na zapisywanie do pliku zestawu fortunek jak
równie¿ odpowiedniego binarnego nag³ówka. Mo¿liwe jest tak¿e
dodawanie, usuwanie lub modyfikowanie poszczególnych fortunek.
Operacje zapisu stworz± binarny plik z nag³ówkami pozwalaj±cy na
wiêksz± zgodno¶æ z plikami fortune i fortune-mod (jak równie¿ z innymi
interfejsami do fortunek).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc install.log docs/%{_pearname}/File/tutorials/File_Fortune/File_Fortune.cls
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/File/Fortune
%dir %{php_pear_dir}/File/Fortune/examples
%{php_pear_dir}/File/Fortune/examples/phpFortune
%{php_pear_dir}/File/Fortune/Exception.php
%{php_pear_dir}/File/Fortune/Writer.php
%{php_pear_dir}/File/Fortune.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/File_Fortune/
