# ocr_study
A simple project to demo how to use python ocr lib to recognize text in pdf file

## How to install:
  1. Install tesseract(on Windows)
    > [!TIP] wiki url: https://github.com/UB-Mannheim/tesseract/wiki
    > [!TIP] donwload url: https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe
    > [!TIP] Install the downloaded binary file.
    > [!TIP] Install the python lib:
      ```bash
      pip install pytesseract
      ```
    > [!TIP] Set env path:
      add "C:/Program Files/Tesseract-OCR" to PATH
    > [!TIP] test installation:
      ```bash
      tesseract --version
      ```
  2. Install poppler(on Windows)
    > [!TIP] wiki url: https://github.com/oschwartz10612/poppler-windows
    > [!TIP] donwload url: https://github.com/oschwartz10612/poppler-windows/releases/download/v24.07.0-0/Release-24.07.0-0.zip
    > [!TIP] extract the downloaded file to "D:/tools/poppler/"
    > [!TIP] Set env path:
      add "D:/tools/poppler/Release-24.07.0-0/poppler-24.07.0/Library/bin" to PATH
    > [!TIP] test installation:
      ```bash
      pdftoppm -v
      ```
  3. Install required python libs:
    ```bash
    pip install pdf2image pillow
    ```
