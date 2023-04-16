from os import getenv

from aiogram import Router

from .error import router as error_router
from .start import router as start_router
from .admin import router as admin_router


router = Router()
router.include_router(start_router)
router.include_router(admin_router)

if getenv('ENABLE_ERRORS_LOGS') == 'True':
    router.include_router(error_router)
