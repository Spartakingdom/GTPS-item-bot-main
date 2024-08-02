# utils/updater.py

import os
import aiohttp
import hashlib
from config import ITEMS_URL

async def download_file(url, dest):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(dest, 'wb') as f:
                    f.write(await response.read())
                return True
            return False

def file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

async def check_for_updates(file_path, url):
    temp_file = file_path + '.tmp'
    await download_file(url, temp_file)

    if not os.path.exists(file_path) or file_hash(file_path) != file_hash(temp_file):
        os.replace(temp_file, file_path)
        return True
    else:
        os.remove(temp_file)
        return False
