
# %% [markdown]
#Lesson-01-02-03-Kien-thuc-Python-co-ban-P03

 # Phần 03 - Kiến thức Python cơ bản dành cho học viên IMIC!¶

#Liên hệ Phòng Tuyển Sinh đào tạo nhân sự: (024)3 7557 666 - (028)2253 2345 - 091 6878 224

#Hòm thư: phongdaotao@imic.edu.vn

#Website: https://www.imic.edu.vn/

 # Phần 03 - Kiến thức Python Collections (Arrays)¶

#Có 4 kiểu dữ liệu collection trong ngôn ngữ lập trình Python:

#List là một tập hợp được sắp xếp và có thể thay đổi. Cho phép các phần tử trùng lặp.

#Tuple là một bộ sưu tập có thứ tự và không thể thay đổi. Cho phép các phần tử trùng lặp.

#Set là một tập hợp không có thứ tự và không được lập chỉ mục. Không có phần tử trùng lặp.

#Dictionary là một tập hợp được sắp xếp theo thứ tự và có thể thay đổi. Không có phần tử trùng lặp.

#Ghi chú: Kể từ phiên bản Python 3.7, các từ điển đã được sắp xếp theo thứ tự. 

#Trong Python 3.6 trở về trước, từ điển không có thứ tự.

 # Kiến thức về Python Lists¶

#Lists được sử dụng để lưu trữ nhiều phần tử trong một biến duy nhất.

#Lists là một trong 4 kiểu dữ liệu tích hợp sẵn (built-in data types) trong Python được 

#sử dụng để lưu trữ các bộ sưu tập dữ liệu, 3 kiểu còn lại là Tuple, Set và Dictionary.

#Lists được tạo bằng [].

# %% 
# Tạo một danh sách:
danh_sach = ["apple", "banana", "cherry"]
# %% [markdown]
#['apple', 'banana', 'cherry']

#Các mục trong danh sách được sắp xếp theo thứ tự, có thể thay đổi và cho phép các giá trị trùng lặp.

#Các mục trong danh sách được lập chỉ mục, mục đầu tiên có chỉ mục [0], mục thứ hai có chỉ mục [1], v.v.

#Danh sách được sắp xếp theo thứ tự, điều đó có nghĩa là các mục có thứ tự xác định và thứ tự đó sẽ không thay đổi.

#Nếu bạn thêm các mục mới vào danh sách, các mục mới sẽ được đặt ở cuối danh sách.

#Danh sách có thể thay đổi, nghĩa là chúng ta có thể thay đổi, thêm và xóa các mục trong danh sách sau khi nó đã được tạo.

#Vì danh sách được lập chỉ mục nên danh sách có thể có các mục có cùng giá trị.

# %% 
# Danh sách cho phép các giá trị trùng lặp
danh_sach = ["apple", "banana", "cherry", "apple", "cherry"]
# %% [markdown]
#['apple', 'banana', 'cherry', 'apple', 'cherry']

#Để xác định danh sách có bao nhiêu mục, hãy sử dụng hàm len().

# %% 
# In số lượng các mục trong danh sách
# %% [markdown]
#5

#Các mục trong danh sách có thể thuộc bất kỳ kiểu dữ liệu nào.

# %% 
# Các kiểu dữ liệu string, int và boolean
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
# %% [markdown]
#print(list2)

#print(list3)

#['apple', 'banana', 'cherry']

#[1, 5, 7, 9, 3]

#[True, False, False]

#Một danh sách có thể chứa các kiểu dữ liệu khác nhau:

# %% 
list1 = ["abc", 34, True, 40, "male"]
# %% [markdown]
#['abc', 34, True, 40, 'male']

#Sử dụng hàm type() để xác định kiểu dữ liệu.

# %% 
danh_sach = ["apple", "banana", "cherry"]
# %% [markdown]
#<class 'list'>

