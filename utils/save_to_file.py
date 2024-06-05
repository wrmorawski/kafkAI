import os
from fpdf import FPDF
from utils.logger import configure_logger
from utils.constants import OUTPUT_PATH, FONT_SIZE, FONT

logger = configure_logger(__name__)

def save_to_pdf(text, filename):
    try: 
        pdf = FPDF()
        pdf.set_margins(10, 10)
        pdf.add_page()
        pdf.set_font(FONT, size = FONT_SIZE)
        pdf.multi_cell(200, 10, txt = text, align = 'L', )
        pdf.output(os.path.join(OUTPUT_PATH, filename))
        logger.info('Saved to pdf')
    except Exception as e:
        logger.info('Saving to pdf failed: ')
        logger.error(e)
        logger.info('Trying to save to txt instead...')
        save_to_txt(text, filename)
        raise e


def save_to_txt(text, filename):
    try:
        if ".pdf" in filename:
            filename = filename.replace(".pdf", ".txt")
        with open(os.path.join(OUTPUT_PATH, filename), "w") as file:
            file.write(text)
        logger.info('Saved to txt')
    except Exception as e:
        logger.info('Saving to txt failed: ')
        logger.error(e)
        raise e
    
