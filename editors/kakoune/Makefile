# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	kakoune
PORTVERSION=	0.0.1
CATEGORIES=	editors

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Vim-inspired, selection-oriented code editor

LICENSE=	UNLICENSE
LICENSE_NAME=	UNLICENSE
LICENSE_FILE=	${WRKSRC}/UNLICENSE
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

LIB_DEPENDS=	libboost_regex.so:devel/boost-libs
BUILD_DEPENDS=	${LOCALBASE}/include/boost/regex.hpp:devel/boost-libs	\
	${LOCALBASE}/bin/a2x:textproc/asciidoc	\
	${LOCALBASE}/bin/gmake:devel/gmake
.include <bsd.port.pre.mk>
.if (${OSVERSION} < 1100000)
BUILD_DEPENDS+=	${LOCALBASE}/bin/clang++38:lang/clang38

CXX=	clang++38
.endif

USES=	gmake ncurses

USE_GITHUB=	yes
GH_ACCOUNT=	mawww
GH_TAGNAME=	8703f30

DATADIR=	${PREFIX}/share/kak
DOCSDIR=	${PREFIX}/share/doc/kak

do-build:
	cd ${WRKSRC}/src && CXX=${CXX} ${GMAKE} && ${GMAKE} doc
	cd ${WRKSRC}/doc && a2x --no-xmllint -f manpage kak.1.txt && ${GZIP_CMD} kak.1

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}/rc/base
	${MKDIR} ${STAGEDIR}${DATADIR}/rc/core
	${MKDIR} ${STAGEDIR}${DATADIR}/rc/extra
	${MKDIR} ${STAGEDIR}${DATADIR}/colors
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${MKDIR} ${STAGEDIR}${DOCSDIR}/manpages
	${INSTALL_PROGRAM} ${WRKSRC}/src/kak ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/doc/kak.1.gz ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/doc/manpages/*.gz ${STAGEDIR}${DOCSDIR}/manpages
	${INSTALL_DATA} ${WRKSRC}/share/kak/kakrc ${STAGEDIR}${DATADIR}
	${INSTALL_DATA} ${WRKSRC}/rc/base/* ${STAGEDIR}${DATADIR}/rc/base
	${INSTALL_DATA} ${WRKSRC}/rc/core/* ${STAGEDIR}${DATADIR}/rc/core
	${INSTALL_DATA} ${WRKSRC}/rc/extra/* ${STAGEDIR}${DATADIR}/rc/extra
	${INSTALL_DATA} ${WRKSRC}/colors/* ${STAGEDIR}${DATADIR}/colors
	${INSTALL_DATA} ${WRKSRC}/README.asciidoc ${STAGEDIR}${DATADIR}

post-install:
	${LN} -Fs rc ${STAGEDIR}${DATADIR}/autoload

.include <bsd.port.post.mk>
