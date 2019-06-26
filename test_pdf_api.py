import boto3
import json
import os
import uuid
import datetime
import logging
import unittest
import api_lambda_sqs

class Test_pdf_api(unittest.TestCase):
       
        
        def test_build_job_data_pdfId(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            self.assertIsNotNone(job['pdfId'])

        def test_build_job_data_folder(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            self.assertIsNotNone(job['folder'])   

        def test_build_job_data_folder_format(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            currentDate = datetime.datetime.now()
            folder = "PDF/" + "/" + str(currentDate.year) + "/" + str(currentDate.month).zfill(2) + "/" + str(currentDate.day).zfill(2)
            self.assertEqual(folder, job['folder'])
        
        def test_build_job_data_absolute_path(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            self.assertIsNotNone(job['absolute_path'])

        def test_build_job_data_absolute_path_format(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            currentDate = datetime.datetime.now()
            folder = "PDF/" + "/" + str(currentDate.year) + "/" + str(currentDate.month).zfill(2) + "/" + str(currentDate.day).zfill(2)
            urlS3 = 'https://s3.amazonaws.com/FileBuilderTestArmenia/'
            absolute_path = urlS3 + "/" + folder + '/' + job['pdfId'] + '.pdf'
            self.assertEqual(absolute_path, job['absolute_path'])  

        def test_build_job_data_pdfId_exist(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            self.assertTrue('pdfId'in job)  

        def test_build_job_data_pdfId_exist(self):
            job= api_lambda_sqs.build_job_data(self.get_options())
            self.assertTrue('pdfId'in job) 

        def get_options(self):
            options = {
            "data":{"usuario":"<strong>Cliente Importante</strong>","adjunto":"8275","carta-jefe":"<div>Esto es un pdf.</div>"},
            "url":"http://madalgo.au.dk/~jakobt/wkhtmltoxdoc/wkhtmltoimage_0.10.0_rc2-doc.html",
            "options":{"encoding":"UTF-8"},
            "metadata":{"emailJobId":"5c1b2fcf0044737efcb29fbc"}
        }

            return options

if __name__ == '__main__':
    unittest.main()