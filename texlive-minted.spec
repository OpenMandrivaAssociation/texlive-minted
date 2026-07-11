%global tl_name minted
%global tl_revision 78270

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8.0
Release:	%{tl_revision}.1
Summary:	Highlighted source code for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minted
License:	lppl1.3c lppl1.3 bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minted.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(catchfile)
Requires:	texlive(etoolbox)
Requires:	texlive(float)
Requires:	texlive(fvextra)
Requires:	texlive(latex2pydata)
Requires:	texlive(minted.bin)
Requires:	texlive(newfloat)
Requires:	texlive(pdftexcmds)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(tools)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package that facilitates expressive syntax highlighting in LaTeX
using the powerful Pygments library. The package also provides options
to customize the highlighted source code output using fancyvrb.

