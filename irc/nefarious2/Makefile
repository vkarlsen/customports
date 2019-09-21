# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=		nefarious2
PORTVERSION=		g20170923
CATEGORIES=		irc

MAINTAINER=		vidar@karlsen.tech
COMMENT=		Evilnet IRC daemon

LICENSE=		GPLv3

GNU_CONFIGURE=		yes

USES=			cpe
CPE_VENDOR=		nefarious2_project
USE_RC_SUBR=		nefarious2

USE_GITHUB=		yes
GH_ACCOUNT=		evilnet
GH_TAGNAME=		47c8bea

USERS=			ircd
GROUPS=			ircd

LOGDIR?=		/var/log/${PORTNAME}
RUNDIR?=		/var/run/${PORTNAME}
SUB_LIST=		LOGDIR=${LOGDIR} RUNDIR=${RUNDIR} PORTNAME=${PORTNAME}
SUB_FILES=		pkg-message

OPTIONS_DEFINE=		SSL DOCS GEOIP
OPTIONS_DEFAULT=	SSL
SSL_CONFIGURE_ENABLE=	ssl
SSL_USES=		ssl
GEOIP_CONFIGURE_ENABLE=	geoip
GEOIP_LIB_DEPENDS=	libGeoIP.so:net/GeoIP

.if defined(NEFARIOUS_DOMAIN)
CONFIGURE_ARGS+=	--with-domain=${NEFARIOUS_DOMAIN}
.endif

CONFIGURE_ARGS+=	--prefix=${PREFIX} \
			--with-cpath=${PREFIX}/etc/${PORTNAME}/ircd.conf \
			--with-dpath=${PREFIX}/etc/${PORTNAME} \
			--with-lpath=/var/log/${PORTNAME}/ircd.log \
			--localstatedir=/var/run/${PORTNAME}

post-patch:
	${REINPLACE_CMD} -e 's|ircd.log|/var/log/nefarious2/ircd.log|' ${WRKSRC}/doc/example.conf
	${REINPLACE_CMD} -e 's|PREFIX|${PREFIX}|' ${WRKSRC}/tools/makepem/makepem
	${REINPLACE_CMD} -e 's|PORTNAME|${PORTNAME}|' ${WRKSRC}/tools/makepem/makepem

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/${PORTNAME}
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/ircd ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/umkpasswd ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/ircd/convert-conf ${STAGEDIR}${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/doc/example.conf ${STAGEDIR}${PREFIX}/etc/${PORTNAME}/ircd.conf.sample
	${INSTALL_SCRIPT} ${WRKSRC}/tools/makepem/makepem ${STAGEDIR}${PREFIX}/etc/${PORTNAME}/

post-install-DOCS-on:
	cd ${WRKSRC}/doc && ${COPYTREE_SHARE} . ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
