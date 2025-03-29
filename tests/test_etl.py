import unittest
from pyspark.sql import SparkSession
import os
import subprocess

class TestEtl(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder \
            .appName("ETL Test") \
            .master("spark://spark-master:7077") \
            .config("spark.jars", "/opt/bitnami/spark/jars/mysql-connector-j-8.0.33.jar") \
            .getOrCreate()
        self.dir_destino = "/notebooks/csv"
        self.nome_python = "movimento_flat_python.csv"
        self.nome_scala = "movimento_flat_scala.csv"
        self.caminho_final_python = os.path.join(self.dir_destino, self.nome_python)
        self.caminho_final_scala = os.path.join(self.dir_destino, self.nome_scala)
        os.makedirs(self.dir_destino, exist_ok=True)
        os.chmod(self.dir_destino, 0o777)

    def tearDown(self):
        self.spark.stop()

    # Testes pro ETL em Python
    def test_python_arquivo_gerado(self):
        self.run_python_etl()  
        self.assertTrue(os.path.exists(self.caminho_final_python))

    def test_python_tamanho_arquivo(self):
        self.run_python_etl()
        self.assertGreater(os.path.getsize(self.caminho_final_python), 0)

    # Testes pro ETL em Scala
    def test_scala_arquivo_gerado(self):
        self.run_scala_etl()  
        self.assertTrue(os.path.exists(self.caminho_final_scala))
        
    def test_scala_tamanho_arquivo(self):
        self.run_scala_etl()
        self.assertGreater(os.path.getsize(self.caminho_final_scala), 0)


if __name__ == '__main__':
    unittest.main()