Summary:	Displays a lit globe in the background of your X screen
Summary(de):	Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms 
Summary(fr):	affiche en 3D la terre vue du soleil en fonds d'écran
Summary(pl):	T³o w postaci animowanej kuli ziemskiej dla X Window System
Summary(tr):	X ekranýnýzýn arkaplanýnda bir dünya görüntüsü
Name:		xearth
Version:	1.1
Release:	2
License:	MIT
Group:		X11/Amusements
Group(pl):	X11/Rozrywka
Source0:	ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.gz
Source1:	xearth.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
Xearth is an X Window System based graphic that shows a globe of the
Earth, including markers for major cities. The Earth is correctly
shaded for the current position of the sun, and the displayed image is
updated every five minutes.

%description -l de
Xearth stellt einen rotierenden pseudo-3D-Globus dar, auf dem die
wichtigsten Städte und PLD & RH eingezeichnet sind:-).

%description -l fr
Xearth est un programme pour le système X Window qui affiche le globe
terrestre en 3D, tel qui l'est vu du soleil (avec ombrage). Les
continents sont parsemées par des points indiquant les grandes villes
ainsi.

%description -l pl
Xearth wy¶wietla pseudo-3D obracaj±c± siê w odstêpach czasowych kulê
ziemska, oraz punkty z zaznaczonymi najwiêkszymi aglomeracjami Ziemi.

%description -l tr
xearth, dünyanýn o saatte güneþe göre durumunu ve üzerindeki belli
baþlý þehirleri grafik olarak gösterir. Özellikle X ortamýnda arka
plan olarak kullanýlmasý tavsiye edilir. Bu durumda her beþ dakikada
bir arka plan resmi kendisini güncelleyecektir.

%prep
%setup -q

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/Amusements

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%{_applnkdir}/Amusements/*
