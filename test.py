from tika import parser


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
        elif not refs[ref] == 102:
            frame_start = dataset.find('P'+str(refs[ref])+'\n')
            frame_end = dataset.find('P'+str(refs[ref]+1)+'\n')
        else:
            frame_start = dataset.find('P'+str(refs[ref])+'\n')
            frame_end = dataset.find('P'+str(104)+'\n')
        indexes[refs[ref]] = [frame_start, frame_end]
    return indexes


def topic_title(data_frame: str) -> tuple:
    '''
    Searches for the topic title in the data frame
    '''
    data_frame = data_frame.split('\n')[1:]
    title = ''
    
    for el in data_frame:
        if el.isupper():
            title = title + el
            elmnt = el
        else:
            break
    return title, elmnt


def presentation_abstract(data_frame: str) -> tuple:
    '''
    Searches for the abstract in the data frame
    Returns start position of the abstract based on the key word
    '''
    keywords = ['Introduction:',
                'Background:',
                'Introduction and Objectives:',
                'Background/Objective:',
                'Introduction/Objective:',
                ]
    position = 0
    found = False
    for keyword in keywords:
        if not data_frame.find(keyword) == -1:
            found, position = True, data_frame.find(keyword)
        if found:
            break
    
    return found, position


# opening pdf file
parsed_pdf = parser.from_file("file.pdf")

# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content']

ref_nums = [i for i in range(100, 116) if not i == 103]

frames = frame_indexes(ref_nums, data)

parsed_data = []
titles = []
abstracts = []
how_to_split = []

for i, ref in enumerate(ref_nums):
   
    parsed_data.append(['P'+str(ref),])
    data_frm = data[frames[ref][0]:frames[ref][1]]
    
    # To find title and last fragment
    title, element = topic_title(data_frm)
    parsed_data[i].append(title)
    carrier1 = data_frm.find(element) + len(element)
    
    # to find abstract
    found, carrier_abstract = presentation_abstract(data_frm)
    if found:
        parsed_data[i].append(data_frm[carrier1:carrier_abstract])
        parsed_data[i].append(data_frm[carrier_abstract:frames[ref][1]])
    else:
        parsed_data[i].append('Author not found')
        parsed_data[i].append('Abstract not found')
    
    for el in parsed_data[i]:
        print(el)

# parser.from_file('/path/to/file.pdf', xmlContent=True)