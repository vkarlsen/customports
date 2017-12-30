# Created by: Douglas Thrift
# $FreeBSD: head/sysutils/dtpstree/Makefile 432284 2017-01-23 18:52:15Z sunpoet $

PORTNAME=	dtpstree
PORTVERSION=	1.0.3
PORTREVISION=	1
CATEGORIES=	sysutils
MASTER_SITES=	http://dl1.douglasthrift.net/${PORTNAME}/ \
		http://dl2.douglasthrift.net/${PORTNAME}/

MAINTAINER=	douglas@douglasthrift.net
COMMENT=	Display a tree of processes

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

GNU_CONFIGURE=	yes
MAKEFILE=	GNUmakefile
USES=		gmake ncurses tar:xz

PLIST_FILES=	bin/dtpstree \
		bin/pstree \
		man/man1/dtpstree.1.gz

post-install:
	${RLN} -s ${STAGEDIR}${PREFIX}/bin/dtpstree ${STAGEDIR}${PREFIX}/bin/pstree

.include <bsd.port.mk>
