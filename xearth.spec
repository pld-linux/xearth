Summary:     Displays a lit globe in the background of your X screen
Summary(de): Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms 
Summary(fr): Affiche un globe terrestre illuminé dans le fond de votre écran X
Summary(pl): T³o w postaci animowanej kuli ziemskiej dla X Window System
Summary(tr): X ekranýnýzýn arkaplanýnda bir dünya görüntüsü
Name:        xearth
Version:     1.0
Release:     12
Copyright:   MIT
Group:       X11/Amusements
Source:      ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
Xearth displays a pseudo-3D globe that rotates to show the earth as it
actually is, including markers for major cities and PLD & RH :-).

%description -l de
Xearth stellt einen rotierenden pseudo-3D-Globus dar, auf dem
die wichtigsten Städte und PLD & RH eingezeichnet sind:-).

%description -l fr
Xearth affiche un globe en pseudo-3D qui tourne et montre la terre telle
qu'elle est sur le moment, avec les principales villes et...
PLD & RH :-).

%description -l pl
Xearth wy¶wietla pseudo-3D obracaj±c± siê w odstêpach czasowych kulê ziemska,
oraz punkty z zaznaczonymi najwiêkszymi aglomeracjami Ziemi. Pokazuje równie¿
gdzie znajduje siê PLD ;)

%description -l tr
xearth, dünyanýn o saatte güneþe göre durumunu ve üzerindeki belli baþlý
þehirleri grafik olarak gösterir. Özellikle X ortamýnda arka plan olarak
kullanýlmasý tavsiye edilir. Bu durumda her beþ dakikada bir arka plan resmi
kendisini güncelleyecektir.

%prep
%setup -q

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,man/man1}}

install xearth $RPM_BUILD_ROOT/usr/X11R6/bin
install xearth.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xearth.1

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xearth <<EOF
xearth name "xearth"
xearth description "xearth"
xearth group Amusements
xearth exec "xearth -fork"
EOF

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root,  man) /usr/X11R6/man/man1/*

%config /etc/X11/wmconfig/xearth

%changelog
* Wed Jan 06 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-12]
- removed patch,
- changed way of passing $RPM_OPT_FLAGS.

* Thu Jul 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- major changes && rewrote spec file.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
