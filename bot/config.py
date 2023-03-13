import os

class Config:
    TELEGRAM_TOKEN=os.environ['6010254886:AAG7R7UcgHBAeQEtgBIe1qB5EL5JmjzPzcU']
    TELEGRAM_APP_HASH=os.environ['6553ea819bb17098b0e3c62530823328']
    TELEGRAM_APP_ID=int(os.environ['13750040'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
