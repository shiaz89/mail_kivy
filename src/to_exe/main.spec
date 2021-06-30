# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['..\\main.py'],
             pathex=['to_exe'],
             binaries=[('../Tesseract-OCR/*', 'Tesseract-OCR'),
             ('../Tesseract-OCR/doc/*', 'Tesseract-OCR/doc'),
             ('../Tesseract-OCR/tessdata/*', 'Tesseract-OCR/tessdata'),],
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
          a.datas,
          [],
          name='mail sender',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )