# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=		nefarious2
PORTVERSION=		g20170923
CATEGORIES=		irc

MAINTAINER=		vidar@karlsen.tech
COMMENT=		Evilnet IRC daemon

LICENSE=		GPLv3

GNU_CONFIGURE=		yes

USE_GITHUB=		yes
GH_ACCOUNT=		evilnet
GH_TAGNAME=		47c8bea

OPTIONS_DEFINE=		SSL DOCS GEOIP
SSL_CONFIGURE_ENABLE=	ssl
SSL_USES=		ssl
GEOIP_CONFIGURE_ENABLE=	geoip
GEOIP_LIB_DEPENDS=	libGeoIP.so:net/GeoIP

.if defined(NEFARIOUS_DOMAIN)
CONFIGURE_ARGS+=	--with-domain=${NEFARIOUS_DOMAIN}
.endif

CONFIGURE_ARGS+=	--prefix=${PREFIX} \
			--with-cpath=${PREFIX}/etc/${PORTNAME}/ircd.conf \
			--with-dpath=${PREFIX}/etc/${PORTNAME}

do-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/etc/${PORTNAME}
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/ircd ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/umkpasswd ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/convert-conf ${STAGEDIR}${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/doc/example.conf ${STAGEDIR}${PREFIX}/etc/${PORTNAME}/ircd.conf.sample

post-install-DOCS-on:
	cd ${WRKSRC}/doc && ${COPYTREE_SHARE} . ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
