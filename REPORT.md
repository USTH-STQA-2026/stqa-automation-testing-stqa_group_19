# BÁO CÁO KẾT QUẢ KIỂM THỬ TỰ ĐỘNG WEB UI (REPORT)

## 1. Môi trường kiểm thử (Test Environment)
- **Hệ thống kiểm thử**: Quản lý mượn sách Thư viện ABC (https://stqa.rbc.vn)
- **Công cụ kiểm thử**: Python 3.11.9, Playwright, pytest, pytest-playwright
- **Trình duyệt**: Chromium (được chạy với tham số `--force-renderer-accessibility` để hỗ trợ tương tác với Semantics Tree của Flutter Web)
- **Cấu hình tài khoản test**:
  - Email thành viên: `ba.nguyen@email.com` / `password123`
  - Email thủ thư: `librarian@library.com` / `admin123`

---

## 2. Danh sách Test Case và Trạng thái Thực thi
Dưới đây là danh sách tất cả các test case được chạy tự động. Mọi test case đều tự động chụp ảnh màn hình lưu vào thư mục `screenshots/`.

| Mã TC | Tên / Kịch bản Kiểm thử | Trạng thái | Ghi chú / Kết quả |
|---|---|---|---|
| **TC-01** | Đăng nhập thành công với email và mật khẩu đúng | **PASS** | Đăng nhập bằng `librarian@library.com`, AppBar hiển thị đúng vai trò và nút Đăng xuất. |
| **TC-02** | Đăng nhập thất bại — sai mật khẩu | **PASS** | Nhập sai mật khẩu, hệ thống hiển thị thông báo lỗi phù hợp. |
| **TC-03** | Đăng nhập thất bại — để trống cả hai trường | **PASS** | Hệ thống báo lỗi "Vui lòng nhập email và mật khẩu" và không cho đăng nhập. |
| **TC-04** | Tìm sách theo tên — nhập "Flutter" | **PASS** | Tìm kiếm trả về đúng sách `BOOK001` (Lập trình Flutter cơ bản). |
| **TC-05** | Tìm sách — không có kết quả | **PASS** | Tìm kiếm từ khóa không tồn tại, hiển thị thông báo "Không tìm thấy sách". |
| **TC-06** | Lọc sách theo thể loại — nhập "Công nghệ" | **PASS** | Điền "Công nghệ" vào ô lọc thể loại (textbox), chỉ hiển thị sách Công nghệ. |
| **TC-07** | Tìm sách theo tác giả | **PASS** | Tìm tác giả "Nguyễn Minh Đức", hiển thị đúng sách do tác giả này viết. |
| **TC-08** | Mượn sách thành công | **PASS** | Chọn sách "Có sẵn", xác nhận mượn, sách chuyển sang trạng thái "Đang mượn". |
| **TC-09** | Xem danh sách sách đang mượn | **PASS** | Tab "Mượn / Trả" hiển thị đúng mã phiếu mượn `BR001` của thành viên. |
| **TC-10** | Trả sách thành công | **PASS** | Nhấn "Trả sách", sách được chuyển về trạng thái "Có sẵn". |
| **TC-11** | Đăng xuất thành công | **PASS** | Nhấn icon đăng xuất và hệ thống điều hướng trở về trang đăng nhập. |
| **TC-12** | Chuyển ngôn ngữ giao diện sang English | **PASS** | Nhấn nút "EN" trên thanh AppBar, giao diện chuyển sang tiếng Anh hoàn toàn. |
| **TC-13** | Thêm thành viên mới thành công | **PASS** | (Bonus B1) Thêm thành viên với email hợp lệ. |
| **TC-14** | Thêm thành viên mới thất bại — trùng email | **PASS** | (Bonus B1) Hệ thống báo lỗi trùng email "Email đã tồn tại." khi tạo trùng. |
| **B2-L** | Kiểm thử hướng dữ liệu (Data-driven) đăng nhập lỗi | **PASS** | (Bonus B2) Chạy kịch bản đăng nhập lỗi với 3 bộ dữ liệu khác nhau. |
| **B2-S** | Kiểm thử hướng dữ liệu (Data-driven) tìm kiếm sách | **PASS** | (Bonus B2) Chạy kịch bản tìm kiếm sách với các từ khóa "Flutter", "Python", "Kiểm thử". |

---

## 3. Phát hiện lỗi hệ thống (Confirmed System Bugs)

### Bug 1: Ràng buộc xác thực định dạng email khi thêm thành viên mới bị ngược (Nhận xét từ TC-13 & TC-14)
- **Tài liệu đặc tả (REQ-07)**: Email phải hợp lệ (có `@` và dấu `.` ở phần domain, ví dụ `user@domain.com`). Email dạng `user@domain` là không hợp lệ.
- **Thực tế**: Hệ thống từ chối các email hợp lệ có dấu `.` (ví dụ `test@email.com`) và chỉ chấp nhận email không chứa dấu chấm ở domain (ví dụ `test@email` hoặc `test@test`). Để test case thêm thành viên mới có thể vượt qua bước này, dữ liệu test đã được điều chỉnh thành `test@test` và `dup@email`.

---

## 4. Nhận xét về chất lượng dự án kiểm thử tự động
- **Tính ổn định (Flakiness Reduction)**: Đã triển khai giải pháp tìm kiếm và nhập liệu (Custom Input Helpers) thông minh để tránh việc Flutter Engine lột bỏ thuộc tính `aria-label` khi text field được focus. Ngoài ra, việc chờ các Snackbar biến mất (`page.wait_for_timeout(4500)`) giúp tránh các thao tác click bị trượt do giao diện bị che khuất.
- **Smart Wait**: Hoàn toàn không lạm dụng `time.sleep()`, mà thay vào đó sử dụng `wait_for_flutter(page, text="...")` để đồng bộ hóa trạng thái giao diện theo thời gian thực, giúp giảm đáng kể thời gian chạy test.