#Cũng có thể sử dụng hàm tạo list() khi tạo một danh sách mới.

# %% 
danh_sach = list(("apple", "banana", "cherry"))
# %% [markdown]
#['apple', 'banana', 'cherry']

 # Cách truy cập phần tử trong Lists¶

# %% 
# Lấy ra phần tử thứ 2 trong danh sách
danh_sach = ["apple", "banana", "cherry"]
# %% [markdown]
#banana

#-1 đề cập đến mục cuối cùng, -2 đề cập đến mục cuối cùng thứ hai,v.v.

# %% 
# %% [markdown]
#cherry

# %% 
# Lấy ra các phần tử trong phạm vi từ 2-4
danh_sach = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(danh_sach[2:5])
# Lưu ý: Tìm kiếm sẽ bắt đầu ở chỉ mục 2 (bao gồm) và kết thúc ở chỉ mục 5 (không bao gồm).
print(danh_sach[:4])
print(danh_sach[4:])
# %% [markdown]
#['cherry', 'orange', 'kiwi']

#['apple', 'banana', 'cherry', 'orange']

#['kiwi', 'melon', 'mango']

#['orange', 'kiwi', 'melon']

#Để xác định xem một mục cụ thể có xuất hiện trong danh sách hay không, hãy sử dụng từ khóa in:

# %% 
if "apple" in danh_sach:
# %% [markdown]
#Có apple trong danh sách!

 # Cách thay đổi giá trị trong Lists¶

# %% 
danh_sach[0] = "Táo"
# %% [markdown]
#['Táo', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# %% 
danh_sach[1:3] = ["chuối", "cam"]
# %% [markdown]
#['Táo', 'chuối', 'cam', 'orange', 'kiwi', 'melon', 'mango']

# %% 
# Nếu bạn chèn nhiều mục hơn số lượng bạn thay thế, các mục mới sẽ được chèn 
# vào nơi bạn đã chỉ định và các mục còn lại sẽ di chuyển tương ứng
danh_sach[1:2] = ["chuối", "vải", "nhãn"]
# %% [markdown]
#['Táo', 'chuối', 'vải', 'nhãn', 'cam', 'orange', 'kiwi', 'melon', 'mango']

# %% 
# Thay đổi giá trị thứ 2 và thứ 3 bằng cách thay thế nó bằng một giá trị
danh_sach = ["apple", "banana", "cherry"]
danh_sach[1:3] = ["táo"]
# %% [markdown]
#['apple', 'táo']

# %% 
# Sử dụng hàm insert() chèn một mục tại chỉ mục được chỉ định
danh_sach = ["apple", "banana", "cherry"]
danh_sach.insert(2, "quýt")
# %% [markdown]
#['apple', 'banana', 'quýt', 'cherry']

 # Cách thêm phần tử vào Lists¶

# %% 
# sử dụng append() để gắn thêm phần tử vào cuối danh sách
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.append("cam")
# %% [markdown]
#['táo', 'chuối', 'anh đào', 'cam']

# %% 
# sử dụng insert() để thêm phần tử vào vị trí bất kỳ
danh_sach.insert(1, "quýt")
# %% [markdown]
#['táo', 'quýt', 'chuối', 'anh đào', 'cam']

# %% 
# Để nối các phần tử từ một danh sách khác vào danh sách hiện tại, 
# hãy sử dụng phương thức expand()
danh_sach1 = ["táo", "chuối", "anh đào"]
danh_sach2 = ["xoài", "dứa", "đu đủ"]
danh_sach1.extend(danh_sach2)
# %% [markdown]
#['táo', 'chuối', 'anh đào', 'xoài', 'dứa', 'đu đủ']

# %% 
# Thêm các phần tử của một tuple vào danh sách
danh_sach1 = ["táo", "chuối", "anh đào"]
danh_sach2 = ("Quả kiwi", "cam")
danh_sach1.extend(danh_sach2)
# %% [markdown]
#['táo', 'chuối', 'anh đào', 'Quả kiwi', 'cam']

 # Cách xóa phần tử trong Lists¶

