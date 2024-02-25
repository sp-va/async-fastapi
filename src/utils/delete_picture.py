import os

# Для той же цели, что функция save_picture
async def delete_picture(file_path: str):
    os.remove(file_path)