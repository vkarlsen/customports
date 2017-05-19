# Custom patch set by Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	lspu
PORTVERSION=	0.0.1
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Lists running processes using given binaries or libraries

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	606u
GH_TAGNAME=	428999d

PLIST_FILES=	sbin/lspu

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/lspu ${STAGEDIR}${PREFIX}/sbin

.include <bsd.port.mk>
