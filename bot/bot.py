# pip install pymupdf aiogram==2.25

import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import fitz  # PyMuPDF

# Telegram Bot Token
BOT_TOKEN = "7903328953:AAGBntt0YR97ELWOsvWC7DhNAfoR1FGI0zY"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# katalog 
TEMP_DIR = "temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)




async def convert_pdf_to_image(file_path):
    try:
        doc = fitz.open(file_path)
        first_page = doc[0]  # 1-beti
        pix = first_page.get_pixmap()  # Convert to image
        image_path = f"{file_path}.jpg"
        pix.save(image_path)  # Save image
        return image_path
    except Exception as e:
        logging.error(f"Error converting PDF: {e}")
        return None


@dp.channel_post_handler(content_types=types.ContentType.DOCUMENT)
async def handle_pdf_document(message: types.Message):
    document = message.document

    # pdf fayl ekanini tekshirish
    if not document.file_name.endswith(".pdf"):
        return

    logging.info(f"Received PDF: {document.file_name}")

    # pdf fileni yuklaymiz
    file_path = f"{TEMP_DIR}/{document.file_name}"
    file = await bot.get_file(document.file_id)
    await bot.download_file(file.file_path, file_path)

    # pdfni 1-betini rasmi
    try:
        image_path = await convert_pdf_to_image(file_path)

        # Send the image as a reply to the original PDF message
        with open(image_path, "rb") as image_file:
            await message.reply_photo(
                photo=image_file,
                caption=f"Preview of: {document.file_name}",
            )

        logging.info(f"Sent image for {document.file_name}")

        # Cleanup
        os.remove(file_path)
        os.remove(image_path)

    except Exception as e:
        logging.error(f"Error processing {document.file_name}: {e}")
        await message.reply("Failed to process the PDF.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
