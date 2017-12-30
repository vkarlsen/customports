# Created by: Sergey Matveev <stargrave@stargrave.org>
# $FreeBSD$

PORTNAME=	nncp
PORTVERSION=	2.0
PORTREVISION=	1
CATEGORIES=	net
MASTER_SITES=	http://www.nncpgo.org/download/

MAINTAINER=	stargrave@stargrave.org
COMMENT=	Utilities for secure store-and-forward files and mail exchanging

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	go:lang/go

USES=		tar:xz
MAKEFILE=	BSDmakefile

USE_RC_SUBR=	nncp-caller nncp-daemon nncp-toss
REQUIRE=	DAEMON

SUB_FILES=	pkg-message pkg-install pkg-deinstall nncp.newsyslog.conf.sample

PORTDOCS=	AUTHORS NEWS NEWS.RU README README.RU THANKS
INFO=		nncp
INSTALL_TARGET=	install-strip

post-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/nncp.newsyslog.conf.sample ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d/nncp.conf.sample

.include <bsd.port.mk>
