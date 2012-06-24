Summary:	Displays a lit globe in the background of your X screen
Summary(de):	Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms
Summary(es):	Ense�a un globo terrestre, como tapiz de fondo, de tu pantalla X
Summary(fr):	affiche en 3D la terre vue du soleil en fonds d'�cran
Summary(pl):	T�o w postaci animowanej kuli ziemskiej dla X Window System
Summary(pt_BR):	Mostra um globo terrestre em pano de fundo de seu tela X
Summary(tr):	X ekran�n�z�n arkaplan�nda bir d�nya g�r�nt�s�
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
Xearth ense�a un globo pseudo 3D que cumple un movimiento de rotaci�n
para ense�ar la tierra como realmente es, mostrando marcas en ciudades
principales, y en RedHat Software y Conectiva tambi�n :-))

%description -l de
Xearth stellt einen rotierenden pseudo-3D-Globus dar, auf dem die
wichtigsten St�dte und PLD & RH eingezeichnet sind:-).

%description -l fr
Xearth est un programme pour le syst�me X Window qui affiche le globe
terrestre en 3D, tel qui l'est vu du soleil (avec ombrage). Les
continents sont parsem�es par des points indiquant les grandes villes
ainsi.

%description -l pl
Xearth wy�wietla pseudo-3D obracaj�c� si� w odst�pach czasowych kul�
ziemska, oraz punkty z zaznaczonymi najwi�kszymi aglomeracjami Ziemi.

%description -l pt_BR
Xearth mostra um globo pseudo-3D que rotaciona para mostrar a terra
como ela realmente �, mostrando marcas para cidades principais, RedHat
Software e a Conectiva tamb�m :-))

%description -l tr
xearth, d�nyan�n o saatte g�ne�e g�re durumunu ve �zerindeki belli
ba�l� �ehirleri grafik olarak g�sterir. �zellikle X ortam�nda arka
plan olarak kullan�lmas� tavsiye edilir. Bu durumda her be� dakikada
bir arka plan resmi kendisini g�ncelleyecektir.

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
