Summary:	Displays a lit globe in the background of your X screen
Summary(de):	Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms
Summary(es):	Enseña un globo terrestre, como tapiz de fondo, de tu pantalla X
Summary(fr):	affiche en 3D la terre vue du soleil en fonds d'écran
Summary(pl):	T³o w postaci animowanej kuli ziemskiej dla X Window System
Summary(pt_BR):	Mostra um globo terrestre em pano de fundo de seu tela X
Summary(tr):	X ekranýnýzýn arkaplanýnda bir dünya görüntüsü
Name:		xearth
Version:	1.1
Release:	6
License:	MIT
Group:		X11/Amusements
Source0:	ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
Xearth is an X Window System based graphic that shows a globe of the
Earth, including markers for major cities. The Earth is correctly
shaded for the current position of the sun, and the displayed image is
updated every five minutes.

%description -l es
Xearth enseña un globo pseudo 3D que cumple un movimiento de rotación
para enseñar la tierra como realmente es, mostrando marcas en ciudades
principales, y en RedHat Software y Conectiva también :-))

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

%description -l pt_BR
Xearth mostra um globo pseudo-3D que rotaciona para mostrar a terra
como ela realmente é, mostrando marcas para cidades principais, RedHat
Software e a Conectiva também :-))

%description -l tr
xearth, dünyanýn o saatte güneþe göre durumunu ve üzerindeki belli
baþlý þehirleri grafik olarak gösterir. Özellikle X ortamýnda arka
plan olarak kullanýlmasý tavsiye edilir. Bu durumda her beþ dakikada
bir arka plan resmi kendisini güncelleyecektir.

%prep
%setup -q

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Amusements,%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
