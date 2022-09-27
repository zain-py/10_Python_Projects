from PIL import Image


while True:
    
    file = input('\nEnter the file name and Extension: ')
    image_name = str(file)
    
    try:
        image = Image.open(image_name)
    except FileNotFoundError:
        print()
        print('[Error]: File in not present in the directory.')    
        break
    
    print(f'\nCurrent size of "{image_name}": {image.size}')
    
    resizer = input('\nDo You want to resize the image? [y/n]: ').lower()
    
    if resizer == 'y':
        width = int(input('Enter desired width:'))
        height = int(input('Enter desired height: '))
    else:
        break
    
    resized_image = image.resize((width, height))
    print(f'\nNew size of image: {resized_image.size}')
    
    new_name = input('\nSave image as [file_name.extension]: ')

    resized_image.save(new_name)
    
    print(f'\nImage is saved as {new_name}')
    
    break
    