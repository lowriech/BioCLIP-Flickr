`traintest/train`

Information about the train data in your train/test split go here. 

This folder will sync to GitHub, so use identifiers instead of raw data. For example, if your data is a table with 1,000 rows and you use an 80/20 train/test split, save the row IDs for 800 rows here and the other 200 in `traintest/test`. Alternatively, if your data is a nested folder structure with 100,000 images, save a file with 80,000 file paths here, and the other 20,000 to `traintest/test`. 

Save the identifiers in a file format appropriate to the language in your pipeline e.g. .rds for R or .pkl for Python.