# %% 
# sử dụng remove() để xóa phần tử khỏi danh sách
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.remove("chuối")
# %% [markdown]
#['táo', 'anh đào']

# %% 
# sử dụng pop() để xóa phần tử theo chỉ mục
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.pop(1)
# %% [markdown]
#['táo', 'anh đào']

# %% 
# Nếu bạn không chỉ định chỉ mục, phương thức pop() sẽ xóa mục cuối cùng
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.pop()
#

# %% [markdown]
#['táo', 'chuối']

# %% 
#

#

# Từ khóa del cũng xóa chỉ mục được chỉ định:
danh_sach = ["táo", "chuối", "anh đào"]
del danh_sach[0]
#

# %% [markdown]
#['chuối', 'anh đào']

# %% 
#

#

# Từ khóa del cũng có thể sử dụng để xóa hoàn toàn danh sách
danh_sach = ["táo", "chuối", "anh đào"]
#

# %% [markdown]
# %% 
#

#

# sử dụng clear() để xóa trống danh sách
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.clear()
#

# %% [markdown]
#[]

 # Sử dụng vòng lặp để duyệt phần tử trong Lists¶

# %% 
#

#

# In tất cả các phần tử trong danh sách, từng cái một
danh_sach = ["táo", "chuối", "anh đào"]
for i in danh_sach:
#

# %% [markdown]
#táo

#chuối

#anh đào

# %% 
#

#

danh_sach = ["táo", "chuối", "anh đào"]
#

# %% [markdown]
#  if "o" in it:

#    ds_moi.append(it)

#print(ds_moi)

#['táo', 'anh đào']

# %% 
#

#

# newlist = [expression for item in iterable if condition == True]
danh_sach = ["táo", "chuối", "anh đào"]
ds_moi = [a for a in danh_sach if a != "táo"]
#

# %% [markdown]
#['chuối', 'anh đào']

# %% 
#

#

# Nếu chỉ đơn giản là duyệt và hiển thị các phần tử trong lists
ds_moi = [a for a in danh_sach]
#

# %% [markdown]
#['táo', 'chuối', 'anh đào']

 # Sắp xếp phần tử trong lists¶

# %% 
#

#

danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.sort() # A-Z
#

# %% [markdown]
#['anh đào', 'chuối', 'táo']

# %% 
#

#

# Để sắp xếp giảm dần, hãy sử dụng đối số từ khóa reverse = True
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.sort(reverse=True) # Z-A
#

# %% [markdown]
#['táo', 'chuối', 'anh đào']

# %% 
#

#

# Sử dụng reverse() để đảo ngược danh sách
danh_sach = ["táo", "chuối", "anh đào"]
danh_sach.reverse()
#

# %% [markdown]
#['anh đào', 'chuối', 'táo']

 # Kiến thức về Python Tuples¶

#Tuples được sử dụng để lưu trữ nhiều phần tử trong một biến duy nhất.

#Tuple là một bộ sưu tập được sắp xếp theo thứ tự và không thể thay đổi.

#Tuples được viết bằng dấu ().

# %% 
#

#

# Định nghĩa 1 tuples
tpl = ("táo", "chuối", "anh đào")
#

# %% [markdown]
#('táo', 'chuối', 'anh đào')

#Các phần tử trong Tuple được sắp xếp theo thứ tự, không thể thay đổi và cho phép các giá trị trùng lặp.

#Tuple các phần tử được lập chỉ mục, phần tử đầu tiên có chỉ mục [0], mục thứ hai có chỉ mục [1], v.v.

#Tuple là không thể thay đổi, có nghĩa là chúng ta không thể thay đổi, thêm hoặc xóa các mục sau khi bộ tuple đã được tạo.

