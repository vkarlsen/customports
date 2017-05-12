# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	mudsh
PORTVERSION=	1.3.1
DISTVERSIONPREFIX=	v
CATEGORIES=	shells

MAINTAINER=	vidar@karlsen.tech
COMMENT=	MUD-inspired shell

USE_GITHUB=	yes
GH_ACCOUNT=	vkarlsen

NO_BUILD=	yes
NO_ARCH=	yes

USES=	shebangfix perl5
SHEBANG_LANG=	perl
SHEBANG_FILES=	*.pl

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/mudsh.pl ${STAGEDIR}${PREFIX}/bin/mudsh

.include <bsd.port.mk>
