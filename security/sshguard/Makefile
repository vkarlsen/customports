# Created by: Mij <mij@bitchx.it>
# $FreeBSD: head/security/sshguard/Makefile 497110 2019-03-29 12:24:32Z garga $

PORTNAME=	sshguard
PORTVERSION=	2.4.0
CATEGORIES=	security
MASTER_SITES=	SF/sshguard/sshguard/${PORTVERSION}

MAINTAINER=	dan.mcgregor@usask.ca
COMMENT=	Protect hosts from brute-force attacks against SSH and other services

LICENSE=	BSD2CLAUSE

USE_RC_SUBR=	sshguard

GNU_CONFIGURE=	yes
SUB_FILES=	pkg-message

post-patch:
	@${REINPLACE_CMD} -e 's|%PREFIX%|${PREFIX}|' \
		${WRKSRC}/doc/sshguard.8.rst
	@${REINPLACE_CMD} -e 's|/usr/local|${PREFIX}|' \
		${WRKSRC}/examples/sshguard.conf.sample

post-install:
	${INSTALL} -d ${STAGEDIR}${PREFIX}/etc
	${INSTALL_DATA} ${WRKSRC}/examples/sshguard.conf.sample \
		${STAGEDIR}${PREFIX}/etc

.include <bsd.port.mk>
