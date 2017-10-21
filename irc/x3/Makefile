# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	x3
PORTVERSION=	1.9
CATEGORIES?=	irc

MAINTAINER=	vidar@karlsen.tech
COMMENT=	IRC services for Nefarious IRCu P10 networks

LICENSE=	GPLv3

LIB_DEPENDS=	libtre.so:textproc/libtre
BUILD_DEPENDS=	${PREFIX}/include/tre/regex.h:textproc/libtre gcc:lang/gcc

USES=		gmake compiler:gcc-c++11-lib
GNU_CONFIGURE=	yes

USE_GITHUB=	yes
GH_ACCOUNT=	evilnet

OPTIONS_DEFINE=	MODULES
OPTIONS_SUB=	yes
OPTIONS_DEFAULT=	#
MODULES_DESC=	Build extra modules (helpserv, memoserv)

include bsd.port.options.mk

.if ${PORT_OPTIONS:MMODULES}
CONFIGURE_ARGS+=	--enable-modules=memoserv,helpserv
PLIST_SUB+=	MODULES=""
RUN_DEPENDS+=	python2:lang/python2
USES+=		shebangfix
SHEBANG_LANG=	python
python_CMD=	${LOCALBASE}/bin/python2
SHEBANG_FILES=	src/modpython.py
MODS=	1
.else
PLIST_SUB+=	MODULES="@comment "
MODS=		0
.endif

do-configure:
	cd ${WRKSRC} && \
	./configure --prefix=${PREFIX}/x3 --with-tre=${PREFIX} ${CONFIGURE_ARGS}

do-build:
	cd ${WRKSRC} && \
	${GMAKE}

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/x3
	${INSTALL_PROGRAM} ${WRKSRC}/src/x3 ${STAGEDIR}${PREFIX}/x3/
	${INSTALL_DATA} ${WRKSRC}/src/*.help ${STAGEDIR}${PREFIX}/x3/
	${INSTALL_DATA} ${WRKSRC}/x3.conf.example ${STAGEDIR}${PREFIX}/x3/x3.conf.sample
	${INSTALL_DATA} ${WRKSRC}/sockcheck.conf.example ${STAGEDIR}${PREFIX}/x3/sockcheck.conf.sample
	if [ ${MODS} = 1 ] ; then \
		${MKDIR} ${STAGEDIR}${PREFIX}/x3/plugins; \
		${MKDIR} ${STAGEDIR}${PREFIX}/x3/plugins/hangman; \
		${MKDIR} ${STAGEDIR}${PREFIX}/x3/plugins/annoy; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/modpython.py ${STAGEDIR}${PREFIX}/x3/; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/__init__.py ${STAGEDIR}${PREFIX}/x3/plugins; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/README ${STAGEDIR}${PREFIX}/x3/plugins; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/hangman/__init__.py ${STAGEDIR}${PREFIX}/x3/plugins/hangman/; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/hangman/plugin.py ${STAGEDIR}${PREFIX}/x3/plugins/hangman/; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/annoy/__init__.py ${STAGEDIR}${PREFIX}/x3/plugins/annoy/; \
		${INSTALL_SCRIPT} ${WRKSRC}/src/plugins/annoy/plugin.py ${STAGEDIR}${PREFIX}/x3/plugins/annoy/; \
	fi

.include <bsd.port.mk>
