Name:		texlive-minted
Version:	2.5
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
%{_texmfdistdir}/tex/latex/minted
%doc %{_texmfdistdir}/doc/latex/minted
#- source
%doc %{_texmfdistdir}/source/latex/minted

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
