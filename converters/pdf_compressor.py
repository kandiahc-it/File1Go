# import subprocess

# def compress_pdf(input_path, output_path):
#     command = [
#         "gswin64c",   # use 'gs' on Linux
#         "-sDEVICE=pdfwrite",
#         "-dCompatibilityLevel=1.4",
#         "-dPDFSETTINGS=/ebook",
#         "-dNOPAUSE",
#         "-dQUIET",
#         "-dBATCH",
#         f"-sOutputFile={output_path}",
#         input_path
#     ]

#     subprocess.run(command, check=True)






import fitz
import io

def compress_pdf(input_path, output_path):
    doc = fitz.open(input_path)

    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Open image using fitz.Pixmap from memory bytes
            pix = fitz.Pixmap(image_bytes)

            if pix.n > 4:  # Convert CMYK to RGB if necessary
                pix = fitz.Pixmap(fitz.csRGB, pix)

            # Compress image in memory
            buffer = io.BytesIO()
            # Save compacted image to buffer using tobytes which supports quality
            buffer.write(pix.tobytes("jpeg", jpg_quality=40)) 
            buffer.seek(0)
            
            # Update the PDF stream with the compressed data
            doc.update_stream(xref, buffer.getvalue())
            
            # Update the object attributes to match the new JPEG data
            doc.xref_set_key(xref, "Filter", "/DCTDecode")
            doc.xref_set_key(xref, "ColorSpace", "/DeviceRGB")  # We converted to RGB or kept it compatible

    # Save optimized PDF
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()
