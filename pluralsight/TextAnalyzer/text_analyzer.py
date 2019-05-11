import  unittest
import os

def analyze_text(file_name):
    """Calculate number of lines and characters in a file
       Args:
            file_name: the name of analyze file

        Raises:
            IOError: If ``file_name`` doesn't exist or can't be read

        Returns:
            A Tuple where first element is the number of lines
            and the second is number of characters
    """
    lines = 0
    chars = 0
    with open(file_name, 'r') as file:
        for line in file:
            lines += 1
            chars += len(line)
    return (lines, chars)
        #return sum(1 for _ in file) # _  -> from 0 to n-1

class TextAnalysisTests(unittest.TestCase):
    """Test for the``analyze_text`` function """

    def setUp(self):
        """fixture that creates a file for the text method to use"""
        self.file_name = "text_analysis_test_fiel.txt"
        with open(self.file_name, 'w') as file:
            file.write("Lorem Ipsum jest tekstem stosowanym jako przykładowy \n"
                       "wypełniacz w przemyśle poligraficznym. Został po raz \n"
                       "pierwszy użyty w XV w. przez nieznanego drukarza do \n"
                       "wypełnienia tekstem próbnej książki. Pięć wieków później \n"
                       "zaczął być używany przemyśle elektronicznym, pozostając \n")

    def tearDown(self):
        """fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_function_run(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.file_name)

    def test_line_count(self):
        """check that the line count is correct"""
        self.assertEqual(analyze_text(self.file_name)[0], 5)

    def test_character_count(self):
        """check that the character count is correct"""
        self.assertEqual(analyze_text(self.file_name)[1], 276)

    def test_no_such_file(self):
        """check the proper exception is thron for a missing file"""
        with self.assertRaises(IOError):
            analyze_text('foo')

    def test_no_deletiob(self):
        """check that function doesn't delete the input file"""
        analyze_text(self.file_name)
        self.assertTrue(os.path.exists(self.file_name))

if __name__ == '__main__':
    unittest.main()