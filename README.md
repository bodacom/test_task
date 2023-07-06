**Custom PDF Parse Script**
The project is my trial to resolve the problem of automatic parsing of a custom *.pdf file.
As it's a special case it could not be helpful in general cases except the stages of extracting 
text content from the *.pdf and appending of existing *.xlsx files.

For the moment the problem was resolved partially. Able to extract:
  - separate Abstract data frame from whole text data
  - Abstract Topic Title
  - Presentation
  - Name(s)+Affiliation(s)+Location mixed data

To be improved:
  - font size could be used to split Name(s)+Affiliation(s)+Location correctly. This requires other PDF Parsed as pdfminer
  - splitting requires multiple rules as Name(s)+Affiliation(s)+Location block isn't homogeneous enough
  - data structure update is required as far as single Abstract could have multiple Authors, Locations, and Affiliations
