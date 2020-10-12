import tabula
 
file = "http://lab.fs.uni-lj.si/lasin/wp/IMIT_files/neural/doc/seminar8.pdf"
 
tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)

# output just the first table in the PDF to a CSV
tabula.convert_into(file, "iris_first_table.csv")
 
# output all the tables in the PDF to a CSV
tabula.convert_into(file, "iris_all.csv", all = True)

tabula.convert_into_by_batch("/path/to/files", output_format = "csv", pages = "all")
