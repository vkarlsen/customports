# $FreeBSD$

PORTNAME=	toybox
PORTVERSION=	0.8.1
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	All-in-one command line

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	bash:shells/bash gsed:textproc/gsed
LIB_DEPENDS=	libinotify.so:devel/libinotify

USES=		gmake

SHEBANG=	scripts/change.sh scripts/findglobals.sh \
		scripts/genconfig.sh scripts/install.sh \
		scripts/make.sh scripts/minicom.sh \
		scripts/portability.sh scripts/runtest.sh \
		scripts/single.sh scripts/test.sh configure

PLIST_FILES=	bin/toybox

USE_GITHUB=	yes
GH_ACCOUNT=	landley

post-patch:
.for f in ${SHEBANG}
	@${REINPLACE_CMD} -e 's|/bin/bash|${LOCALBASE}/bin/bash|' ${WRKSRC}/${f}
.endfor
	@${REINPLACE_CMD} -e 's|<sys/inotify.h>|"${LOCALBASE}/include/sys/inotify.h"|' \
		${WRKSRC}/lib/portability.c
	@${REINPLACE_CMD} -e 's|-Werror=implicit-function-declaration||' \
		${WRKSRC}/configure
	@${REINPLACE_CMD} -e 's|-Wundef||' ${WRKSRC}/configure

do-configure:
	cd ${WRKSRC} && ${GMAKE} bsd_defconfig

do-build:
	cd ${WRKSRC} && ${GMAKE}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/toybox ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