#Vì các bộ giá trị được lập chỉ mục nên chúng có thể có các mục có cùng giá trị.

# %% 
#

#

tpl = ("táo", "chuối", "anh đào", "táo", "anh đào")
#

# %% [markdown]
#('táo', 'chuối', 'anh đào', 'táo', 'anh đào')

# %% 
#

#

tpl01 = ("táo",)
#

# %% [markdown]
#tpl02 = ("táo")

#print(type(tpl02))

#<class 'tuple'>

#<class 'str'>

# %% 
#

#

# Sử dụng hàm tuple() để khởi tạo 1 tuples
tpl = tuple(("táo", "chuối", "anh đào"))
#

# %% [markdown]
#('táo', 'chuối', 'anh đào')

 # Cách truy cập phần tử trong Tuples¶

#Tương tự như trong Lists.

#tpl[1]: Lấy ra giá trị ở chỉ mục 1.

#-1 đề cập đến mục cuối cùng, -2 đề cập đến mục cuối cùng thứ hai, v.v.

#tpl[2:5]: Lấy ra bắt đầu ở chỉ mục 2 (bao gồm) và kết thúc ở chỉ mục 5 (không bao gồm).

#tpl[:4]: Lấy ra từ 0-3.

#tpl[2:]: Lấy ra từ 2 đến cuối cùng.

#tpl[-4,-1]: trả về các mục từ chỉ mục -4 (bao gồm) đến chỉ mục -1 (loại trừ).

#if "apple" in tpl: Kiểm tra nếu có tồn tại.

 # Cách cập nhật phần tử trong Tuples¶

#Tuple không thể thay đổi, có nghĩa là bạn không thể thay đổi, thêm hoặc xóa các mục sau khi tuple được tạo.

#Nhưng có một cách giải quyết. Bạn có thể chuyển đổi tuple thành một lists, thay đổi lists và chuyển đổi lại lists thành tuple.

#Chuyển đổi tuple thành một danh sách để có thể thay đổi nó.

# %% 
#

#

x = ("táo", "chuối", "anh đào")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#

# %% [markdown]
#('táo', 'kiwi', 'anh đào')

# %% 
#

#

# Cách 1: Convert into a list -> thêm phần tử vào tuple
tpl = ("táo", "chuối", "anh đào")
y = list(tpl)
y.append("cam")
tpl = tuple(y)
#

# %% [markdown]
#('táo', 'chuối', 'anh đào', 'cam')

# %% 
#

#

# Cách 2: Add tuple to a tuple -> thêm phần tử vào tuple
tpl = ("táo", "chuối", "anh đào")
y = ("cam",)
tpl += y
#

# %% [markdown]
#('táo', 'chuối', 'anh đào', 'cam')

#Tuples là không thể thay đổi, vì vậy bạn không thể xóa các mục khỏi nó, nhưng bạn có thể sử dụng cách giải quyết tương tự như chúng tôi đã sử dụng để thay đổi và thêm các mục.

# %% 
#

#

tpl = ("táo", "chuối", "anh đào")
y = list(tpl)
y.remove("táo")
tpl = tuple(y)
#

# %% [markdown]
#('chuối', 'anh đào')

 # Cách "Unpack" trong tuples¶

# %% 
#

#

# Ví dụ 01 - Packing a tuple:
danh_sach = ("táo", "chuối", "cam")
#

# %% [markdown]
#('táo', 'chuối', 'cam')

# %% 
#

#

# Ví dụ 02 - Unpacking a tuple:
danh_sach = ("táo", "chuối", "cam")
(green, yellow, red) = danh_sach
print(green)
print(yellow)
#

# %% [markdown]
#táo

#chuối

#cam

#Lưu ý: Số lượng biến phải khớp với số lượng giá trị trong bộ tuple, 

#nếu không, bạn phải sử dụng dấu hoa thị để thu thập các giá trị còn lại dưới dạng danh sách.

