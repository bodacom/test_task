import os
from tika import parser


# To find the frames
def frame_indexes(refs: list, dataset: str):
    '''
    Searches for the dataframe indexes based on the reference number
    Returns dictionary with reference number as a key and list of frame
    start and end indexes as a value
    '''
    indexes = dict()

    for ref, _ in enumerate(refs):
        if not ref == len(refs)-1:
            frame_start = dataset.find('P'+str(refs[ref])+'\n')
            frame_end = dataset.find('P'+str(refs[ref+1])+'\n')
        else:
            frame_start = dataset.find('P'+str(refs[ref])+'\n')
            frame_end = dataset.find('P'+str(refs[ref]+1)+'\n')
        indexes[refs[ref]] = [frame_start, frame_end]
    return indexes

# To find the title
def topic_title(data_frame: str) -> str:
    '''
    Searches for the topic title in the data frame
    '''
    data_frame = data_frame.split('\n')[1:]
    title = ''
    
    for el in data_frame:
        if el.isupper():
            title = title + el
        else:
            break
    return title


# opening pdf file
parsed_pdf = parser.from_file("file.pdf")

# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content']

ref_nums = [i for i in range(100, 110) if not i == 103]

frames = frame_indexes(ref_nums, data)

titles = []
for ref in ref_nums:
    titles.append(topic_title(data[frames[ref][0]:frames[ref][1]]))

for index, title in enumerate(titles):
    print(index, title)
    print()

# parser.from_file('/path/to/file.pdf', xmlContent=True)