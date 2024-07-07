import PyPDF2

def remove_pdf_password(input_pdf, output_pdf):
    password = input("Enter password for the PDF (leave empty if none): ").strip()
    
    # Open the encrypted PDF
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Try to decrypt with the provided password or an empty password
            if reader.decrypt(password):
                print(f"Password removed successfully from {input_pdf}.")
                # Create a writer object
                writer = PyPDF2.PdfWriter()
                
                # Add all pages to writer
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])
                
                # Write all pages to output PDF
                with open(output_pdf, 'wb') as output_file:
                    writer.write(output_file)
                
                print(f"Saved decrypted PDF as {output_pdf}.")
            else:
                print(f"Password removal failed for {input_pdf}. Password may be incorrect.")
        else:
            print(f"{input_pdf} is not password protected. No action taken.")

# Example usage:
if __name__ == "__main__":
    input_pdf = "re.pdf"  # Replace with the path to your encrypted PDF file
    output_pdf = "decrypted.pdf"  # Replace with the path where you want to save the decrypted PDF
    
    remove_pdf_password(input_pdf, output_pdf)
