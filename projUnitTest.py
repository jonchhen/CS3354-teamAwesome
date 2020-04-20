#Unit Test written in python

import unittest


class TestBookMethods(unittest.TestCase):


# nextPage should set currentPage to an integer value passed by the user.
# In doing so, we consider the cases numbers in page range, zero or below, and
# past the maximum page count of the book
    def test_setPage(self):
        # test an ordinary page number
        self.ebook.setPage(5)
        self.assertEqual(book.getPageNum(),5)
        # test the first page number
        self.ebook.setPage(1)
        self.assertEqual(book.getPageNum(),1)
        #test the last page
        self.ebook.setPage(ebook.getLastPageNum())
        self.assertEqual(book.getPageNum(),ebook.getLastPageNum())
        # check cases beyond first or last page
        with self.assertRaises(IndexOutofBoundsException):
            ebook.setPage(0)
        with self.assertRaises(IndexOutofBoundsException):
            ebook.setPage(ebook.getLastPageNum()+1)


if __name__ == '__main__':
    unittest.main()
