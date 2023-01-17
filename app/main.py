import os
import uuid

import pandas as pd
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from app.tools import make_cache, description_setup, data_eng

temp = make_cache("temp")

API = FastAPI(
    title="DataEngFastAPI",
    description=description_setup(),
    version="0.0.1",
    docs_url="/",
)

API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@API.post("/process", tags=["CSV Processing"])
async def process(data: UploadFile = File(...)):
    filepath = os.path.join(temp, f"{uuid.uuid4()}.csv")
    data_eng(pd.read_csv(data.file)).to_csv(filepath, index=False)
    return FileResponse(
        filepath,
        media_type=data.content_type,
        filename=data.filename,
    )
