import os
import shutil
import argparse
import unittest

from md2remark import main

class MainTest(unittest.TestCase):
  '''Test Class for Main module'''

  def setUp(self):
    '''Ensures the test project is destroyed.'''
    if os.path.exists('md2remark_build'):
      shutil.rmtree('md2remark_build')

  def test_compile_slides_file(self):
    '''Tests detection of file'''
    main.compile_slides('tests/fixtures/input_file.md')

    f = open('md2remark_build/input_file.html', 'r')
    contents = f.read()
    f.close()

    assert 'Hello World Input' in contents
    assert 'input_file' in contents

  def test_compile_slides_dir(self):  
    '''Tests detection of directory'''
    main.compile_slides('tests/fixtures/input_dir/')

    assert os.path.exists('md2remark_build/input1.html')
    assert os.path.exists('md2remark_build/input2.html')
    
  def test_parse_cl_args(self):
    '''Tests commandline interface'''
    args = main.parse_cl_args(['my_slides.md'])

    assert args.source == 'my_slides.md'