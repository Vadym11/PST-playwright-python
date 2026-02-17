def get_all_categories(api_handler):
    return api_handler.get('/categories')

def get_all_brands(api_handler):
    return api_handler.get('/brands', {}, {})

def get_all_images(api_handler):
    return api_handler.get('/images', {}, {})