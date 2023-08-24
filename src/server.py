
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import os

app = FastAPI()

@app.post("/upload")
async def upload_image(project_name: str, image: UploadFile = File(...)):
    # 画像のアップロード処理を実装する
    save_path = os.path.join(project_name, image.filename)
    with open(save_path, "wb") as f:
        f.write(image.file.read())
    
    # PILを使用して画像をPNG形式で保存する
    img = Image.open(save_path)
    png_save_path = os.path.splitext(save_path)[0] + ".png"
    img.save(png_save_path, "PNG")
    
    return {"filename": image.filename, "save_path": png_save_path}
