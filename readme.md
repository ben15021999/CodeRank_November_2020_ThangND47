# CodeRank November 2020

## Author: ThangND47

### Problem 1: Stair Case
Bài này rất đơn giản, chỉ cần in kết quả như đề yêu cầu.

Lưu ý: Trong Python có hàm rjust trong String để điều chỉnh vị trí chuỗi ở trái, giữa hoặc phải (trong bài này thì sẽ là bên phải)

### Problem 2: Full Counting Sort
Chú ý đến cụm "The first half of the strings encountered in the inputs are to be replaced with the character '-' (dash)." tức là nửa phần input (chuỗi con) của bài sẽ được thay thế bằng dấu "-".

Ban đầu, ta dùng 1 dòng for để thay thế nửa input đầu của bài bằng dấu "-". Sau đó, ta sẽ mapping các chuỗi con theo key, trong test ví dụ, cặp "0 ab" sẽ có key là 0, value là ab. Ta dùng 1 số kỹ thuật mapping như Map (Hashmap) trong C++, Java hoặc Dictionary (Python). Lúc này ta sẽ có bộ key, value mới là số thứ tự với chuỗi mới được ghép từ các chuỗi con.

Cuối cùng, ta for các giá trị theo key đã được sắp xếp để in ra kết quả.

### Problem 3: Minimum Loss
Theo thuật giải chân phương, ta sẽ dùng 2 vòng for để lấy ra bộ i, j sao cho i < j & price[i] > price[j] rồi lấy minimun. Nhưng cách ấy với độ phức tạp O(n^2) không thật sự hiệu quả với n lớn (trong bài này là n <= 10^5).

Nếu để ý thì ta sẽ có nhận xét thế này, giữa 2 số a và b trong 1 mảng thì min(|a -b|) xảy ra khi a và b là 2 số kề nhau của mảng sau khi được sắp xếp. Lúc này ta sẽ có nhận xét 2, sau khi sắp xếp, thì nếu trường hợp i, j, k sao cho i < j < k và (price[i] < price[j] < price[k]) và ((year[i] < year[j] < year[k]) luôn xảy ra thì dữ liệu đầu vào là dữ liệu tuyến tính theo xu hướng tăng theo năm, lúc này ta sẽ không nhận được minimun loss. 

Từ đó ta kết luận rằng muốn có minimun loss thì phải tồn tại các cặp i, j sao cho (j - i = 1) và (price[i] < price[j]) và (year[i] > year[j]), ta lấy min của các price[j] - price[i] sẽ ra kết quả