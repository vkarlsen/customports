# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	obmenu-generator
PORTVERSION=	0.84
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Menu generator for the Openbox Window Manager

LICENSE=	GPLv3

RUN_DEPENDS=	p5-Linux-DesktopFiles>=0.25:sysutils/p5-Linux-DesktopFiles \
		p5-Data-Dump>0:devel/p5-Data-Dump \
		p5-GDBM>0:databases/p5-GDBM

USES=		shebangfix perl5
SHEBANG_FILES=	*.pl obmenu-generator

USE_GITHUB=	yes
GH_ACCOUNT=	trizen

NO_BUILD=	yes
NO_ARCH=	yes

post-patch:
	${REINPLACE_CMD} -e 's|/etc/xdg/$$pkgname/schema.pl|${PREFIX}/etc/${PORTNAME}/schema.pl|' \
		${WRKSRC}/obmenu-generator
	${REINPLACE_CMD} -e 's|/usr/bin/perl|${PREFIX}/bin/perl|' \
		${WRKSRC}/obmenu-generator

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/obmenu-generator ${STAGEDIR}${PREFIX}/bin/
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/obmenu-generator
	${INSTALL_SCRIPT} ${WRKSRC}/schema.pl ${STAGEDIR}${PREFIX}/etc/obmenu-generator/

.include <bsd.port.mk>
