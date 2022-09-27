import qrcode

def qr_generator():
    
    text = str(input('\nEnter the text you want to encode: '))
    
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_M,
        box_size= 10,
        border= 4
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qrcode.png')
    
    print()
    print('QR code has been saved as "png" file.')

qr_generator()
