import io

from fastapi import FastAPI, File, Depends
from fastapi.datastructures import UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError
from sqlalchemy.ext.asyncio import AsyncSession

from main_app.logic import scale_image, create_image, get_image
from setup import MEDIA_ROOT, engine, get_session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload(
        image: UploadFile = File(...),
        session: AsyncSession = Depends(get_session)):
    try:
        unique_id = await create_image(session=session, directory=MEDIA_ROOT)
        image = image.file
        image = Image.open(image)
        image.save(f"{MEDIA_ROOT}/{unique_id}.jpg")
        await engine.dispose()
        return {"pic_id": unique_id}
    except UnidentifiedImageError:
        await session.rollback()
        return {"error": "Invalid image format"}
    except Exception as e:
        print(e)
        await session.rollback()
        return {"error": str(e)}


@app.get("/get/")
async def get(
        pic_id: str, scale: float = 1.0,
        session: AsyncSession = Depends(get_session)):
    try:
        image = await get_image(session, pic_id)
        if image is None:
            return {"error": "No image found"}
        image = scale_image(image, scale)
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="JPEG")
        image_bytes.seek(0)
        return StreamingResponse(image_bytes, media_type="image/jpeg")
    except Exception as e:
        print(e)
        await session.rollback()
        return {"error": str(e)}
