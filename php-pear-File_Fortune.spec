%define		_class		File
%define		_subclass	Fortune
%define		_status		stable
%define		_pearname	File_Fortune

Summary:	%{_pearname} - interface for reading from and writing to fortune files
Summary(pl.UTF-8):	%{_pearname} - interfejs do odczytu i zapisywania plików fortunek
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	790f547447ade697d4227eca00107dec
URL:		http://pear.php.net/package/File_Fortune/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1.3.4
Obsoletes:	php-pear-File_Fortune-tests
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

%description -l pl.UTF-8
File_Fortune dostarcza interfejs PHP do odczytu plików z fortunkami.
Przy jego użyciu możliwe jest odczytanie pojedynczej lub losowej
fortunki, jak również wszystkie fortunki z pliku.

File_Fortune_Writer dostarcza interfejs do obróbki zawartości pliku z
fortunkami. Pozwala na zapisywanie do pliku zestawu fortunek jak
również odpowiedniego binarnego nagłówka. Możliwe jest także
dodawanie, usuwanie lub modyfikowanie poszczególnych fortunek.
Operacje zapisu stworzą binarny plik z nagłówkami pozwalający na
większą zgodność z plikami fortune i fortune-mod (jak również z innymi
interfejsami do fortunek).

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
%doc install.log docs/%{_pearname}/tutorials/File_Fortune.cls
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/data/%{_pearname}
%{php_pear_dir}/File/Fortune
%{php_pear_dir}/File/Fortune.php
