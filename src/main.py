from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.core.database import Base, engine
from src.models.product import Product
from src.models.customer import Customer
from src.models.order import Order
from src.api.v1.products import router as product_router
from src.api.v1.customers import router as customer_router
from src.api.v1.orders import router as order_router
from src.core.exceptions import http_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)

    yield

    # Shutdown
    pass


app = FastAPI(
    title="Inventory Management API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    product_router,
    prefix="/api/v1"
)

app.include_router(
    customer_router,
    prefix="/api/v1"
)

app.include_router(
    order_router,
    prefix="/api/v1"
)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler,
)

@app.get("/")
async def root():
    return {
        "message": "Inventory Management API"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }