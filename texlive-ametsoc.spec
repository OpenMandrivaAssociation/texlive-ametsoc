Name:		texlive-ametsoc
Version:	4.3.2
Release:	3
Summary:	Official American Meteorological Society Latex Template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ametsoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ametsoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ametsoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains all the files necessary to write an
article using latex for the American Meteorological Society
journals. The article and bibliography style files are provided
along with two PDFs describing the use of the files and a blank
template for authors to use in writing their article. Also
available is a separate style file used to format a two-column,
journal page layout draft for the author's personal use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ametsoc
%{_texmfdistdir}/tex/latex/ametsoc
%doc %{_texmfdistdir}/doc/latex/ametsoc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
