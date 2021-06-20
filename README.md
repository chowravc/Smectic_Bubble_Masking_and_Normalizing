# Smectic_Bubble_Masking_and_Normalizing

Masking and normalizing images of Smectic Bubbles with islands on them.

There is a mask included by default. More can be created using utils.py.

## Utilities:

1. Process images
    
    Input the images inside directory `/input/<your-directory-name>/`.
    
    ```
    python main.py --process --fDir /input/example/ --ext tif --fC 1.5 --fS 2.0
    ```
    
    Processed frames will be outputted to `/output/<your-directory-name>/`.
