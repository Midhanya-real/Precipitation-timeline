from src.Services.FileCounterService import FileCounterService
from src.Services.InputService import InputService
from src.Services.OutputService import OutputService
from src.Services.SortDictService.SortByCondService import SortByCondService

io_service = InputService(r'D:\Projects\PyProjects\PD\Lab4\Files\data.csv')
fc_service = FileCounterService(r'D:\Projects\PyProjects\PD\Lab4\Files')

data = io_service.input()
cond_service = SortByCondService(data, 13)
data = cond_service.sort()

out_service = OutputService(data)
print(out_service.data[2])
out_service.output()

# io_service.output_for_num(data)
# io_service.output_for_string(data)

files_count = fc_service.count_files()
print(files_count)