#Nếu số biến ít hơn số giá trị, bạn có thể thêm dấu * vào tên biến và các giá trị sẽ được gán cho biến dưới dạng danh sách.

# %% 
#

#

danh_sach = ("táo", "chuối", "cam", "anh đào", "bưởi", "chanh")
#

# %% [markdown]
#print(yellow)

#print(red)

#táo

#chuối

#['cam', 'anh đào', 'bưởi', 'chanh']

#Nếu dấu hoa thị được thêm vào tên biến khác với tên biến cuối cùng, 

#Python sẽ gán giá trị cho biến cho đến khi số giá trị còn lại khớp với số biến còn lại.

# %% 
#

#

danh_sach = ("táo", "chuối", "cam", "anh đào", "bưởi", "chanh")
(green, *tropic, red) = danh_sach
print(green)
print(tropic)
#

# %% [markdown]
#táo

#['chuối', 'cam', 'anh đào', 'bưởi']

#chanh

 # Cách duyệt tuples¶

# %% 
#

#

# Sử dụng vòng lặp for để duyệt tuples
danh_sach = ("táo", "chuối", "cam")
for i in danh_sach:
#

# %% [markdown]
#táo

#chuối

#cam

 # Cách nối dữ liệu giữa các tuples¶

# %% 
#

#

tuple1 = ("a", "b" , "c")
#

# %% [markdown]
#print(tuple3)

#('a', 'b', 'c', 1, 2, 3)

 # Kiến thức về Python Sets¶

#myset = {"apple", "banana", "cherry"}

#Sets được sử dụng để lưu trữ nhiều phần tử trong một biến duy nhất.

#Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trữ các tập hợp dữ liệu.

#Set là một tập hợp không có thứ tự và không được lập chỉ mục.

#Set được viết bằng dấu {}.

#Lưu ý: Các set không có thứ tự, vì vậy bạn không thể chắc chắn các phần tử sẽ xuất hiện theo thứ tự nào.

#Các phần tử tập hợp là không có thứ tự, không thể thay đổi và không cho phép các giá trị trùng lặp.

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
#

# %% [markdown]
#{'chuối', 'anh đào', 'táo'}

#Không có thứ tự có nghĩa là các phần tử trong một tập hợp không có thứ tự xác định.

#Các phần tử tập hợp có thể xuất hiện theo một thứ tự khác nhau mỗi khi bạn sử dụng chúng và 

#không thể được tham chiếu bằng chỉ mục hoặc khóa.

#Sau khi một set được tạo, bạn không thể thay đổi các phần tử của nó, nhưng bạn có thể thêm các phần tử mới.

#Các giá trị trùng lặp sẽ bị bỏ qua.

 # Cách truy cập phần tử¶

#Không thể truy cập các phần tử trong một tập hợp bằng cách tham chiếu đến chỉ mục hoặc khóa.

#Nhưng có thể lặp qua các phần tử bằng vòng lặp for hoặc kiểm tra sự tồn tại 1 phần tử trong set bằng cách sử dụng từ khóa in.

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
for i in myset:
#

# %% [markdown]
#chuối

#anh đào

#táo

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
if "chuối" in myset:
#

# %% [markdown]
#Có phần tử này trong set!

 # Cách thêm mới phần tử¶

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
myset.add("cam")
#

# %% [markdown]
#{'chuối', 'cam', 'anh đào', 'táo'}

#Để thêm các phần tử từ một tập hợp khác vào tập hợp hiện tại, hãy sử dụng phương thức update().

#Đối tượng trong phương thức update() không nhất thiết phải là một set, nó có thể là bất kỳ đối tượng nào 

#có thể lặp lại (tuples, lists, dictionaries,v.v.).

# %% 
#

#

myset1 = {"táo", "chuối", "anh đào"}
myset2 = {"dứa", "xoài", "đu đủ"}
myset1.update(myset2)
#

