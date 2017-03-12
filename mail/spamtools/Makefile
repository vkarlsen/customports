# $FreeBSD$

PORTNAME=	spamtools
PORTVERSION=	0.1
CATEGORIES=	mail
MASTER_SITES=	# none
DISTFILES=	# none

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Scripts for handling Postfix block lists

LICENSE=	BSD2CLAUSE

NO_BUILD=	yes
NO_ARCH=	yes

do-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/etc/traplists
	${INSTALL_SCRIPT} ${FILESDIR}/addspammer ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${FILESDIR}/fetchtraplist ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
