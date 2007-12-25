# TODO:
# - finish pl :)
Summary:	List of country and language names
Summary(pl.UTF-8):	Lista nazw krajów i języków
Name:		iso-codes
Version:	1.7
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/%{name}-%{version}.tar.bz2
# Source0-md5:	d827155521f4f9baf3fbece2f4bc1985
Patch0:		%{name}-pl.patch
URL:		http://pkg-isocodes.alioth.debian.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	python-PyXML
Requires:	FHS >= 2.3-16
Conflicts:	pkgconfig < 1:0.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	%{_datadir}/pkgconfig

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%description -l pl.UTF-8
Celem tego pakietu jest dostarczenie list nazw krajów i języków (oraz
walut) w jednym miejscu, zamiast powtarzania ich w wielu programach.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{dv,haw,kok,ps,syr}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/iso-codes
%{_datadir}/xml/iso-codes
%{_noarchpkgconfigdir}/iso-codes.pc
