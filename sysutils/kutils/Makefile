# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	kutils
PORTVERSION=	1.0
CATEGORIES=	sysutils
MASTER_SITES=	# none
DISTFILES=	# none

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Home-grown utilities

LICENSE=	BSD3CLAUSE

NO_BUILD=	yes
NO_ARCH=	yes

PLIST_FILES=	bin/tree

do-install:
	${INSTALL_SCRIPT} ${FILESDIR}/tree ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
