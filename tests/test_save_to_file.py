from unittest.mock import patch 
import pytest
import os 

from utils.constants import OUTPUT_PATH
from utils.save_to_file import save_to_pdf, save_to_txt
from utils.maintenance import clear_test_outputs


def test_save_to_pdf_excpetion():
    with patch('utils.save_to_file.FPDF') as mock_pdf:
        mock_pdf.side_effect = Exception('mocked exception')
        with pytest.raises(Exception) as e:
            save_to_pdf('test_text', 'test_exception.pdf')

        assert os.path.exists(os.path.join(OUTPUT_PATH, 'test_exception.txt')) == True
        assert e.value.args[0] == 'mocked exception'
        clear_test_outputs()
