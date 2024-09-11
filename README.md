# ocr_study
A simple project to demo how to use python ocr lib to recognize text in pdf file

## How to install:
  1. Install tesseract(on Windows)
  - [wiki url](https://github.com/UB-Mannheim/tesseract/wiki)
  - [donwload url](https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe)
  - Install the downloaded binary file.
  - Install the python lib:
    ```bash
    pip install pytesseract
    ```
  - Set env path:
    - add "C:/Program Files/Tesseract-OCR" to PATH
  - test installation:
    ```bash
    tesseract --version
    ```
  - create a "tessdata" folder
    ```bash
    d:
    md tessdata
    ```
  - set env virable:
    ```bash
    virable name: TESSDATA_PREFIX
    virable value: D:/tessdata
    ```
  - download language data for tesseract:
    ```bash
    d:
    cd tessdata
    wget https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata
    ```
  2. Install poppler(on Windows)
  - [wiki url](https://github.com/oschwartz10612/poppler-windows)
  - [donwload url](https://github.com/oschwartz10612/poppler-windows/releases/download/v24.07.0-0/Release-24.07.0-0.zip)
  - extract the downloaded file to "D:/tools/poppler/"
  - Set env path:
    - add "D:/tools/poppler/Release-24.07.0-0/poppler-24.07.0/Library/bin" to PATH
  - test installation:
    ```bash
    pdftoppm -v
    ```
  3. Install required python libs:
    - 
      ```bash
      pip install pdf2image pillow
      ```
