# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	mgba
PORTVERSION=	0.5.2
CATEGORIES=	emulators

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Game Boy Advance Emulator

LICENSE=	MPL
LICENSE_FILE=	${WRKSRC}/LICENSE

INSTALLS_ICONS=	yes

LIB_DEPENDS=	libepoxy.so:graphics/libepoxy \
				libavcodec.so:multimedia/ffmpeg \
				libavformat.so:multimedia/ffmpeg \
				libavresample.so:multimedia/ffmpeg \
				libavutil.so:multimedia/ffmpeg \
				libswscale.so:multimedia/ffmpeg \
				libMagickWand-6.so:graphics/ImageMagick \
				libMagickCore-6.so:graphics/ImageMagick \
				libpng16.so:graphics/png \
				libzip.so:archivers/libzip

USES=	cmake:outsource libedit

USE_GITHUB=	yes
GH_ACCOUNT=	mgba-emu

USE_SDL=	sdl2
USE_GL=		glu gl
USE_QT5=	qmake opengl network widgets gui core buildtools linguisttools

do-build:
	${MKDIR} ${WRKSRC}/build && \
	cd ${WRKSRC}/build && \
	cmake -DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} .. && \
	make

do-install:
	${INSTALL_LIB} ${WRKSRC}/build/libmgba.so.0.5.2 ${STAGEDIR}${PREFIX}/lib/libmgba.so.0.5.2
	${LN} -sf libmgba.so.0.5.2 ${STAGEDIR}${PREFIX}/lib/libmgba.so.0.5
	${LN} -sf libmgba.so.0.5 ${STAGEDIR}${PREFIX}/lib/libmgba.so
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/16x16/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/24x24/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/32x32/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/48x48/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/64x64/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/96x96/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/128x128/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/256x256/apps
	${MKDIR} ${STAGEDIR}${PREFIX}/share/icons/hicolor/512x512/apps
	${INSTALL_DATA} ${WRKSRC}/res/mgba-16.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/16x16/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-24.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/24x24/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-32.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/32x32/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-48.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/48x48/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-64.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/64x64/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-96.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/96x96/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-128.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/128x128/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-256.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/256x256/apps/mgba.png
	${INSTALL_DATA} ${WRKSRC}/res/mgba-512.png ${STAGEDIR}${PREFIX}/share/icons/hicolor/512x512/apps/mgba.png
	${MKDIR} ${STAGEDIR}${PREFIX}/${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README.md ${STAGEDIR}${PREFIX}/${DOCSDIR}/README.md
	${INSTALL_DATA} ${WRKSRC}/CHANGES ${STAGEDIR}${PREFIX}/${DOCSDIR}/CHANGES
	${INSTALL_PROGRAM} ${WRKSRC}/build/sdl/mgba ${STAGEDIR}${PREFIX}/bin/mgba
	${INSTALL_MAN} ${WRKSRC}/doc/mgba.6 ${STAGEDIR}${PREFIX}/man/man6/mgba.6
	${MKDIR} ${STAGEDIR}${PREFIX}/share/mgba/shaders/agb001.shader
	${INSTALL_DATA} ${WRKSRC}/res/shaders/agb001.shader/manifest.ini ${STAGEDIR}${PREFIX}/share/mgba/shaders/agb001.shader/manifest.ini
	${INSTALL_DATA} ${WRKSRC}/res/shaders/agb001.shader/agb001.fs ${STAGEDIR}${PREFIX}/share/mgba/shaders/agb001.shader/agb001.fs
	${MKDIR} ${STAGEDIR}${PREFIX}/share/mgba/shaders/xbr.shader
	${INSTALL_DATA} ${WRKSRC}/res/shaders/xbr.shader/manifest.ini ${STAGEDIR}${PREFIX}/share/mgba/shaders/xbr.shader/manifest.ini
	${INSTALL_DATA} ${WRKSRC}/res/shaders/xbr.shader/xbr.vs ${STAGEDIR}${PREFIX}/share/mgba/shaders/xbr.shader/xbr.vs
	${INSTALL_DATA} ${WRKSRC}/res/shaders/xbr.shader/xbr.fs ${STAGEDIR}${PREFIX}/share/mgba/shaders/xbr.shader/xbr.fs
	${MKDIR} ${STAGEDIR}${PREFIX}/share/mgba/shaders/ags001.shader
	${INSTALL_DATA} ${WRKSRC}/res/shaders/ags001.shader/ags001.fs ${STAGEDIR}${PREFIX}/share/mgba/shaders/ags001.shader/ags001.fs
	${INSTALL_DATA} ${WRKSRC}/res/shaders/ags001.shader/ags001-light.fs ${STAGEDIR}${PREFIX}/share/mgba/shaders/ags001.shader/ags001-light.fs
	${INSTALL_DATA} ${WRKSRC}/res/shaders/ags001.shader/manifest.ini ${STAGEDIR}${PREFIX}/share/mgba/shaders/ags001.shader/manifest.ini
	${MKDIR} ${STAGEDIR}${PREFIX}/share/mgba/shaders/pixelate.shader
	${INSTALL_DATA} ${WRKSRC}/res/shaders/pixelate.shader/manifest.ini ${STAGEDIR}${PREFIX}/share/mgba/shaders/pixelate.shader/manifest.ini
	${INSTALL_DATA} ${WRKSRC}/res/nointro.dat ${STAGEDIR}${PREFIX}/share/mgba/nointro.dat
	${INSTALL_PROGRAM} ${WRKSRC}/build/qt/mgba-qt ${STAGEDIR}${PREFIX}/bin/mgba-qt
	${INSTALL_MAN} ${WRKSRC}/doc/mgba-qt.6 ${STAGEDIR}${PREFIX}/man/man6/mgba-qt.6

.include <bsd.port.mk>
