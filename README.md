# QEP07 TIN Loader

**QEP07 TIN Loader** adds support for loading common engineering TIN formats in QGIS.  
This plugin was made to make flood modelling workflows (e.g. **TUFLOW**) a bit easier.  

- Open **12d (.12da)** and **SMS/XMS (.tin)** files as MDAL Mesh(.tin) layers.  
- Convert directly to **2DM** for full editing with **QGIS Mesh Digitizing tools**.  
- TUFLOW should be able to read **2DM** format directly.

**Tested with QGIS 3.34 and 3.40.**

---

**Future improvements:**  
- Handle different encoding (for now, modellers please do your own conversion to ANSI, untick *Full TIN* when exporting from 12d, etc.).  
- Support for more formats (e.g. `.12daz`, 3D faces in DWG/DXF).  
- Other interface improvements.  

---

**Status:** First release — feedback welcome!
