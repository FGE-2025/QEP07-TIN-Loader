# -*- coding: utf-8 -*-
def classFactory(iface):
    from .qep07_loader import Qep07LoaderPlugin
    return Qep07LoaderPlugin(iface)