# %% [markdown]
#{'đu đủ', 'chuối', 'xoài', 'dứa', 'anh đào', 'táo'}

 # Cách xóa phần tử¶

# %% 
#

#

# Cách 1: Xóa bằng remove()
myset = {"táo", "chuối", "anh đào"}
myset.remove("chuối2")
#

# %% [markdown]
#---------------------------------------------------------------------------

#KeyError                                  Traceback (most recent call last)

#<ipython-input-10-4301f1ce1e23> in <module>

#      1 # Cách 1: Xóa bằng remove()

#      2 myset = {"táo", "chuối", "anh đào"}

#----> 3 myset.remove("chuối2")

#      4 print(myset)

#KeyError: 'chuối2'

# %% 
#

#

# Cách 2: Xóa bằng discard()
myset = {"táo", "chuối", "anh đào"}
myset.discard("chuối2")
#

# %% [markdown]
#{'chuối', 'anh đào', 'táo'}

#Cũng có thể sử dụng phương thức pop() để xóa một phần tử, nhưng phương thức này sẽ xóa phần tử cuối cùng. 

#Hãy nhớ rằng các set không có thứ tự, vì vậy bạn sẽ không biết mục nào sẽ bị loại bỏ.

#Giá trị trả về của phương thức pop() là phần tử bị loại bỏ đó.

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
ptu = myset.pop()
#

# %% [markdown]
#chuối

 # Cách duyệt qua từng phần tử¶

# %% 
#

#

myset = {"táo", "chuối", "anh đào"}
for i in myset:
#

# %% [markdown]
#chuối

#anh đào

#táo

 # Kiến thức về Python Dictionaries¶

#mydict = {

#  "brand": "Ford",

#  "model": "Everest",

#  "year": 2021

#}

#Dictionaries được sử dụng để lưu trữ các giá trị dữ liệu trong các cặp key: value.

#Dictionaries là một tập hợp được sắp xếp theo thứ tự, có thể thay đổi và không cho phép trùng lặp.

#Kể từ phiên bản Python 3.7, các từ điển được sắp xếp theo thứ tự. Trong Python 3.6 trở về trước, từ điển không có thứ tự.

#Dictionaries được viết bằng dấu {key:value}.

# %% 
#

#

mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021
}
#

# %% [markdown]
#{'brand': 'Ford', 'model': 'Everest', 'year': 2021}

#Các mục từ điển được sắp xếp theo thứ tự, có thể thay đổi và không cho phép trùng lặp.

#Các mục từ điển được trình bày theo key:value và có thể được tham chiếu bằng cách sử dụng tên khóa.

# %% 
#

#

#

# %% [markdown]
#Everest

#Khi chúng ta nói rằng từ điển được sắp xếp theo thứ tự, có nghĩa là các mục có thứ tự xác định và thứ tự đó sẽ không thay đổi.

#Từ điển có thể thay đổi, nghĩa là chúng ta có thể thay đổi, thêm hoặc bớt các mục sau khi từ điển đã được tạo.

#Từ điển không thể có hai phần tử với cùng một khóa.

#Các giá trị trong các phần tử từ điển có thể thuộc bất kỳ kiểu dữ liệu nào.

# %% 
#

#

mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021,
olors": ["red", "white", "blue"]
}
#

# %% [markdown]
#{'brand': 'Ford', 'model': 'Everest', 'year': 2021, 'colors': ['red', 'white', 'blue']}

 # Ví dụ 01¶

# %% 
#

#

# truy cập phần tử của từ điển
mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021,
olors": ["red", "white", "blue"]
}
# Sử dụng hàm get để lấy giá trị trong dictionary qua Key
x = mydict.get("model")
#

# %% [markdown]
#Everest

 # Ví dụ 02¶

# %% 
#

#

# Thay đổi giá trị
mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021,
olors": ["red", "white", "blue"]
#

# %% [markdown]
#mydict["year"] = 2021

