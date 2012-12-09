# revision 24002
# category Package
# catalog-ctan /macros/latex/contrib/minted
# catalog-date 2011-09-18 00:13:37 +0200
# catalog-license lppl1.3
# catalog-version 1.7
Name:		texlive-minted
Version:	1.7
Release:	2
Summary:	Highlighted source code for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minted
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package that facilitates expressive syntax highlighting in
LaTeX using the powerful Pygments library. The package also
provides options to customize the highlighted source code
output using fancyvrb.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minted/minted.sty
%doc %{_texmfdistdir}/doc/latex/minted/Makefile
%doc %{_texmfdistdir}/doc/latex/minted/README
%doc %{_texmfdistdir}/doc/latex/minted/minted.pdf
#- source
%doc %{_texmfdistdir}/source/latex/minted/minted.dtx
%doc %{_texmfdistdir}/source/latex/minted/minted.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-2
+ Revision: 754014
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7-1
+ Revision: 719039
- texlive-minted
- texlive-minted
- texlive-minted
- texlive-minted

