# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['..\\main.py'],
             pathex=['to_exe'],
             binaries=[('../../Tesseract-OCR/*', 'Tesseract-OCR')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          [],
          exclude_binaries=True,
          name='mail_img_text',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main',
               runtime_tmpdir=None,
               console=True)