#mydict["model"] = "Ford"

#mydict["brand"] = "Explorer"

#print(mydict)

#{'brand': 'Explorer', 'model': 'Ford', 'year': 2021, 'colors': ['red', 'white', 'blue']}

 # Ví dụ 03¶

# %% 
#

#

# sử dụng vòng lặp để duyệt Dictionary
# In tất cả các tên khóa trong từ điển, từng cái một:
mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021,
olors": ["red", "white", "blue"]
#

# %% [markdown]
#mydict["year"] = 2021

#mydict["model"] = "Ford"

#mydict["brand"] = "Explorer"

 Sử dụng vòng lặp for để duyệt các phần tử bên trong dictionary
#for i in mydict:

#    print(f"Giá trị = {i}")

#Giá trị = brand

#Giá trị = model

#Giá trị = year

#Giá trị = colors

 # Ví dụ 04¶

# %% 
#

#

mydict = {
rand": "Ford",
odel": "Everest",
ear": 2021  
#

# %% [markdown]
#for x in mydict:

#    print(mydict[x])

#    # print(mydict.get(x))

 Cách 02: Duyệt và lấy ra các giá trị từng phần tử
 print(mydict.values())
 Cách 03: Duyệt và lấy ra từng phần tử
#for x, y in mydict.items():

#    print(f"Key: {x} - Value: {y}")

#Ford

#Everest

#2021

#Key: brand - Value: Ford

#Key: model - Value: Everest

#Key: year - Value: 2021

 # Ví dụ 05¶

# %% 
#

#

hai báo khởi tạo từ điển
mydict = {
"brand": "Ford",
"model": "BMW",
"year": 2020
#

# %% [markdown]
#if "model" in mydict:

#    print("Có khóa model trong từ điển!")

#Có khóa model trong từ điển!

 # Ví dụ 06¶

# %% 
#

#

# khai báo và khởi tạo từ điển
mydict = {
"brand": "Ford",
"model": "BMW",
"year": 1964
}
# Kiểm tra số phần tử trong dictionary
#

# %% [markdown]
#-> Số phần tử là: 3

 # Ví dụ 07¶

# %% 
#

#

# khai báo và khởi tạo từ điển
mydict = {
"brand": "Ford",
"model": "BMW",
"year": 1964
#

# %% [markdown]
#mydict["color"] = "red :D"

 Hiển thị dữ liệu trong từ điển
#print(mydict.get("color"))

#print(mydict['color'])

#red :D

#red :D

 # Ví dụ 08¶

# %% 
#

#

# khai báo và khởi tạo từ điển
mydict = {
"brand": "Ford",
"model": "BMW",
"year": 1964
#

# %% [markdown]
#mydict.pop("model")

#print(mydict)

 Hàm popitem() sẽ xóa phần tử được thêm vào ở cuối.
#mydict.popitem()

#print(mydict)

 Từ khóa del sẽ thực hiện xóa đi phần tử theo Key.
 del mydict["model"]
 print(mydict)
 Hàm clear() sử dụng để xóa trống các phần tử trong dictionary.
#mydict.clear()

#print(mydict)

 {}
 Từ khóa del có thể sử dụng để xóa hoàn toàn từ điển.
#del mydict

#{'brand': 'Ford', 'year': 1964}

#{'brand': 'Ford'}

#{}

 # Ví dụ 09¶

# %% 
#

#

# khai báo và khởi tạo từ điển
dict1 = {
"brand": "Ford",
"model": "BMW",
"year": 1964
#

# %% [markdown]
 Sử dụng hàm copy() để sao chép dữ liệu giữa 2 dictionary
#dict2 = dict1.copy()

#dict2["model"] = "Honda"

#print(dict1)

#print(dict2)

#{'brand': 'Ford', 'model': 'BMW', 'year': 1964}

#{'brand': 'Ford', 'model': 'Honda', 'year': 1964}

