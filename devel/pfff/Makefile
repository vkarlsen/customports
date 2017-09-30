# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=		pfff
PORTVERSION=		0.29
DISTVERSIONPREFIX=	v
CATEGORIES=		devel

MAINTAINER=		vidar@karlsen.tech
COMMENT=		Tools for code analysis

LICENSE=		LGPL21
LICENSE_FILE=		${WRKSRC}/license.txt

BUILD_DEPENDS=		gcc:lang/gcc ocaml:lang/ocaml camlp4:devel/ocaml-camlp4

USES=			gmake perl5 shebangfix
SHEBANG_FILES=		${WRKSRC}/configure

USE_GCC=		yes
USE_GITHUB=		yes
GH_ACCOUNT=		facebook

do-build:
	cd ${WRKSRC} && \
	./configure --prefix=${PREFIX} && \
	${GMAKE} depend && \
	${GMAKE} && \
	${GMAKE} opt

post-install:
.for l in pfff sgrep spatch stags scheck codequery codeslicer pfff_db pfff_test
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/${l}
.endfor

.include <bsd.port.mk>
