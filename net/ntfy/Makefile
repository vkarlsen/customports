# This port is dirty.
# It requires poudriere.conf: ALLOW_NETWORKING_PACKAGES="ntfy"
# and it currently only works with amd64.
PORTNAME=	ntfy
DISTVERSIONPREFIX=	v
DISTVERSION=	2.11.0
CATEGORIES=	net

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Utility for sending push notifications
WWW=		https://ntfy.sh

LICENSE=	GPLv2

BUILD_DEPENDS=	git:devel/git goreleaser:devel/goreleaser npm:www/npm \
		sqlite3>0:databases/sqlite3

USES=		go:modules

GO_MODULE=	heckel.io/ntfy/v2
CGO_ENABLED=	1

do-build:
	${LN} -s ${LOCALBASE}/bin/go122 ${LOCALBASE}/bin/go
	cd ${WRKSRC} && make cli-linux-amd64 && make web
	${RM} ${LOCALBASE}/bin/go

do-install:
	${INSTALL} ${WRKSRC}/dist/ntfy_linux_amd64_freebsd_amd64_v1/ntfy \
		${STAGEDIR}${PREFIX}/bin/ntfy

.include <bsd.port.mk>
